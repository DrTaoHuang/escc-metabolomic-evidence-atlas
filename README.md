# ESCC Metabolomic Evidence Atlas


An evidence atlas for metabolomic research in esophageal squamous cell carcinoma (ESCC). It supports finding reported observations, tracing the reports and participant sources behind them, and examining scientific interpretation and clinical-use boundaries.

## Evidence coverage

| Unit | Count | Interpretation |
| --- | ---: | --- |
| Included reports | 113 | Publications, including related or companion reports |
| Study units | 95 | Registered study-level entities |
| Source-cohort nodes | 124 | Participant-source entities; this is not a count of verified independent replications |
| Analytic datasets | 165 | Analysis-level datasets or source subsets |
| Molecular observations | 3,846 | Findings separated by identity, matrix, comparison, timepoint and source context |
| Pathway or biological-support records | 614 | Mapping, observational, orthogonal or experimental support, with evidence-layer limits |
| Performance records | 811 | Source-specific results; multiple records can describe one model or subgroup |
| Model/marker identifiers | 692 | Identifiers rather than independent validated clinical tests |
| Accepted molecular-result groups | 3,704 | 19 narrative-synthesis groups, 3,675 evidence-map/direction groups and 10 groups not synthesizable with the available information |
| Eligible quantitative synthesis endpoints | 0 | No pooled effect or overall diagnostic-performance estimate is supplied |

The observation, support and performance subsets are contributed by 109, 111 and 87 reports, respectively. These overlapping contribution counts must not be added together or substituted for the 113 included reports. The resource also provides 1,101 individual quality-domain assessments, 17 scientific topics, four clinical-use topics, 41 research-priority entries, 182 glossary entries and the S1–S20 supplementary-table register.

## Access and use

- **Online atlas:** `https://drtaohuang.github.io/escc-metabolomic-evidence-atlas/`
- **Source repository:** `https://github.com/DrTaoHuang/escc-metabolomic-evidence-atlas`
- **Fixed release and offline downloads:** `https://github.com/DrTaoHuang/escc-metabolomic-evidence-atlas/releases/tag/v1.0.0`

The atlas opens in English, with a Simplified Chinese switch. Both language views use the same evidence records. Interface translation does not change scientific values, participant relationships, original feature names, citations or source uncertainty. Source wording can remain in its original language where faithful quotation or identification requires it.

### Online

1. Open the verified atlas URL and choose English or Simplified Chinese.
2. Search for a metabolite, pathway, report, author or clinical use, or browse the evidence sections.
3. Combine available report, sample-matrix, direction and clinical-use filters.
4. Open a record to read its full fields, citation, source locator, identity qualification and evidence limits.
5. Export the matching records or download the supplementary tables. A record export covers all matches, rather than only the displayed page.

### Offline

1. Download the complete ZIP from the fixed release.
2. Extract the whole archive and retain its folder structure.
3. Open `index.html` in a current Chrome, Edge or Firefox browser.
4. Use the language switch, search, record details, topics, local exports and bundled supplementary tables without an internet connection.

Article DOI links and release-download links require internet access. The offline archive need not contain another copy of its own ZIP. The online and offline editions should identify the same fixed release and expose the same scientific records.

## Read the evidence in context

Reports, studies, source cohorts, analytic datasets, observations and models are different counting units. Multiple publications, repeated measurements, internal training/test splits and subgroup performance rows do not establish additional independent participants or replications.

The accepted groups preserve qualified source groupings. Name similarity, pathway co-occurrence and common direction are insufficient to merge uncertain molecular identities or claim independent human replication. Human observations, animal/cell experiments, spatial regions and cross-omic support retain their own evidence levels.

Clinical-use tags are `prevention`, `diagnosis`, `treatment` and `prognosis`. A tag identifies the review's use context; it does not imply clinical deployment or demonstrated benefit. AUCs from different tasks and populations are not an overall ranking. Quality assessments remain framework- and domain-specific and are not a composite quality score.

Missing and uncertain values must be read with their field-specific notes:

- **NR:** not reported in the specified source context, or not established from the available cited evidence in broader S9/S16 fields. It does not prove that a procedure was never performed or that an effect was absent.
- **UNC:** unclear, contradictory or insufficiently resolved; information may be present.
- **NA:** not applicable to the stated field or comparison.
- **NE:** context-dependent: confirmation not established, a quantity not estimable, or a specified result not extractable. It does not mean zero or non-detection.

Explicit negative findings and conflicting directions are retained. An empty relation or tag array is not a negative result. Topic-specific facts are carried in `details`; omitted generic summary fields must not be replaced with invented NR values.

## Files and citation

`evidence.json` contains the reader-facing structured records. `data.js` supplies the same records for offline browser use. Supplementary Word documents describe methods, record-level evidence and scientific boundaries. See [DATA_DICTIONARY.md](DATA_DICTIONARY.md) for the field contract.

Cite the fixed resource release as described in [CITATION.md](CITATION.md), and cite the original reports when using a particular finding. The atlas is an index and evidence synthesis, not a substitute for the original source report. The resource's neutral display name is not a claim about the final title or authorship of the associated review. No resource DOI or associated paper DOI is provided.

## Rights and included materials

See [NOTICE](NOTICE) for third-party credits and rights boundaries. Lucide icons retain their upstream license file. Its permissions apply to those icons and do not license the curated evidence data or other project materials.

No additional project-wide open reuse license is granted for project-authored code, curated data or text. Public access alone does not transfer third-party rights. Original article PDFs, participant-level datasets, private correspondence, internal audits, extraction records and internal identifier crosswalks are not part of the public distribution. Interface decoration is symbolic artwork, not a research result or anatomical evidence.

## Reproducibility and limitations

Use the fixed release version when describing the resource. Preserve original names, units, matrices, timepoints, citations and uncertainty when exporting or reusing records. No participant-level model training data or repeated patient-level analysis is provided. The atlas supports research evidence appraisal; it does not establish patient benefit from using a test.


## Website source and release bundle

The website HTML, CSS and JavaScript source and the original evidence payload are included in the complete offline release archive. GitHub Pages deploys the same reviewed archive. The public repository contains the deployment workflow and release documentation; the archive keeps the website, scientific records and supplementary documents together.
