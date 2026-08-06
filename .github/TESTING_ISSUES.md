# 🧪 Testing & Validation Issues for Literature Curation Automation

This document outlines the testing tasks and issue templates required to fully validate and finalize the automated literature monitoring pipeline.

---

## Issue 1: Test Gemini API Rate Limits & Query Optimization
**Labels:** `automation`, `performance`, `testing`

### Description
The literature curation script queries the Google Gemini API with Google Search Grounding across 8 README sections. Under free-tier constraints (5 requests per minute limit), sequential querying requires strict delay management.

### Tasks
- [ ] **Benchmark Query Execution:** Run `python scripts/curate_articles.py --dry-run` and measure execution time across all 8 sections with the 65s delay (~8.5–9 minutes total runtime).
- [ ] **Prompt Aggregation Testing:** Investigate consolidating section searches into 2–3 broader multi-topic prompts instead of 8 separate queries to reduce total API calls.
- [ ] **Rate Limit Error Handling:** Test API fallback when hitting HTTP 429 to verify exponential backoff and retry behavior.

---

## Issue 2: Validate Search Grounding Relevance, Freshness & Deduplication
**Labels:** `automation`, `quality-assurance`, `testing`

### Description
Ensure Gemini Google Search Grounding outputs accurate, recent, non-duplicated literature entries formatted to match the repository style.

### Tasks
- [ ] **URL Verification:** Verify that extracted URLs resolve directly to canonical publisher pages (DOIs, PubMed, bioRxiv, arXiv) rather than Google Search redirect links.
- [ ] **Publication Date Window:** Confirm that discovered papers were published within the target 14-day window.
- [ ] **Deduplication Check:** Confirm that existing URLs in `README.md` (200+ links) are successfully skipped.
- [ ] **Formatting Consistency:** Check that year-prefixed entries (`**YYYY** - [Title](URL) - Authors.`) and bullet-list entries (`- [Name](URL)`) match existing README syntax.

---

## Issue 3: End-to-End Workflow Execution & Pull Request Validation
**Labels:** `ci/cd`, `github-actions`, `testing`

### Description
Verify end-to-end pipeline execution in GitHub Actions via `workflow_dispatch`.

### Tasks
- [ ] **Manual Dispatch Verification:** Trigger `.github/workflows/weekly_curation.yml` manually from GitHub Actions UI.
- [ ] **Pull Request Creation:** Verify that `peter-evans/create-pull-request@v7` successfully opens a PR on branch `curation/update-<run_id>`.
- [ ] **Permission Audit:** Confirm repository permissions for `GITHUB_TOKEN` vs custom Personal Access Token (`PAT_TOKEN`) if downstream CI checks are needed.
- [ ] **Re-enable Schedule:** Once testing passes, uncomment the cron schedule (`0 9 * * 1`) in `.github/workflows/weekly_curation.yml`.
