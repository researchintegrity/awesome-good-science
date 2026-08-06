#!/usr/bin/env python3
"""
curate_articles.py — Automated literature curation for awesome-good-science.

Uses the Google Gemini API with Google Search Grounding to discover new
research-integrity literature, format it to match the repository's Markdown
style, and update README.md so that an automated PR can be opened.

Usage:
    python scripts/curate_articles.py              # normal run
    python scripts/curate_articles.py --dry-run    # preview without writing

Environment variables:
    GEMINI_API_KEY  – required; Google AI Studio API key
    GEMINI_MODEL    – optional; override the default model (gemini-2.5-flash)
"""

from __future__ import annotations

import json
import logging
import os
import re
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from google import genai
from google.genai import types

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("curate_articles")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
README_PATH = REPO_ROOT / "README.md"
DEFAULT_MODEL = "gemini-3.6-flash"
MAX_RETRIES = 5
RETRY_BASE_DELAY = 5  # seconds
SEARCH_WINDOW_DAYS = 14
# Delay between Gemini calls to avoid rate-limit bursts (seconds)
INTER_QUERY_DELAY = 8


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------
@dataclass
class ArticleEntry:
    """A single curated article / paper / tool discovered by the search."""

    title: str
    url: str
    authors: str = ""
    year: str = ""
    summary: str = ""


@dataclass
class SectionInfo:
    """Metadata about a README section that we can auto-curate."""

    heading: str
    level: int  # 2 → ##, 3 → ###
    start_line: int  # 0-indexed
    end_line: int  # 0-indexed, inclusive
    format_type: str  # "year_prefixed" | "bullet_list"
    search_topic: str = ""


# ---------------------------------------------------------------------------
# Section configuration
# ---------------------------------------------------------------------------
# Maps *exact* section headings (as they appear in README.md) to their
# search topic and Markdown format type.
SECTION_CONFIG: dict[str, dict[str, str]] = {
    "Integrity Reports": {
        "format": "year_prefixed",
        "topic": (
            "scientific misconduct investigations, paper mill discoveries, "
            "large-scale retraction studies, research fraud exposés, and "
            "reports on the integrity of the scientific record"
        ),
    },
    "Image Integrity Methods": {
        "format": "year_prefixed",
        "topic": (
            "scientific image forensics methods, biomedical image manipulation "
            "detection, western blot forgery detection, copy-move forgery "
            "detection in scientific figures, deepfake detection for "
            "scientific images, and synthetic image attribution"
        ),
    },
    "Public Image Integrity Datasets": {
        "format": "bullet_list",
        "topic": (
            "new public datasets for scientific image integrity, biomedical "
            "image forgery benchmarks, scientific figure manipulation datasets, "
            "and western blot or gel electrophoresis forensic datasets"
        ),
    },
    "Text Integrity Methods": {
        "format": "year_prefixed",
        "topic": (
            "AI-generated text detection in scientific papers, tortured "
            "phrase detection, paper mill screening using NLP, plagiarism "
            "detection in academic publishing, and citation manipulation "
            "detection methods"
        ),
    },
    "Public Text Integrity Datasets": {
        "format": "bullet_list",
        "topic": (
            "new public datasets for detecting AI-generated scientific text, "
            "tortured phrase corpora, and text integrity benchmarks"
        ),
    },
    "Gene Integrity Methods": {
        "format": "year_prefixed",
        "topic": (
            "nucleotide sequence verification in biomedical papers, gene "
            "nomenclature error detection, reagent misidentification "
            "screening, and automated fact-checking of genetic data in "
            "publications"
        ),
    },
    "Statistics and Science of Science": {
        "format": "year_prefixed",
        "topic": (
            "meta-research and science-of-science studies, publication trend "
            "analyses, funding impact assessments, reproducibility crisis "
            "updates, and large-scale bibliometric analyses of the "
            "scientific literature"
        ),
    },
    "Commercial Tools": {
        "format": "bullet_list",
        "topic": (
            "new commercial or SaaS tools for scientific integrity checking, "
            "image duplication detection services, manuscript screening "
            "platforms, and AI-powered publication ethics tools"
        ),
    },
}


# ═══════════════════════════════════════════════════════════════════════════
# README Parser
# ═══════════════════════════════════════════════════════════════════════════
class ReadmeParser:
    """Parses README.md to extract section structure and existing URLs."""

    # Regex for markdown links: [text](url)
    _URL_RE = re.compile(r"\[([^\]]*)\]\((https?://[^)]+)\)")
    # Regex for heading lines (## or ###)
    _HEADING_RE = re.compile(r"^(#{2,3})\s+(.+)$")

    def __init__(self, readme_path: Path) -> None:
        self.path = readme_path
        self.raw_text: str = ""
        self.lines: list[str] = []
        self.sections: list[SectionInfo] = []
        self.existing_urls: set[str] = set()
        self._parse()

    # ── internal ──────────────────────────────────────────────────────────

    def _parse(self) -> None:
        """Read the file, extract headings/sections, and collect URLs."""
        self.raw_text = self.path.read_text(encoding="utf-8")
        self.lines = self.raw_text.splitlines(keepends=True)
        self._extract_sections()
        self._extract_urls()
        logger.info(
            "Parsed README: %d lines, %d searchable sections, %d existing URLs",
            len(self.lines),
            len(self.sections),
            len(self.existing_urls),
        )

    def _extract_sections(self) -> None:
        """Identify heading lines, compute ranges, map to config."""
        headings: list[tuple[int, int, str]] = []  # (line_idx, level, text)
        for idx, line in enumerate(self.lines):
            m = self._HEADING_RE.match(line.rstrip())
            if m:
                headings.append((idx, len(m.group(1)), m.group(2).strip()))

        for i, (line_num, level, heading) in enumerate(headings):
            end = headings[i + 1][0] - 1 if i + 1 < len(headings) else len(self.lines) - 1
            cfg = SECTION_CONFIG.get(heading)
            if cfg is None:
                continue  # not a section we curate
            self.sections.append(
                SectionInfo(
                    heading=heading,
                    level=level,
                    start_line=line_num,
                    end_line=end,
                    format_type=cfg["format"],
                    search_topic=cfg["topic"],
                )
            )

    def _extract_urls(self) -> None:
        """Collect every URL already present in README.md."""
        for line in self.lines:
            for m in self._URL_RE.finditer(line):
                url = m.group(2).rstrip("/")
                self.existing_urls.add(url)
                # Also store without trailing slash and with both http/https
                if url.startswith("https://"):
                    self.existing_urls.add("http://" + url[8:])
                elif url.startswith("http://"):
                    self.existing_urls.add("https://" + url[7:])

    # ── public helpers ────────────────────────────────────────────────────

    def find_insertion_line(self, section: SectionInfo) -> int:
        """Return the 0-indexed line where new entries should be inserted.

        Strategy:
          • Skip the heading line itself.
          • Skip blank lines and non-entry description paragraphs.
          • Return the index of the first actual entry (so we insert *before* it).
          • If the section is empty, return just after the heading + one blank line.
        """
        i = section.start_line + 1

        # Skip leading blank lines
        while i <= section.end_line and self.lines[i].strip() == "":
            i += 1

        if section.format_type == "year_prefixed":
            # Skip description paragraphs until we hit a **YYYY** entry
            while i <= section.end_line:
                stripped = self.lines[i].strip()
                if re.match(r"^\*\*\d{4}\*\*", stripped):
                    break
                # Also stop if we hit a sub-heading
                if stripped.startswith("#"):
                    break
                i += 1
        elif section.format_type == "bullet_list":
            while i <= section.end_line:
                stripped = self.lines[i].strip()
                if re.match(r"^- \[", stripped):
                    break
                if stripped.startswith("#"):
                    break
                i += 1

        return i


# ═══════════════════════════════════════════════════════════════════════════
# Gemini Curator
# ═══════════════════════════════════════════════════════════════════════════
class GeminiCurator:
    """Queries Gemini with Google Search Grounding to find new articles."""

    def __init__(self, api_key: str, model: str | None = None) -> None:
        self.client = genai.Client(api_key=api_key)
        self.model = model or os.environ.get("GEMINI_MODEL", DEFAULT_MODEL)
        self.search_tool = types.Tool(google_search=types.GoogleSearch())
        logger.info("Gemini client initialised (model=%s)", self.model)

    # ── public ────────────────────────────────────────────────────────────

    def search_for_section(
        self,
        section: SectionInfo,
        existing_urls: set[str],
    ) -> list[ArticleEntry]:
        """Search the web for recent articles matching *section* and return
        de-duplicated entries."""
        today = datetime.now()
        start_date = (today - timedelta(days=SEARCH_WINDOW_DAYS)).strftime("%B %d, %Y")
        end_date = today.strftime("%B %d, %Y")

        prompt = self._build_prompt(section, start_date, end_date)
        logger.info("Searching for section: %s", section.heading)

        try:
            response = self._call_with_retry(prompt)
        except Exception:
            logger.exception("Gemini API call failed for section '%s'", section.heading)
            return []

        if response is None or not response.text:
            logger.warning("Empty response for section '%s'", section.heading)
            return []

        entries = self._parse_response(response)

        # Deduplicate against existing URLs
        filtered: list[ArticleEntry] = []
        for entry in entries:
            normalized = entry.url.rstrip("/")
            if normalized in existing_urls:
                logger.debug("Skipping duplicate URL: %s", entry.url)
                continue
            # Also skip entries with empty or clearly invalid URLs
            if not entry.url.startswith("http"):
                logger.debug("Skipping invalid URL: %s", entry.url)
                continue
            filtered.append(entry)
            # Add to the set so intra-batch duplicates are caught
            existing_urls.add(normalized)

        logger.info(
            "Section '%s': found %d entries, %d new after dedup",
            section.heading,
            len(entries),
            len(filtered),
        )
        return filtered

    # ── private ───────────────────────────────────────────────────────────

    def _build_prompt(
        self, section: SectionInfo, start_date: str, end_date: str
    ) -> str:
        return (
            "You are a research librarian specialising in scientific integrity, "
            "research ethics, and reproducibility.\n\n"
            f"Search the web for scholarly articles, academic papers, preprints, "
            f"or official reports **published between {start_date} and {end_date}** "
            f"that are related to:\n\n"
            f"  {section.search_topic}\n\n"
            "Focus on:\n"
            "• Peer-reviewed journal articles (DOI links preferred)\n"
            "• Preprints on arXiv, bioRxiv, or medRxiv\n"
            "• Official reports from research integrity organisations\n"
            "• Significant coverage in Nature, Science, PNAS, The Lancet, BMJ, "
            "Retraction Watch, or similar established outlets\n\n"
            "Return your findings as a JSON array inside a ```json fenced code "
            "block.  Each object must have exactly these keys:\n\n"
            '  "title"   – the exact title of the paper or article\n'
            '  "url"     – the direct, canonical URL (DOI or publisher page)\n'
            '  "authors" – author list in "LastName, I." format; use "et al." '
            "after three authors\n"
            '  "year"    – publication year as a four-digit string\n'
            '  "summary" – a concise one-to-two-sentence description\n\n'
            "Rules:\n"
            "1. Only include results you are confident are real, published works.\n"
            "2. Do NOT fabricate entries or URLs.\n"
            "3. If you cannot find any relevant recent publications, return an "
            "empty JSON array: `[]`\n"
            "4. Return at most 10 entries, ranked by relevance.\n"
        )

    def _call_with_retry(self, prompt: str) -> Any:
        """Call Gemini with exponential back-off on rate-limit errors."""
        config = types.GenerateContentConfig(
            tools=[self.search_tool],
            temperature=0.1,
        )
        last_exc: Exception | None = None
        for attempt in range(MAX_RETRIES):
            try:
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt,
                    config=config,
                )
                return response
            except Exception as exc:
                last_exc = exc
                err_str = str(exc)
                if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                    delay = RETRY_BASE_DELAY * (2 ** attempt)
                    logger.warning(
                        "Rate-limited (attempt %d/%d). Retrying in %ds…",
                        attempt + 1,
                        MAX_RETRIES,
                        delay,
                    )
                    time.sleep(delay)
                else:
                    raise
        raise RuntimeError(
            f"Gemini API call failed after {MAX_RETRIES} retries"
        ) from last_exc

    def _parse_response(self, response: Any) -> list[ArticleEntry]:
        """Extract ArticleEntry objects from the Gemini text response.

        The response text is expected to contain a ```json code block with
        an array of article objects.
        """
        text: str = response.text or ""

        # Try to extract a JSON code block
        json_match = re.search(
            r"```(?:json)?\s*\n(.*?)```", text, re.DOTALL
        )
        if json_match:
            json_str = json_match.group(1).strip()
        else:
            # Fallback: try to find a bare JSON array in the text
            arr_match = re.search(r"(\[.*\])", text, re.DOTALL)
            if arr_match:
                json_str = arr_match.group(1).strip()
            else:
                logger.warning("No JSON found in Gemini response")
                return []

        try:
            data = json.loads(json_str)
        except json.JSONDecodeError as exc:
            logger.warning("Failed to parse JSON from response: %s", exc)
            return []

        if not isinstance(data, list):
            logger.warning("Expected JSON array, got %s", type(data).__name__)
            return []

        entries: list[ArticleEntry] = []
        for item in data:
            if not isinstance(item, dict):
                continue
            title = str(item.get("title", "")).strip()
            url = str(item.get("url", "")).strip()
            if not title or not url:
                continue
            entries.append(
                ArticleEntry(
                    title=title,
                    url=url,
                    authors=str(item.get("authors", "")).strip(),
                    year=str(item.get("year", "")).strip(),
                    summary=str(item.get("summary", "")).strip(),
                )
            )
        return entries


# ═══════════════════════════════════════════════════════════════════════════
# Markdown formatting helpers
# ═══════════════════════════════════════════════════════════════════════════

def format_year_prefixed(entry: ArticleEntry) -> str:
    """Format an entry in the year-prefixed style used for papers.

    Example output:
        **2025** - [Title](URL) - Authors.

        - Summary.

    """
    year = entry.year or str(datetime.now().year)
    author_part = f" - {entry.authors}" if entry.authors else ""
    # Ensure authors end with a period if present
    if author_part and not author_part.rstrip().endswith("."):
        author_part = author_part.rstrip() + "."
    line = f"**{year}** - [{entry.title}]({entry.url}){author_part}\n"
    if entry.summary:
        summary = entry.summary.rstrip(".")
        line += f"\n- {summary}.\n"
    line += "\n"
    return line


def format_bullet_list(entry: ArticleEntry) -> str:
    """Format an entry in the bullet-list style used for datasets/tools.

    Example output:
        - [Name](URL)
          - Description.

    """
    line = f"- [{entry.title}]({entry.url})\n"
    if entry.summary:
        summary = entry.summary.rstrip(".")
        line += f"  - {summary}.\n"
    return line


FORMATTERS = {
    "year_prefixed": format_year_prefixed,
    "bullet_list": format_bullet_list,
}


# ═══════════════════════════════════════════════════════════════════════════
# README updater
# ═══════════════════════════════════════════════════════════════════════════

def insert_entries(
    lines: list[str],
    section: SectionInfo,
    entries: list[ArticleEntry],
    insertion_line: int,
) -> list[str]:
    """Return a new list of lines with *entries* inserted at *insertion_line*.

    The entries are formatted according to the section's format_type.
    """
    formatter = FORMATTERS[section.format_type]
    block = ""
    for entry in entries:
        block += formatter(entry)

    new_lines = list(lines)
    # Split the block into individual lines (preserving newlines)
    block_lines = [l + "\n" if not l.endswith("\n") else l for l in block.splitlines()]
    # Ensure there is a blank line before existing content
    if (
        insertion_line < len(new_lines)
        and new_lines[insertion_line].strip() != ""
        and block_lines
        and block_lines[-1].strip() != ""
    ):
        block_lines.append("\n")
    new_lines[insertion_line:insertion_line] = block_lines
    return new_lines


# ═══════════════════════════════════════════════════════════════════════════
# Main entry point
# ═══════════════════════════════════════════════════════════════════════════

def main() -> None:
    dry_run = "--dry-run" in sys.argv

    # ── 1. Validate environment ───────────────────────────────────────────
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key:
        logger.error(
            "GEMINI_API_KEY environment variable is not set. "
            "Please set it to your Google AI Studio API key."
        )
        sys.exit(1)

    if not README_PATH.exists():
        logger.error("README.md not found at %s", README_PATH)
        sys.exit(1)

    # ── 2. Parse README ──────────────────────────────────────────────────
    parser = ReadmeParser(README_PATH)
    if not parser.sections:
        logger.warning("No searchable sections found in README.md. Exiting.")
        sys.exit(0)

    # ── 3. Search for new articles per section ───────────────────────────
    curator = GeminiCurator(api_key)
    # We accumulate (section, entries, insertion_line) tuples.
    # Entries must be inserted from *bottom to top* so that line numbers
    # computed from the original file remain valid after each insertion.
    updates: list[tuple[SectionInfo, list[ArticleEntry], int]] = []

    for section in parser.sections:
        entries = curator.search_for_section(section, parser.existing_urls)
        if entries:
            ins_line = parser.find_insertion_line(section)
            updates.append((section, entries, ins_line))
        # Politeness delay between API calls
        time.sleep(INTER_QUERY_DELAY)

    if not updates:
        logger.info("No new entries found across any section. README unchanged.")
        sys.exit(0)

    # ── 4. Insert entries into README (bottom-up to preserve line nums) ──
    lines = list(parser.lines)
    # Sort updates by insertion line descending so earlier insertions don't
    # shift later ones.
    updates.sort(key=lambda t: t[2], reverse=True)
    total_new = 0
    for section, entries, ins_line in updates:
        lines = insert_entries(lines, section, entries, ins_line)
        total_new += len(entries)
        logger.info(
            "Inserted %d entries into '%s' at line %d",
            len(entries),
            section.heading,
            ins_line + 1,
        )

    # ── 5. Write updated README ──────────────────────────────────────────
    if dry_run:
        logger.info("[DRY RUN] Would write %d new entries. Preview:", total_new)
        print("".join(lines))
    else:
        README_PATH.write_text("".join(lines), encoding="utf-8")
        logger.info(
            "README.md updated successfully with %d new entries.", total_new
        )

    # ── 6. Summary ───────────────────────────────────────────────────────
    logger.info("=== Curation Summary ===")
    for section, entries, _ in sorted(updates, key=lambda t: t[0].start_line):
        logger.info("  %-40s  +%d entries", section.heading, len(entries))
    logger.info("  %-40s  +%d entries", "TOTAL", total_new)


if __name__ == "__main__":
    main()
