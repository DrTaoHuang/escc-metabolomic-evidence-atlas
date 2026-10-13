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
- **Fixed release and offline downloads:** `https://github.com/DrTaoHuang/escc-metabolomic-evidence-atlas/releases/tag/v1.1.0`
- **Earlier fixed edition:** [v1.0.0](https://github.com/DrTaoHuang/escc-metabolomic-evidence-atlas/releases/tag/v1.0.0)

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

## Integrated evidence view

The integrated view provides a theme-first entry to linked molecular observations, reported features, model or marker records, clinical-use contexts and source evidence. Expand a theme or selected entity to read its context and follow the original record. The complete record lists remain available through evidence search.

Read a line by its declared relationship type, as defined in [the graph rules](https://drtaohuang.github.io/escc-metabolomic-evidence-atlas/atlas-source/RULES.md). Review-topic membership organizes a narrative context; model-input membership identifies a feature included in a particular reported test. A human association, experimental support and a source/provenance link have different meanings. A line is not automatically a causal relation, a molecular-identity confirmation or an independent validation. The relationship types available in a particular view follow the supplied relation table.

The graph retains the accepted observation, support, performance, result-group and model registries and their recorded source links. The connections from the 17 scientific themes to particular records are selected representative examples, not an exhaustive supporting-record census: they include 102 observation links, 92 biological-support links and 32 performance links. Original-feature bindings cover 307 source features from R008 only. The 41 research-programme links involve 33 specific S19 programmes; the eight general research gates remain available without a forced theme or clinical-use assignment. These relation counts are not counts of independent studies or validated tests. An absent displayed line does not establish absent evidence or a negative finding; consult the complete record and source context.

Serum and plasma, different comparators and sampling times, named compounds and unresolved features, and human versus nonhuman support retain their distinctions. Related reports do not add independent participants. A topic row's inherited parent context is identified as such and does not grant more specific molecular, model or source conclusions.

Identity, independent human support, biological anchoring, assay/model implementation, target-population evaluation, incremental value and clinical utility are parallel evidence dimensions. They do not form a total score or a universal progression ladder. Model-level validation cannot be transferred to every input molecule or a related pathway. Node size, colour, line count and AUC are not rankings of evidence strength or clinical readiness. Null, opposite, conflicting and scientifically uncertain findings retain their source qualifications.

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

The fixed v1.1.0 release provides:

- `ESCC_Evidence_Atlas_v1.1.0_Offline.zip`: the complete website, original reader evidence, supplementary Word documents and integrated view.
- `ESCC_Integrated_Atlas_v1.1.0_Source.zip`: the public evidence input, typed graph data and CSV files, reviewed relation input, relationship rules, field dictionary, reproduction script, graph interface code and generated PNG outputs.
- `SHA256SUMS_v1.1.0.txt`: SHA-256 checksums for both archives.

Both archives are bound to the same fixed release and publication commit. The online site is deployed from the corresponding complete website archive. The earlier v1.0.0 edition remains available and does not acquire the new integrated view retroactively.

For reconstruction, see [the reconstruction guide](https://drtaohuang.github.io/escc-metabolomic-evidence-atlas/atlas-source/README.md). Both complete archives also include these local documents at atlas-source/README.md and atlas-source/RULES.md, so their contents are available offline. The reproduction input is the public `evidence.json` plus the included reviewed relation input; it does not require private extraction files or local project paths. The graph data and its generated outputs retain their declared evidence boundaries.
