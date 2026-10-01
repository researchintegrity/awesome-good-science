# The Good Science Repository [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of resources, tools, datasets, and papers related to scientific integrity, misconduct detection, and the science of science.

## Table of Contents

- [Research Motivation and Integrity News](#research-motivation-and-integrity-news)
- [Image Integrity](#image-integrity)
  - [Methods](#image-integrity-methods)
  - [Datasets](#image-integrity-datasets)
- [Text Integrity](#text-integrity)
  - [Methods](#text-integrity-methods)
  - [Datasets](#text-integrity-datasets)
- [Gene Integrity](#gene-integrity)
- [Statistics and Science of Science](#statistics-and-science-of-science)
  - [Datasets](#public-retraction-datasets)
- [Commercial Tools](#commercial-tools)
- [Organizations](#organizations)
- [Conferences and Journals](#conferences-and-journals)
- [Related Awesome Lists](#related-awesome-lists)
- [Contributing](#contributing)

## Research Motivation and Integrity News

Papers and reports denouncing cases of possible scientific misconduct or related issues.

### Integrity Reports

**2026** - [This award-winning microscopy image used AI — igniting controversy in a prestigious competition](https://www.nature.com/articles/d41586-026-03086-z) - Fieldhouse, R.

- A Nikon Small World in Motion award-winning video of cilia from a child with primary ciliary dyskinesia used AI for post-processing, and microscopy experts flagged biologically implausible structures that raised questions about whether the image misrepresented the underlying data.

**2026** - [Elsevier journal retracts 100+ papers for authorship issues, editor conflicts of interest](https://retractionwatch.com/2026/09/22/elsevier-journal-retracts-100-papers-for-authorship-issues-editor-conflicts-of-interest/) - Orrall, A.

- Elsevier's Science of the Total Environment retracted 165 papers in 2026 for unauthorized authorship changes, plagiarism and tortured phrases, and editor conflicts of interest, following the journal's November 2025 delisting from Web of Science.

**2026** - [China punishes prominent academics exposed by research sleuth](https://www.nature.com/articles/d41586-026-02890-x) - You, X.

- China's National Natural Science Foundation disciplined four senior academics with multi-year funding bans after a video blogger's analysis of Nature-branded papers found data fabrication and tampering, part of a wider crackdown on 31 research groups.

**2026** - [Paper mill studies get cited by clinical guidelines, policy docs and more, analysis finds](https://retractionwatch.com/2026/09/17/paper-mill-studies-get-cited-by-clinical-guidelines-policy-docs-and-more-analysis-finds/) - Chawla, D.S.

- An analysis of nearly 2,000 papers tied to the Pharmakon Neuroscience Network paper mill found 480 cited in patents, 57 in policy documents and 12 in clinical guidelines, while 90% of associated authors kept publishing after the mill's 2022 exposure.

**2026** - [The Emerging AI Paper-Review Arms Race: Adversarial Co-Evolution in Scholarly Publishing](https://arxiv.org/abs/2609.07713) - Wang, C. et al.

- A survey of 230 publications maps six interacting dynamics, from AI-scaled production to evaluation manipulation and evasion, arguing that trustworthy evaluation, not generation speed, is now the binding constraint on scholarly publishing.

**2026** - [Procrastination study by Duke's Dan Ariely retracted after sleuths find signs of data tampering](https://retractionwatch.com/2026/09/03/procrastination-study-duke-dan-ariely-psychological-science-data-colada-tampering-retraction/) - Travis, K.

- A 24-year-old, nearly 1,000-times-cited Psychological Science paper on deadlines and procrastination by Dan Ariely and Klaus Wertenbroch was retracted after Data Colada found duplicated values, implausible effects, and a falsified analysis submitted in response to a reviewer request.

**2026** - [Nations expanding their research programmes impose sweeping penalties for malpractice](https://www.nature.com/articles/d41586-026-02517-1) - Plackett, B.

- India, Peru and Vietnam are introducing government-level penalties for research misconduct, from funding bans and bonus clawbacks to national violation databases, prompting debate over distinguishing fraud from honest error.

**2026** - [Hundreds of paper-mill papers peddled in ads were later published](https://doi.org/10.1126/science.ael6249) - Brainard, J.

- A news investigation traces hundreds of paper-mill manuscripts advertised for sale on social media to their eventual appearance as published articles in legitimate journals, illustrating how mill output moves from marketplace to the indexed literature.

**2026** - [Sage issues dozens of retractions from two journals it acquired](https://retractionwatch.com/2026/08/17/sage-issues-dozens-of-retractions-from-two-journals-it-acquired/) - Orrall, A.

- Sage retracted 43 papers from the Journal of Intelligent and Fuzzy Systems and 34 from the International Journal of Knowledge-Based and Intelligent Engineering Systems for third-party peer-review manipulation, citation manipulation and tortured phrases, extending an earlier mass retraction of over 1,500 JIFS papers.

**2026** - [Biology journal pulls 100+ articles and counting from special issues for peer review manipulation](https://retractionwatch.com/2026/08/12/biology-journal-pulls-100-articles-and-counting-from-special-issues-for-peer-review-manipulation/) - Orrall, A.

- Elsevier's International Journal of Biological Macromolecules retracted around 120 papers from guest-edited special issues after finding systematic, coordinated peer-review manipulation alongside plagiarism and image duplication, almost all involving authors at Chinese institutions during a period when the journal's output nearly doubled.

**2026** - [BMJ Group retracts paper on COVID-19 vaccines and mortality featured in Senate hearing](https://retractionwatch.com/2026/08/11/bmj-public-health-retraction-covid-19-vaccines-death-senate-hearing/) - Orrall, A.

- BMJ Public Health retracted a 2024 paper on COVID-19 excess mortality after an institutional investigation found negligence and likely plagiarism of Ariel Karlinsky's World Mortality Dataset; the paper had been cited in a U.S. Senate subcommittee hearing to suggest vaccine-death links.

**2026** - [Decade-long fraud by market survey firm a 'gut punch' for researchers](https://retractionwatch.com/2026/08/06/op4g-market-research-indictment-fake-data/) - Borrell, B.

- Eight defendants were indicted over a decade-long scheme at market research firm Op4G that sold clients survey data fabricated by mixing real and invented responses, defrauding roughly $10 million and leaving researchers at several universities now reviewing potentially compromised published studies.

**2026** - [The barrier is purely financial: analysis of the acceptance rate and peer review practice of predatory journals using AI generated papers](https://doi.org/10.1186/s41073-026-00238-7) - Poland, K., and Davies, P.

- Submitted AI-generated and other low-quality manuscripts to predatory journals and found high acceptance rates with minimal or no substantive review, showing financial motive overrides quality control.

**2026** - [More than 18,000 questionable images found in antibody catalogues of 15 companies](https://www.nature.com/articles/d41586-026-02635-w) - Garisto, D.

- Metascientist Reese Richardson found over 18,000 potentially altered validation images across 17,495 antibody products from 15-16 vendors; more than half of the antibodies reportedly did not work as advertised. Underlying data: [Zenodo dataset](https://zenodo.org/records/22090940). Related coverage: [Science](https://www.science.org/content/article/fraudulent-images-are-rife-antibody-sellers-websites-researcher-says), [The Scientist](https://www.the-scientist.com/misleading-antibody-validation-images-controversy-expands-to-15-vendors-74915), [Reese Richardson's blog](https://reeserichardson.blog/2026/08/25/at-least-15-companies-are-selling-antibodies-using-faked-validation-data/).

**2026** - [Follow-up investigation of ethics approvals and regulatory compliance in publications from the IHU-Mi](https://doi.org/10.1186/s41073-026-00234-x) - Frank, F., Bik, E.M., Meyerowitz-Katz, G., et al.

- Audited 2,674 publications from the IHU-Méditerranée Infection, finding ethical concerns in 853 articles and mismatches between stated approvals and the research actually described in 81.3% of the 374 cases where approval documents were obtained.

**2026** - [Zombie trials are often monocentric and cluster within fabricated evidence "factories": a cohort study of 236 retracted randomized controlled trials with confirmed data fabrication](https://doi.org/10.64898/2026.07.23.26357975) - Jajieh, T., Chapelle, C., Lemarchand, C., et al.

- Of 236 RCTs retracted for confirmed data fabrication, 83.5% involved repeat offenders and a single author accounted for 104 trials; repeat-offender trials took 13.6 years to retract versus 2.75 years for one-off cases.

**2026** - [Fabricated citations: an audit across 2·5 million biomedical papers](https://doi.org/10.1016/S0140-6736(26)00603-3) - Topaz, M., Roguin, N., Gupta, P., et al.

- An AI-assisted audit of ~2.5 million open-access papers and ~97 million references found nearly 3,000 papers citing publications that cannot be matched to any known work, with fabricated-citation rates rising roughly 12-fold in two years.

**2026** - [Research integrity within systematic reviews: investigating the prevalence of studies by authors with multiple retraction histories in Cochrane reviews](https://doi.org/10.1186/s41073-026-00205-2) - Zaw, T.M.M., Heathers, J., and Meyerowitz-Katz, G.

- Across 9,323 Cochrane reviews, 81 cite work by authors with 24 or more retractions, and only 6 of the 32 reviews that meta-analysed such studies ran a sensitivity analysis excluding them.

**2026** - [Publishers' responses to integrity concerns – does the type of notice influence subsequent citations? A cohort study](https://doi.org/10.64898/2026.02.25.26346683) - Studd, H., Avenell, A., Grey, A., and Bolland, M.J.

- Citation decline after an editorial notice did not differ by notice type, nor from the natural decline of matched controls; notices arrive on average five years after publication, by which point the papers are already embedded.

**2026** - [Editorial expressions of concern are infrequent even for researchers with multiple retracted publications – An observational study](https://doi.org/10.1080/08989621.2026.2671154) - Grey, A., Avenell, A., and Bolland, M.

- Journals rarely issue expressions of concern about the remaining literature of authors who already have multiple retractions, leaving the unretracted work of serial offenders unflagged.

**2026** - [Suspected distortion of citations in high-impact cancer journals](https://doi.org/10.64898/2026.05.25.727627) - Scancar, B., Byrne, J.A., Causeur, D., and Barnett, A. - [News](https://www.nature.com/articles/d41586-026-01908-8)

- Molecular cancer papers carrying the textual signature of retracted paper-mill articles receive 50–100% more citations than comparable articles while attracting fewer readers, evidence of deliberate citation inflation feeding journal impact factors.

**2026** - [When science corrects itself but patents do not: Retractions, boundary infrastructure, and downstream invention](https://doi.org/10.2139/ssrn.6904220) - Kim, H.

- Screened 13 million US patents and found 401 citing retracted papers, with 71.6% of those exposures falling in windows where a correction was still actionable before filing or during examination.

**2026** - [The 'shades of grey' in research integrity—Researchers admit to questionable research practices that they do not perceive to be serious](https://doi.org/10.1371/journal.pone.0339056) - Entradas, M., Feng, Y., and Carneiro e Sousa, I.

- In a survey of 1,573 researchers, about 92% admitted to at least one questionable research practice, with engagement predicted most strongly by perceiving the practice as not serious.

**2026** - ['A waste of time for all of us': caught in the crossfire of the peer-review wars](https://www.nature.com/immersive/d41586-026-01360-8/index.html) - Zimmer, K.

- A long-form investigation into "review mills" producing duplicated peer-review reports that demand coercive citations, spanning thousands of manuscripts across MDPI, Springer Nature and Taylor & Francis.

**2026** - [Hallucinated citations are polluting the scientific literature. What can be done?](https://www.nature.com/articles/d41586-026-00969-z) - Naddaf, M., and Quill, E.

- A news feature surveying the fabricated-reference problem and the detection landscape responding to it, reporting that tens of thousands of 2025 publications may carry invalid citations.

**2026** - [Growing use of guest editors has turned some journals into a 'playground of bad science'](https://www.statnews.com/2026/04/24/science-journal-retractions-highlight-guest-editor-special-edition-problem/) - Oza, A.

- Reports on guest-edited special issues as the main vector for paper-mill output, hung on the near-total retraction of one guest-edited special issue for compromised peer review.

**2026** - [Controversial editorial practices boost plastic surgeon's publishing empire](https://retractionwatch.com/2026/03/12/riaz-agha-international-journal-surgery-research-registry-wolters-kluwer/) - Joelving, F.

- An investigation showing that self-citation of reporting guidelines supplied 3.4 points of one journal's 15.3 impact factor; Clarivate placed six of the group's journals on hold in Web of Science three months later.

**2026** - [Office of Research Integrity Annual Report 2025](https://ori.hhs.gov/sites/default/files/2026-08/2025%20ORI%20Annual%20Report_final.pdf) - Office of Research Integrity (ORI), U.S. Department of Health and Human Services

- ORI received 446 misconduct allegations in CY2025 and closed 177 cases, returning 43 findings of research misconduct, 2 debarments and 3 supervision plans.

**2026** - [Safeguarding Scholarly Communication: Publisher Practices to Uphold Research Integrity](https://stm-assoc.org/new-report-documents-publisher-investment-in-research-integrity-infrastructure/) - Storan, D., and Chiarelli, A., for the STM Research Integrity Committee

- An industry stocktake reporting research-integrity teams of 100+ staff at some publishers and over 2 million submissions screened in 8–9 months, while concluding that publisher action alone is insufficient.

**2026** - [AI-Generated Figures in Academic Publishing: Policies, Tools, and Practical Guidelines](https://arxiv.org/abs/2603.16159) - Chen, D.

- Surveys how major publishers regulate AI-generated figures and proposes disclosure, human-review and record-keeping guidelines for authors, calling on publishers to invest in detection during peer review.

**2026** - [Medical students are using a popular research tool to pump out misleading studies](https://www.science.org/content/article/medical-students-are-using-popular-research-tool-pump-out-misleading-studies) - Science

- Reports a surge of low-quality observational studies mass-produced from a federated electronic health record platform, where easy analyses fuel quick publications from inexperienced authors.

**2026** - [Citation cartels use fake author names to target chemistry journals](https://cen.acs.org/research-integrity/Citation-cartels-use-fake-author/104/web/2026/02) - Chemical & Engineering News

- Reports on citation cartels creating fictitious author identities in order to inflate citation counts in chemistry journals.

**2025** - [The entities enabling scientific fraud at scale are large, resilient, and growing rapidly](https://www.pnas.org/doi/10.1073/pnas.2420092122) - Richardson, R.A.K. et al. - [Video](https://www.youtube.com/watch?v=YdVwUv1bfWE)

- Discusses the industrial scale of "paper mills," revealing that they are growing rapidly (doubling every ~1.5 years) and are resilient to current interventions like retractions.  

**2025** - The View from a Mega Journal- Spick, M. -[Video](https://www.youtube.com/watch?v=5bNVQXpQpUw) 

- A presentation discussing paper mills and integrity issues from the perspective of a mega-journal editor and researcher.

**2025** - [Retracted clinical trials in systematic reviews and guidelines](https://www.bmj.com/content/389/bmj.r724) - Avenell, A., Bolland, M.J., et al. - [Video](https://youtu.be/u692orGfu1Q?si=Ug2d2hCBsujbT84t)

- Investigates the extent to which retracted clinical trials continue to be cited in systematic reviews and clinical guidelines, potentially compromising medical advice.  

**2025** - [Misconduct Detection — Evolving Methods & Lessons from 15 Years of Scientific Image Sleuthing](https://www.cambridge.org/core/journals/journal-of-law-medicine-and-ethics/article/misconduct-detection-evolving-methods-lessons-from-15-years-of-scientific-image-sleuthing/B10AC2793CC5DA6DE8A37E6893CB55A4) - Brookes, P.S.

- Reflects on 15 years of experience in scientific image sleuthing, discussing the evolution of detection methods and the broader implications for scientific integrity.

**2024** - [Widespread misidentification of SEM instruments in the peer-reviewed materials science and engineering literature](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0326754) - Richardson, R.A.K. et al.

- Developed a semi-automated pipeline to detect misreporting of Scanning Electron Microscope (SEM) instrumentation, finding that 21.2% of analyzed articles had image metadata that did not match the text.

**2024** - [Paying for open, perverse incentives and problematic scholarship](https://www.youtube.com/watch?v=XzCJZAkuKO0) - Khoo, S.

- Examines how the author-pays model of Open Access creates perverse incentives and contributes to the stratification of publishing.  

**2024** - [The landscape of biomedical research](https://www.cell.com/patterns/fulltext/S2666-3899(24)00076-X) - González-Márquez, R. et al. - [Video](https://youtu.be/zDDa3pWYadQ?si=cmhxVAr6xTQy_25t)

- Uses text mining and visualization techniques to identify clusters of papers with suspiciously similar textual features, potentially indicating paper mill activity.  

**2024** - [Image misconduct in published research articles - how to spot them and how to prevent them](https://youtu.be/J6ANspM6tA4?si=_IWwCyc8nj44GwjP) - Bazargan, K. - [Video](https://youtu.be/--E9_WUrgDs?si=PAZwXzXb-AQ3TdsM)

- A presentation by the founder of River Valley Technologies discussing image manipulation and the importance of using high-resolution and vector graphics to prevent it.

**2023** - Screening studies for fake research - Lisa Parker - [Video](https://youtu.be/--E9_WUrgDs?si=PAZwXzXb-AQ3TdsM)


**2023** - [Seven signs of fraud in individual participant data](https://youtu.be/7qr8Us-PF6A?si=_6g8T0TdvoG4ttgb) - Khoo, S.Y.S. - [Video](https://youtu.be/7qr8Us-PF6A?si=_6g8T0TdvoG4ttgb)

The inspiration for the talk was the trails of ivermectin for treatment of COVID-19. The seven techniques ranges from blatant cases such as duplicate patients, through to more subtle manifestations such as unlikely homogeneity or heterogeneity.

**2023** - [“Conducted Properly, Published Incorrectly”: The Evolving Status of Gel Electrophoresis Images Along Instrumental Transformations in Times of Reproducibility Crisis](https://onlinelibrary.wiley.com/doi/10.1002/bewi.202200051) - Callaerts, N. et al.

- "Our aim is to analyze the evolving epistemic status of generated images and its connection with a crisis of trust in images within that field". They are focused on Gel Electrophoresis images.

**2023** - [Analysis and Correction of Inappropriate Image Duplication: the Molecular and Cellular Biology Experience](https://www.tandfonline.com/doi/full/10.1128/MCB.00309-18) - Bik E., Fang F.C., Kullas A.L., Davis R.J., and Casadevall A.

- MCB instituted a pilot program to screen images of accepted papers prior to publication.

**2022** - [Quality Output Checklist and Content Assessment (QuOCCA): a new tool for assessing research quality and reproducibility](https://bmjopen.bmj.com/content/12/9/e060976) - Héroux, M.E. et al. - [Video](https://www.youtube.com/watch?v=t9xs7rTdR7E)

- Presents QuOCCA, a tool for assessing research quality and reproducibility in biomedical publications.  


**2022** - [Blind spots on western blots: Assessment of common problems in western blot figures and methods reporting with recommendations to improve them](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3001783) - Kronn, C. et al.

- Systematically examined 551 articles published in the top 25% of journals in neurosciences (n = 151\) and cell biology (n = 400\) that contained western blot images. Most published western blots are cropped and blot source data are not made available to readers in the supplement.

**2022** - [Development of the individual participant data integrity tool](https://onlinelibrary.wiley.com/doi/10.1002/jrsm.1739) - Sheldrick, K. et al.

- Describes the development of a tool to detect integrity issues in randomized trials using individual participant data, highlighted by the Ivermectin fraud investigations.  

**2021** - [Investigating the replicability of preclinical cancer biology](https://elifesciences.org/articles/71601) - Errington, T.M. et al.

- A massive project investigating the replicability of preclinical cancer biology research, highlighting barriers such as lack of data sharing and incomplete methods.  

**2019** - [Figure errors, sloppy science, and fraud: keeping eyes on your data](https://www.jci.org/articles/view/128380) - Williams C.L., Casadevall A., and Jackson S.

- Introduced several data screening checks for manuscripts prior to acceptance.

**2019** - [Compliance with ethical standards in the reporting of donor sources and ethics review in peer-reviewed publications involving organ transplantation in China: a scoping review](https://bmjopen.bmj.com/content/9/2/e024473) - Rogers, W. et al.

- Investigates the extent to which Chinese transplant research complies with international ethical standards regarding donor sources and consent.  

**2016** - [The Prevalence of Inappropriate Image Duplication in Biomedical Research Publications](https://journals.asm.org/doi/10.1128/mbio.00809-16) - Bik, E., Casadevall, A., and Fang F.C. 🔥🔥🔥

- A game-changing article. The images from **20,621 papers published in 40 scientific journals from 1995 to 2014** were visually screened. **3.8% of published papers contained problematic figures.**

**2013** - [Manipulation and Misconduct in the Handling of Image Data](https://academic.oup.com/plphys/article/163/1/3/6110926) - Blatt, M., and Martin C.

- Discussion about ethics in image from Plant studies.

**2012** - [Digital Images Are Data: And Should Be Treated as Such](https://link.springer.com/protocol/10.1007/978-1-62703-056-4_1) - Cromey, D. 🔥🔥

- A well-established guideline regarding image integrity.

**2010** - [Identification and prevention of digital forgery in orthodontic records](https://www.sciencedirect.com/science/article/abs/pii/S0889540610007328) - Madhana, B., and Gayathrib, H.

- Examples of image tapering in odontology.

**2010** - [Forensic Examination of Questioned Scientific Images](https://www.tandfonline.com/doi/abs/10.1080/08989620212970) - Krueger, J. 🔥🔥

- Analysis of 35 cases involving questioned scientific images received by the Office of research Integrity (ORI) within (1989-2010).

## Image Integrity

### Image Integrity Methods


**2026** - [GAN-Blot: A Controllable Structure-Style Synthesis Benchmark for Western Blot Forensics](https://arxiv.org/abs/2609.06619) - Shao, H.-C. et al.

- Introduces a 46,000-image benchmark of synthetic western blots with independently controllable band geometry and visual style, finding domain experts and existing forensic detectors fail to identify 81.3% of the generated images as fake.

**2026** - [Rescind: Countering Image Misconduct in Biomedical Publications with Vision-Language and State-Space Modeling](https://arxiv.org/abs/2601.08040) - Nandi, S., and Natarajan, P.

- Introduces a ~600K-image benchmark of synthetic biomedical forgeries spanning classical, generative and VLM-guided manipulations, together with a state-space detector for localising duplication, splicing and region removal.

**2026** - [BioTamperNet: Affinity-Guided State-Space Model Detecting Tampered Biomedical Images](https://arxiv.org/abs/2602.01435) - Nandi, S., and Natarajan, P.

- Uses affinity-guided attention derived from state-space models to localise both a duplicated region and its source counterpart, arguing that detectors trained on natural images transfer poorly to biomedical data.

**2026** - [THEMIS: Towards Holistic Evaluation of MLLMs for Scientific Paper Fraud Forensics](https://arxiv.org/abs/2603.25089) - Ma, T.-Y. et al.

- A multi-task benchmark of 4,054 QA pairs built from 152 real retracted-paper cases plus synthetic manipulations, evaluating multimodal LLMs across five fraud types and sixteen manipulation operations.

**2026** - [SciFigDetect: A Benchmark for AI-Generated Scientific Figure Detection](https://arxiv.org/abs/2604.08211) - Hu, Y. et al.

- Pairs 72,965 real and 150,807 synthetic scientific figures with paper context and generation prompts, evaluating detectors under zero-shot transfer, cross-generator generalisation and degradation robustness.

**2026** - [Dynamically Perceived Forgery Conditional Diffusion Model for Scientific Image Tampering Localization](https://doi.org/10.1109/TCSVT.2026.3653499) - Xu, J. et al.

- Formulates tampering-mask prediction for scientific images as a conditional denoising process steered by a forgery condition and an enhanced edge condition, reporting strong cross-dataset robustness.

**2026** - [VrySure: A Multi-Task AI Scientific Fraud Detection Platform for Identifying Manipulated and AI-Generated Biomedical Research Images](https://doi.org/10.64898/2026.06.10.731492) - Sun, J. et al.

- An integrated screening platform combining cross-image reuse detection, within-image copy-move detection, blot and gel splicing detection, and AI-generated image detection, benchmarked against commercial tools.

**2026** - [Spectral Forensics of Diffusion Attention Graphs for Copy-Move Forgery Detection](https://arxiv.org/abs/2604.17287) - Tabib, H.M.S., Tias, T.A., and Tahmid, N.

- A training-free copy-move detector reading the spectral properties of self-attention affinity graphs from a pretrained diffusion model, benchmarked primarily on the Recod.ai/LUC scientific image forgery set.

**2026** - [BioForensNet: A Precision-First Framework for Pixel-Level Copy-Move Forgery Detection in Scientific Images](https://doi.org/10.1109/ICDCA69396.2026.11620297) - Maurya, V., Srivastava, G., and Kumari, L.

- Combines Vision Transformer representations with a structure-aware false-positive elimination stage, prioritising precision over recall to reduce false accusations in biomedical figure screening.

**2025** - [MultiFakeVerse: A Large-Scale Benchmark for Synthetic Image Detection in the Era of Vision-Language Models](https://arxiv.org/abs/2506.00868) - Gupta, P. et al.
- A large-scale deepfake dataset containing over 800,000 images generated by Vision-Language Models (VLMs) to benchmark detection of semantic image manipulations.

**2025** - [Forensics-Bench: A Comprehensive Forgery Detection Benchmark Suite for Large Vision Language Models](https://arxiv.org/abs/2503.15024) - Wang, J. et al.
- A benchmark for fake image detection that contains 1.44 million images generated by 38 diverse forgery methods to evaluate the performance of 50 state-of-the-art detection algorithms.

**2024** - [Explainable Artifacts for Synthetic Western Blot Source Attribution](https://ieeexplore.ieee.org/document/10810680) - Cardenuto, J.P. et al.

- Identifies explainable artifacts to attribute the source of synthetic western blots.

**2024**\- [Exposing image splicing traces in scientific publications via uncertainty-guided refinement](https://www.cell.com/patterns/fulltext/S2666-3899(24)00180-6) - Lin et al.

- Identifies splicing image manipulation on scientific images. It also proposes a dataset for the task.

**2024** - [Unveiling scientific articles from paper mills with provenance analysis](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0312666) - Cardenuto, J.P. et al.

- Uses provenance analysis to identify scientific articles generated by paper mills.

**2024** - [Detecting Biomedical Copy-Move Forgery by Attention-Based Multiscale Deep Descriptors](https://ieeexplore.ieee.org/abstract/document/10647460) - Shao, H. et al.

- Proposes a multiscale attention-based deep descriptor scheme for detecting copy-move forgery in biomedical research scenarios.

**2024** - [AI-Powered Western Blot Interpretation: A Novel Approach to Studying the Frameshift Mutant of Ubiquitin B (UBB+1) in Schizophrenia](https://www.mdpi.com/2076-3417/14/10/4149) - Fabijan, A. et al.

**2023** - [A Comprehensive Survey on Methods for Image Integrity](https://dl.acm.org/doi/10.1145/3633203) - Capasso, P. et al.

- A comprehensive survey reviewing methods for ensuring image integrity.

**2023** - Forensic Analysis of Scientific Images - Daniel Acuna, Guillaume Cabanac, Cyril Labbe, Jennifer Byrne - [Video](https://youtu.be/DXfcckLSG3c?si=FepYfY6AXpNwW_sY)


**2023** - [GH-DDM: the generalized hybrid denoising diffusion model for medical image generation](https://link.springer.com/article/10.1007/s00530-023-01059-0) - Zhang, S. et al.

- Presents a hybrid denoising diffusion model for generating medical images, relevant for understanding synthetic image generation in biomedicine.

**2023** - [Shrinking the Semantic Gap: Spatial Pooling of Local Moment Invariants for Copy-Move Forgery Detection](https://ieeexplore.ieee.org/abstract/document/10007894) - Wang, C. et al.

- Proposes spatial pooling of local moment invariants to bridge the semantic gap in copy-move forgery detection.

**2022** - [SILA: a system for scientific image analysis](https://www.nature.com/articles/s41598-022-21535-3) - Moreira, D. et al.

- Presents SILA, a system for analyzing scientific images for reuse and manipulation, including a new dataset.

**2022** - [Image forgery detection: a survey of recent deep-learning approaches](https://link.springer.com/article/10.1007/s11042-022-13797-w) - Zanardelli, M. et al.

- Surveys recent deep learning approaches for image forgery detection.

**2022** - [Benchmarking Scientific Image Forgery Detectors](https://link.springer.com/article/10.1007/s11948-022-00391-4) - Cardenuto et al.

- Proposed a dataset synthetically build with scientific forgeries (duplication and splicing). Using the dataset, they benchmarked the state-of-the-art copy-move forgery detectors of the epochs, which resulted in low performance for scientific images.

**2022** - [Forensic Analysis of Synthetically Generated Western Blot Images](https://ieeexplore.ieee.org/abstract/document/9785655) - Mandelli, S. et al.

- Analyzes synthetically generated western blot images for forensic purposes.

**2020** - [Scientific image tampering detection based on noise inconsistencies: A method and datasets](https://arxiv.org/abs/2001.07799) - Xiang, Z. and Acuna, D.E.

- Introduces a method using noise inconsistencies and a new dataset for image tampering detection.  

**2018** - [Automatic detection of image manipulations in the biomedical literature](https://www.nature.com/articles/s41419-018-0430-3) - Bucci, E.M.

- Proposes a method for detecting image manipulation of Gel Blots using proprietary tools.

**2018** - [Bioscience-scale automated detection of figure element reuse](https://www.biorxiv.org/content/10.1101/269415v3) - Acuna, D.E. et al.

- Discusses automated detection of figure element reuse at a bioscience scale.

**2006** - [Exposing digital forgeries in scientific images](https://dl.acm.org/doi/10.1145/1161366.1161374) - Farid, H.

- Discusses techniques for detecting digital forgeries in scientific images.

### Public Image Integrity Datasets


- [Problematic images in vendor antibody verification data](https://zenodo.org/records/22090940)
  * 18,943 suspicious or manipulated antibody verification images across 17,495 products from 16 vendors, with original images, annotated versions flagging the issues, and a spreadsheet cataloging each case with vendor and product details (Richardson, R. and David, S.).
- [Recod.ai/LUC Scientific Image Forgery Detection Challenge Set](https://www.kaggle.com/competitions/recodai-luc-scientific-image-forgery-detection)
  * A challenge set of 5,128 biomedical research images (2,377 authentic, 2,751 copy-move forged) used as the primary benchmark in recent copy-move forensics work.
- [Recod.ai Scientific Image Integrity Dataset (RSIID)](https://zenodo.org/records/15095089)
  * A benchmark dataset designed for evaluating forgery detection methods in scientific images.
- [Scientific Papers (SILA) Dataset](https://www.nature.com/articles/s41598-022-21535-3)  
  * Introduced in the SILA paper (2022), it contains scientific papers with annotated reuse and manipulation.  
- [Synthetic Western Blots Dataset](https://ieeexplore.ieee.org/abstract/document/9785655)  
  * A dataset of synthetically generated western blot images for forensic analysis (Mandelli et al., 2022).  
- [MIMIC-CXR](https://physionet.org/content/mimic-cxr/2.0.0/)  
  * 371,920 chest X-rays associated with 227,943 imaging studies from 65,079 patients.  
  * It might be useful to access the [MIMIC-CXR-JPG](https://physionet.org/content/mimic-cxr-jpg/2.1.0/), with images already in JPEG.

## Text Integrity

### Text Integrity Methods

**2026** - [Testing Our Foundations: Citation Trends, Errors, and Emerging Hallucinations in the Computing Education Literature](https://arxiv.org/abs/2609.16574) - Denny, P. et al.

- Analysing 24,751 computing-education papers and 15 million references, finds verified hallucinated citations at the SIGCSE Technical Symposium jumped from 3 in 2025 to 17 in 2026, affecting 2.3% of proceedings papers.

**2026** - [LLM-assisted writing and citation advantage: evidence from scientific publications before and after ChatGPT release](https://doi.org/10.1007/s11192-026-05805-9) - Paklina, S., Parshakov, P., and Rapoport, E.

- A classifier applied to 234,073 arXiv-Crossref papers finds that those flagged as LLM-assisted receive roughly 7% more citations than non-AI papers, even after controlling for journal quality and author reputation.

**2026** - [RefVerifier: Semi-Automated Reference Claim Verification for Scientific Manuscripts](https://arxiv.org/abs/2609.07652) - Mocan, S., Angermeir, F., and Kreitz, M.

- Introduces a four-stage pipeline that extracts citation-bearing claims, verifies bibliography metadata and localises supporting evidence in cited papers, reaching 71% end-to-end verdict accuracy on test manuscripts.

**2026** - [HalluPeer: A Taxonomy-driven Benchmark for Detecting Hallucinations in Scientific Peer Reviews](https://arxiv.org/abs/2609.03580) - Lin, T.-L. et al.

- A taxonomy-driven benchmark of 12,000 papers and over 38,000 reviews shows existing hallucination detectors struggle to separate fabricated claims from legitimate critique in AI-generated peer reviews, though domain-specific fine-tuning helps substantially.

**2026** - [Hallucination Rate of Peer-Reviewed Citations Generated by Large Language Models in Neurocritical Care](https://doi.org/10.1097/cce.0000000000001474) - Seifi, A., and Seyfi, A.

- Tested LLM-generated citations in a neurocritical care context and found 55.0% contained a citation inaccuracy and 28.3% were entirely fabricated, quantifying the scale of hallucinated references in a clinical subspecialty.

**2026** - [Systematic Plagiarism, Author Identity Misuse, and Fabricated Literature Citations in AI-Generated Herpetological Resources](https://doi.org/10.1670/3163630) - Blackburn, D.G.

- Documents a case of AI-generated herpetological reference works containing over 450 invalid citations alongside plagiarism and misuse of author identities, combining fabricated references with authorship fraud in one applied case.

**2026** - [Prompt injection compromises large language model-based peer review: evidence from randomised controlled trial abstracts from anaesthesia journals](https://doi.org/10.1016/j.bja.2026.06.041) - De Cassai, A., Dost, B., Pistollato, E., et al.

- Shows that hidden prompt-injection text embedded in RCT abstracts can manipulate LLM-based peer review outputs, exposing an adversarial vulnerability in using LLMs to assist manuscript review.

**2026** - [Detection of AI-Obfuscated, AI-Refined, and Humanized Text: A Systematic Review](https://doi.org/10.48084/etasr.20040) - Sharimbayev, B., and Kadyrov, S.

- A systematic review of 26 studies finds AI-text detectors degrade sharply on paraphrased, humanized or obfuscated text and show bias against non-native English writers, arguing detector scores should serve only as supportive evidence, not verdicts.

**2026** - [Most biomedical publications show signs of LLM-assisted writing](https://arxiv.org/abs/2608.10715) - Holzwarth, L., González-Márquez, R., and Kobak, D.

- Extends the excess-vocabulary method to paragraph level, finding that by the end of 2025, 89% of open-access biomedical papers show an excess of LLM-associated vocabulary, with Discussion sections far ahead of Methods.

**2026** - [Phantom References: Hallucinated Citations That Survive Peer Review at Top-Tier Conferences](https://arxiv.org/abs/2607.00738) - Russinovich, M., Siva Kumar, R.S., and Salem, A.

- Introduces RefChecker, an open-source pipeline that cross-checks every bibliographic entry against multiple scholarly databases; roughly 1 in 20 NeurIPS and USENIX Security 2025 papers carries at least two likely hallucinated references.

**2026** - [Fine-Grained Detection of AI-Generated Writing in the Biomedical Literature](https://doi.org/10.64898/2026.01.01.697311) - She, R.

- Passage-level detection across the biomedical literature finds near-zero AI text through 2024 and 12.4% of 2025 papers containing at least one localised AI-written passage, with a strong geographic and journal-tier skew.

**2026** - [Sem-Detect: Semantic Level Detection of AI Generated Peer-Reviews](https://arxiv.org/abs/2605.21713) - Duarte, A.V., Tufts, B., Oke, A., et al.

- Detects AI-written reviews by comparing claim-level semantics rather than surface style, separating fully human, LLM-refined and fully AI reviews across more than 20,000 ICLR and NeurIPS reviews.

**2026** - [Detecting AI-Generated Content in Academic Peer Reviews](https://arxiv.org/abs/2602.00319) - Shen, S., and Wang, K.

- Applies an AI-text detector to review reports over time, finding that by 2025 roughly one fifth of ICLR reviews and one eighth of Nature Communications reviews are flagged as AI-generated.

**2026** - [Detecting Hallucinated and Suspicious Citations: What Current Tools Can and Cannot Do](https://arxiv.org/abs/2607.22693) - Badalova, F., and Mayr, P.

- Reviews and hands-on evaluates the current crop of fabricated-citation detectors, finding them useful as early warnings but limited by reference-extraction errors and patchy database coverage.

**2026** - [Why AI Detection Fails for Academic Integrity](https://arxiv.org/abs/2608.11256) - Karr Jr, J.A., Khvatskii, G., Hua, T., and Chawla, N.V.

- Commercial detectors flag minor human edits to published abstracts at 64–80% while flagging unmodified recent human text at 9–15%, concluding that detector scores cannot stand alone as evidence of misconduct.

**2026** - [Have LLM-associated terms increased in article full texts in all fields?](https://arxiv.org/abs/2604.07565) - Thelwall, M., and Kousha, K.

- Tracks 80 LLM-associated terms across ~1.25 million full texts from 2021 to 2025, finding prevalence rises through 2024 and then diverges by field, with social sciences and engineering ahead of the life sciences.

**2026** - [Trust-Aware Citation Cartel Ranking in Scholarly Knowledge Graphs](https://arxiv.org/abs/2607.06528) - Gupta, P., Udandarao, V., and Bandi, S.S.S.

- Combines graph topology with LLM-labelled citation-intent analysis over 4.87 million citations, surfacing a top-ranked community of 1,079 papers with 254 times the expected internal citation density.

**2026** - [Designing a Computational Framework for Identifying Suspicious Citation Groups in Heterogeneous Academic Networks: A Graph Learning Approach](https://doi.org/10.1007/s10796-026-10770-y) - Liu, J., Cheng, X., Wei, S., and Wang, G.

- Argues that citation-cartel detection over-relies on local signals and proposes a graph-learning framework fusing local and global structure across heterogeneous journal and paper networks.

**2026** - [From concept to measurement: operationalizing and normalizing Integrity Risk Indicators by SCImago (IRIS)](https://doi.org/10.1186/s41073-026-00233-y) - Sánchez-Jiménez, R., Guerrero-Bote, V.P., Halevi, G., et al.

- Operationalises integrity risk indicators from bibliographic metadata — authorship and affiliation patterns, citation dynamics and venue credibility — normalised for cross-institution comparison.

**2026** - [AI text detection in dentistry: a comparative analysis across generative models](https://doi.org/10.1186/s41073-026-00228-9) - Villa, J., Garcovich, D., Lombardo, L., et al.

- Benchmarks six commercial AI detectors on 120 full-length manuscripts from three generative models plus human authors, one of few head-to-head evaluations on full papers rather than student essays.

**2026** - [Hallucination Detector: A hybrid LLM and Semantic Scholar tool calling for detecting hallucination in scientific literature](https://arxiv.org/abs/2607.09774) - Neralla, H., Lee, J., Romero, A.H., and Choudhary, K.

- An open-source tool combining LLM-based bibliographic field extraction with Semantic Scholar retrieval, scoring metadata agreement to assign confidence bands from trustworthy to likely fabricated.

**2026** - [LLM-Generated or Human-Written? Comparing Review and Non-Review Papers on ArXiv](https://arxiv.org/abs/2601.17036) - Elazar, Y., and Antoniak, M.

- Tests the premise behind restricting unpublished review papers on a preprint server, finding AI-generated content is proportionally more common in reviews but far more numerous in absolute terms among non-reviews.

**2026** - [Machine learning based screening of potential paper mill publications in cancer research: methodological and cross sectional study](https://doi.org/10.1136/bmj-2025-087581) - Scancar, B., Byrne, J., Causeur, D., and Barnett, A

- Proposed a BERT-based model to identify Paper Mill papers using their Titles and Abstracts..

**2024** - [Sneaked references: The invisible citation fraud](https://asistdl.onlinelibrary.wiley.com/doi/10.1002/asi.24896) - Besançon, L., Cabanac, G., Labbé, C., et al.

- Documents the manipulation of metadata to inflate citation counts via "invisible" references.


**2024** - [Characterizing the Increase in Artificial Intelligence Content Detection in Oncology Scientific Abstracts From 2021 to 2023](https://ascopubs.org/doi/abs/10.1200/CCI.24.00077) - Pearson, A.T. et al.

- Evaluated text from over 15,000 published abstracts to detect AI-generated content, finding a significant increase in AI usage.

**2024** - [Detection of tortured phrases in scientific literature](https://arxiv.org/abs/2402.03370) - Elkhatib, A. et al.

- Proposes automatic detection methods for "tortured phrases" using language models and embedding similarities to identify papers employing synonym-replacement software.

**2021** - [Tortured phrases: A dubious writing style emerging in science](https://arxiv.org/abs/2107.06751) - Cabanac, G., Labbé, C., & Magazinov, A.

- The seminal paper identifying "tortured phrases" (e.g., "counterfeit consciousness" instead of "artificial intelligence") resulting from spinning software used to mask plagiarism.

### Public Text Integrity Datasets

- [CiteAudit](https://arxiv.org/abs/2602.23452)
  * A human-validated benchmark of real versus fabricated and mis-attributed scientific references, with a four-stage verification pipeline; code and data released.
- [LLM-Generated Citation Integrity Dataset](https://doi.org/10.3390/data11050122)
  * 74,196 BibTeX references generated by nine language models, alongside a screen of 127,063 citations from 3,541 published papers.
- [FabTab](https://arxiv.org/abs/2603.19712)
  * A benchmark of 1,173 AI-generated and 1,215 human-authored empirical papers for detecting fabricated result tables via within-table likelihood mismatch.
- [Is Your Paper Being Reviewed by an LLM?](https://arxiv.org/abs/2502.19614)
  * A benchmark pairing genuine ICLR and NeurIPS reviews with LLM-generated reviews of the same papers, used to evaluate AI-text detectors on review text.
- [Problematic Paper Screener (PPS)](https://www.irit.fr/~Guillaume.Cabanac/problematic-paper-screener)  
  * A platform and dataset leveraging human assessment and automatic detection to flag articles containing "tortured phrases" and other anomalies.

## Gene Integrity

### Gene Integrity Methods

**2026** - [Misidentification of SMMC-7721 undermines its use as a hepatocellular carcinoma model](https://doi.org/10.1007/s00210-026-05868-8) - Weiskirchen, R.

- Shows that SMMC-7721, long used as a hepatocellular carcinoma model, is actually HeLa-derived, undermining conclusions from studies that relied on it for liver-cancer-specific findings.

**2026** - [ICLAC Has Released Version 14 of Its Misidentified Cell Line Register: Updating the Global Watchlist of Misidentified Cell Lines](https://doi.org/10.3390/cells15070576) - Weiskirchen, R.

- Announces version 14 of the ICLAC register — 608 misidentified lines, 560 with no known authentic stock — and recommends routine register checks and STR profiling enforced by journals, funders and institutions.

**2026** - [Cell line authentication: a commercial service provider perspective](https://doi.org/10.3389/fcell.2026.1843943) - Ralston, E., and Haskayne, C.

- Reports real screening rates from an STR authentication service — around 4.7% misidentified and 1.8% contaminated in 2024 — and argues that proprietary, access-restricted STR databases impede contamination investigation.

**2026** - [Genetic Insights into the Economic Toll of Cell Line Misidentification: A Comprehensive Review](https://doi.org/10.3390/medsci14010025) - Weiskirchen, R.

- Reviews authentication methods from STR profiling to genome sequencing, estimating that roughly one in five lines in use is compromised at a cost of some $28 billion a year in US irreproducibility.

**2026** - [Addressing antibody validation failures: a multi-stakeholder Delphi consensus study on actionable solutions](https://doi.org/10.64898/2026.03.04.709541) - Blades, K., Biddle, M., Froud, R., et al.

- A 32-expert Delphi study reaching consensus on 15 actionable items across institutional training, funder requirements, publisher standards and manufacturer accountability for reagent validation.

**2019** - [Semi-automated fact-checking of nucleotide sequence reagents in biomedical research publications: The Seek & Blastn tool](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0213266) - Labbé C., Grima, N., Gautier T., Favier B., Byrne J.A.

- [Tool Link](https://scigendetection.imag.fr/TPD52/Vb/)

### Gene Integrity Datasets

- [ICLAC Register of Misidentified Cell Lines](https://iclac.org/databases/cross-contaminations/)
  * The canonical watchlist of cross-contaminated and misidentified cell lines; version 14 (February 2026) lists 608 lines, with HeLa implicated in 145 entries.
- [Cellosaurus](https://www.cellosaurus.org/)
  * A cell line knowledge resource covering more than 168,000 lines, with a dedicated filter for problematic entries and a queryable API.
- [CLASTR](https://www.cellosaurus.org/str-search/)
  * The Cellosaurus STR similarity search tool, which matches submitted STR profiles against human, mouse and dog reference profiles to turn a raw readout into a misidentification finding.
- [DSMZ Online STR Analysis](https://www.dsmz.de/services/human-and-animal-cell-lines/online-str-analysis)
  * A bank-independent STR reference database of over 2,500 human cell line profiles, merging the ATCC, JCRB and RIKEN datasets; login required.
- [HGNC (genenames.org)](https://www.genenames.org/)
  * The authoritative set of over 44,400 approved human gene symbols, with a Multi-Symbol Checker that validates submitted terms against approved, previous, withdrawn and alias symbols.

## Statistics and Science of Science

Papers discussing attributes of science, evolution, publication trends, and funding.

**2026** - [Understanding prolonged retraction lag among retracted biomedical papers: an explainable machine-learning analysis](https://doi.org/10.1007/s11192-026-05808-6) - Peng, Z. et al.

- An explainable machine-learning analysis of 13,685 retracted biomedical papers finds that prolonged retraction delays stem from compounding factors rather than any single cause, with Hindawi-published papers showing comparatively shorter lags.

**2026** - [Disclosure is not documentation: an open science framework for documenting generative AI use in scholarly research and publication workflows](https://doi.org/10.1186/s41073-026-00245-8) - Cwik, J.C.

- Proposes a tiered "minimal" versus "extended" documentation framework, with open templates for researchers, editors and institutions, for recording generative-AI use in research workflows beyond a simple disclosure statement.

**2026** - [Tracking the retracted paper mill articles: a bibliometric study](https://doi.org/10.1007/s11192-026-05751-6) - Cheng, M.W.T., Yang, X., and Allen, R.M.

- Characterises 10,409 paper-mill-linked retractions through 2024, with a 2023 spike and a keyword drift from biomedical terms toward computational ones between 2011 and 2024.

**2026** - [How Ten Publishers Retract Research](https://arxiv.org/abs/2602.19197) - Oppenlaender, J.

- Compares 46,087 retractions across ten publishers, finding normalised rates spanning two orders of magnitude and identifying one publisher whose record is dominated by a single incident and a non-public archive.

**2026** - [An analysis of the relationship between access models and retractions with peer review issues (2014–2024)](https://doi.org/10.1007/s11192-026-05668-0) - Mañana-Rodríguez, J., Granadino-Goenechea, B., and Bautista-Puig, N.

- Matches 31,910 retracted publications against access model, finding gold open access has the highest retraction rate but only from 2020 onward, with rates comparable across models before then.

**2026** - [Does retraction interrupt knowledge-claims diffusion? Evidence from retracted papers in Nature and Science](https://doi.org/10.1007/s11192-026-05741-8) - Wang, J.J., Wei, S., Yuan, X., and Ye, F.Y.

- Mean annual citations fall by 76% and 82% after retraction but never reach zero, and the citation network survives in a weaker and more unevenly organised form.

**2026** - [The Case of the Mysterious Citations](https://arxiv.org/abs/2602.05867) - Bienz, A., Pearson, C., and Garcia de Gonzalo, S.

- Compares citation accuracy in the 2021 and 2025 proceedings of four computing conferences: no 2021 paper contained an unverifiable citation, while every 2025 proceeding did, affecting 2–6% of papers.

**2026** - [Incidence and evolution of retracted publications according to the sources used: A meta-analysis comparison with RetractBASE](https://doi.org/10.1177/01655515251398723) - Sanchez, C., Ortega, J.L., Delgado-Quiros, L., et al.

- Shows that multi-source harvesting materially improves retraction detection, implying that true retraction incidence is higher than single-source estimates suggest.

**2026** - ['Wasted' research and lost citations: A scientometric assessment of retracted documents in Scopus between 2001 and 2024](https://doi.org/10.1177/01655515251362383) - Lendvai, G.F., and Sasvari, P.

- Across 35,514 retracted Scopus publications, citation impact is extremely unequal and author-level retraction frequency correlates only weakly with citation influence, arguing for retraction-aware bibliometric evaluation.

**2023** - [“Publication Output by Region, Country, or Economy and by Scientific Field"](https://ncses.nsf.gov/pubs/nsb202333/publication-output-by-region-country-or-economy-and-by-scientific-field) - Schneider, B. et al.

- NFS report regarding the output trends over time in publication output across regions, countries, or economies and by fields of science.

### Public Retraction Datasets

- [Retraction Watch Database](https://gitlab.com/crossref/retraction-watch-data)
  * The open record of retractions, corrections, expressions of concern and reinstatements, distributed free by Crossref as a 20-field CSV and updated daily.

## Commercial Tools

> **Disclaimer:** We have not tested these tools and cannot verify their effectiveness or accuracy. Inclusion in this list does not constitute an endorsement.

- [Zintzo Research Integrity (River Valley Technologies)](https://www.stm-publishing.com/river-valley-technologies-launches-zintzo-research-integrity-with-risk-triage-dashboard/)
  - Advertises a Risk Triage Dashboard consolidating over 40 manuscript integrity checks across content, references, metadata, authorship and AI-related risk signals into a single color-coded assessment, with optional integrations with ImageTwin and Clear Skies.
- [ReviewerZero AI](https://www.reviewerzero.ai/)
  - Advertises automated checks across figure integrity, statistical revalidation, reference validation, AI-text detection and author identity verification in a single manuscript screen.
- [Argos (Scitility)](https://www.scitility.com/argos)
  - A research-integrity intelligence platform tracking retractions and their downstream citation effects, with alerts, an API and institutional dashboards.
- [SciScore](https://sciscore.com/)
  - Automated review of a manuscript's methods section for rigour and transparency, including detection of research resources and whether they are identified by RRID, vendor and catalogue number.
- [Morressier Integrity Manager](https://www.morressier.com/company/morressiers-guide-to-research-integrity)
  - Publisher-facing screening that runs inside a submission workflow, covering compliance pre-flight, author identity verification, plagiarism and tortured phrases, citation manipulation and AI-generated text.
- [Paperpal Reference Checker](https://paperpal.com/tools/reference-checker)
  - Scans a reference list before submission for retracted references, hallucinated citations, invalid DOIs, and mismatches between in-text citations and the reference list.
- [RefIntegrity](https://refintegrity.com/)
  - Free and open source. Checks a reference list for retracted citations via OpenAlex and the Retraction Watch database, and is also published as an MCP server.
- [ImageTwin](https://imagetwin.ai/)
  - AI-based software for detecting image duplication and manipulation in scientific publications. Indexes over 100 million images.
- [Proofig](https://www.proofig.com/)
  - Automated image integrity detection for scientific publications, focusing on splicing, cloning, and beautification artifacts.
- [FigCheck](https://www.figcheck.com/)
  - A "self-check" tool for authors to identify accidental duplications before submission.
- [ImaCheck](https://imacheck.com/)
  - Offers automated detection and forensic toolbox services, with a focus on education and best practices.
- [Signals (Sleuth AI)](https://research-signals.com/)
  - An AI assistant that allows editors to query manuscripts for anomalies, coherence, and logic.
- [Clear Skies (Oversight)](https://clear-skies.co.uk/)
  - Provides probability scores for AI generation and network-based checks.
- [Skyline Academic](https://skylineacademic.com/)
  - Uses AI to distinguish between acceptable text recycling and unethical self-plagiarism.

**2022** - [Assessment of ImageTwin, Proofig, FigCheck and Imacheck by STM](https://stm-assoc.org/what-we-do/strategic-areas/research-integrity/image-integrity/resource-center/)

- [Result Sheet](https://stm-assoc.org/document/image-alterations-duplications-consultation-comparison/)


## Organizations

| Type | Organization Name | Region | Description |
|------|-------------------|--------|-------------|
| Governmental | [Office of Research Integrity (ORI)](https://ori.hhs.gov/) | USA | Oversees investigations and manages the "Voluntary Exclusion" list of banned researchers for PHS-funded research. |
| Governmental | [Secretariat on Responsible Conduct of Research (SRCR)](https://srcr-scrr.gc.ca/) | Canada | Manages the Tri-Agency Framework (CIHR, NSERC, SSHRC) and requires institutions to report misconduct summaries. |
| Governmental | [Danish National Committee on Research Misconduct (Nævnet for Videnskabelig Uredelighed)](https://ufm.dk/en/research-and-innovation/councils-and-commissions/The-Danish-Board-on-Research-Misconduct) | Denmark | National body with legal power to overturn university decisions and handle misconduct cases centrally. |
| Governmental | [CNPq - Commission for Integrity in Scientific Activity (CIAC)](https://www.gov.br/cnpq/pt-br/) | Brazil | Federal commission analyzing allegations of misconduct involving CNPq funding and productivity fellows. |
| Governmental | [FAPESP (Scientific Directorate)](https://fapesp.br/boaspraticas/) | Brazil | Investigates misconduct in São Paulo-funded research under the "Code of Good Scientific Practice". |
| Governmental | [UK Research Integrity Office (UKRIO)](https://ukrio.org/) | UK | Independent charity providing expert advice on investigations and support to universities. |
| Governmental| [French Office for Research Integrity (OFIS)](https://www.ofis-france.fr/en/) | France | Guides national strategy and harmonizes definitions of scientific integrity and research ethics. |
| Governmental | [ENRIO (European Network of Research Integrity Offices)](https://www.enrio.eu/) | Europe (EU) | Facilitates cross-border investigations and connects European research integrity offices. |
| NGO | [Center for Scientific Integrity (Retraction Watch)](https://retractionwatch.com/) | USA / Global | Maintains the definitive public record of retractions and an open database for vetting citations. |
| NGO | [PubPeer Foundation](https://pubpeer.com/) | Global | Platform for anonymous post-publication peer review, often used to identify image manipulation. |
| Non-profit organization | [Center for Open Science (COS)](https://www.cos.io/) | USA | Operates the Open Science Framework (OSF) and promotes Registered Reports to improve reproducibility. |
| Charitable Company | [COPE (Committee on Publication Ethics)](https://publicationethics.org/) | Global | Provides guidelines and flowcharts for editors to handle publication ethics and misconduct. |
| Association | [STM Association (Integrity Hub)](https://www.stm-assoc.org/integrity-hub/) | Global | Collaboration of publishers building the "Integrity Hub" to detect duplicate submissions and paper mills. |
| Association | [APRIN (Association for the Promotion of Research Integrity)](https://www.aprin.or.jp/en/) | Japan | Primary body for e-learning and integrity certification in Japan, focusing on life sciences. |



## Conferences and Journals

### Conferences

| Name | Description |
|------|-------------|
| [World Conference on Research Integrity (WCRI)](https://wcri2026.org/) | Premier global policy forum involving all stakeholders in research integrity, including universities, funders, and governments. |
| [European Conference on Ethics and Integrity in Academia (ECEIA/ECAIP)](https://www.eventleaf.com/ECEIA25) | European forum for academic integrity focusing on plagiarism, contract cheating, and student/researcher misconduct. |
| [Society for Scholarly Publishing (SSP) Annual Meeting](https://www.sspnet.org/) | Industry-focused meeting covering systematic manipulation and operationalizing tools like Papermill Alarm. |
| [Int. Congress on Peer Review and Scientific Publication](https://peerreviewcongress.org/) | Major quadrennial event researching the quality and credibility of scientific review and evidence-based improvements. |
| [IEEE Int. Workshop on Information Forensics and Security (WIFS)](https://signalprocessingsociety.org/events/2025-ieee-international-workshop-information-forensics-and-security-wifs) | Primary technical workshop for information forensics, focusing on signal processing to detect manipulation and AI forgery. |
| [CVPR (Computer Vision and Pattern Recognition)](https://cvpr.thecvf.com/) | Top-tier computer vision conference hosting workshops for fraud detection, including visual anomaly detection. |
| [ICCV (International Conference on Computer Vision)](https://iccv.thecvf.com/) | Biennial computer vision event featuring technical tracks on deepfake detection, image manipulation, and synthesis verification. |
| [ECCV (European Conference on Computer Vision)](https://eccv.ecva.net/) | Biennial top-tier vision conference for detecting generative artifacts and image manipulation. |
| [IEEE Int. Conference on Image Processing (ICIP)](https://2025.ieeeicip.org/) | Signal processing conference with sessions on explainable deepfake detection for verifying scientific images. |
| [ACM Workshop on Information Hiding and Multimedia Security (IH&MMSec)](https://www.ihmmsec.org/) | Technical venue for digital watermarking, steganography, and provenance technologies (C2PA). |
| [WACV (Winter Conf. on Applications of Computer Vision)](https://wacv2025.thecvf.com/) | Practical application focus hosting the AI for Multimedia Forensics and Disinformation Detection workshop. |

### Journals

| Name | Description |
|------|-------------|
| [Accountability in Research](https://www.tandfonline.com/journals/gacr20) | Premier venue for empirical studies on research misconduct policies, mentorship, and integrity training. |
| [Research Integrity and Peer Review](https://researchintegrityjournal.biomedcentral.com/) | Open access journal focusing on research reporting quality, peer review transparency, and publication ethics. |
| [Science and Engineering Ethics](https://link.springer.com/journal/11948) | Multidisciplinary journal exploring ethical issues in science and engineering practice, including data integrity. |
| [PLOS ONE](https://journals.plos.org/plosone/) | Multidisciplinary open access journal publishing meta-research and studies on reproducibility and negative results. |
| [Patterns](https://www.cell.com/patterns/home) | Data science journal focusing on data sharing, reusability, and open data infrastructure. |


## Related Awesome Lists

Lists grouped to mirror the sections above. The forensics and detection lists are
general-purpose (natural images, faces, generic text); the techniques they index are
the same ones applied to figures and manuscripts in the scientific literature.

### Image and Media Forensics

- [Image Forgery Detection and Localization Papers](https://github.com/greatzh/Papers) - Papers on splicing, copy-move, inpainting and AIGC tampering detection, the core methods behind figure duplication analysis.
- [Image Forgery Datasets List](https://github.com/greatzh/Image-Forgery-Datasets-List) - Datasets for forgery detection and localization, indexed by manipulation type, format and post-processing.
- [Awesome Deepfakes Detection](https://github.com/Daisy-Zhang/Awesome-Deepfakes-Detection) - Datasets, tools, competitions and papers for detecting manipulated faces in images and video.
- [Awesome AIGC Image and Video Detection](https://github.com/ant-research/Awesome-AIGC-Image-Video-Detection) - Benchmarks, MLLM-based detectors and open-source tools for identifying AI-generated images and video.
- [Awesome GenAI Watermarking](https://github.com/and-mill/Awesome-GenAI-Watermarking) - Watermarking schemes for generative models, plus C2PA and content-provenance resources.

### Text and LLM Integrity

- [Awesome Machine-Generated Text](https://github.com/ICTMCG/Awesome-Machine-Generated-Text) - Continuously updated resources on generative LLMs, their societal analysis, and machine-generated text detection.
- [Papers on LLM-Generated Text Detection](https://github.com/Xianjun-Yang/Awesome_papers_on_LLMs_detection) - Detection of LLM-written text and code: training-based, zero-shot, watermarking, fingerprinting, evasion attacks and datasets.
- [Awesome Hallucination Detection](https://github.com/EdinburghNLP/awesome-hallucination-detection) - Papers on hallucination and factuality detection in LLMs, annotated with metrics, datasets and evaluation setups.

### Open Science, Metascience, and Scholarly Data

- [Awesome Scholarly Data Analysis](https://github.com/napsternxg/awesome-scholarly-data-analysis) - Datasets, papers and tools for bibliometrics, citation analysis and peer review, including OpenAlex and PeerRead.
- [Awesome Reproducible Research](https://github.com/leipzig/awesome-reproducible-research) - Reproducible research case studies, tooling, reporting standards, journals and organizations.
- [Awesome Open Science Software](https://github.com/ASSERT-KTH/awesome-open-science-software) - Open source software for open science, covering software as a research object and open science infrastructure.


## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this list.