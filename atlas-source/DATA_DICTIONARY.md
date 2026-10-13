# Atlas graph data dictionary

The graph is an additional relation layer. The original `evidence.json`, offline reader data, citations and supplementary Word documents retain their scientific values.

## Files

| File | Contents |
| --- | --- |
| graph.json | Complete typed graph object |
| graph-data.js | The same object assigned to `window.ESCC_GRAPH` for offline browser use |
| nodes.csv | One row per typed public node; arrays and context objects are JSON text |
| edges.csv | One row per documented typed relation; context and source references are JSON text |
| RULES.md | Meaning and scientific limits of each relation type |

The JSON object contains `schemaVersion`, `nodes`, `edges`, `counts`, `coverage` and `rules`. Coverage is reported by node type, relation type and counting unit. It is not a measure of evidence strength or completeness of scientific validation.

## Nodes

Each node has `id`, `kind`, `label`, `labelEn`, `labelZh`, `recordKind`, `recordId`, `context`, `reportIds`, `studyIds`, `cohortIds` and `datasetIds`. The globally unique ID has the form `kind:publicId`.

| Kind | Unit |
| --- | --- |
| report | Included publication or companion report |
| study | Registered study unit |
| cohort | Registered source-cohort node, with independence assessed separately |
| dataset | Registered analytic dataset or source subset |
| observation | Source-specific molecular finding |
| group | Accepted molecular-result group with identity qualifications retained |
| performance | Source-specific performance result |
| model | Registered model/marker identifier; one fixed deployable test is not assumed |
| support | Pathway, observational, orthogonal or experimental support record |
| topic | One scientific, clinical-use or research-priority reader entry |
| topicRow | One clinical supplementary-table reader row |
| feature | Original source feature, identified within its own source context |
| pathway | External pathway identifier used in a reported source mapping |
| compound | External compound code used in a reported mapping; not confirmation of the measured feature's structure |

Original molecule names and citations are retained. `labelEn` uses only an approved display translation where available; `labelZh` retains the source wording. An original name can therefore be identical in both language labels.

`recordKind` and `recordId` point to the existing reader record where applicable. A `topicRow` also has `topicId` and `topicRowId`; its `recordId` points to its parent clinical-use topic. A model has `modelId` and lists its specific `performanceIds` in context. Nodes representing a registry or external identifier can have no individual reader record; follow their typed edges and specific source references.

For observations and groups, `identityQualification` preserves the source qualification. For supports, `evidenceLayer` preserves the original evidence-object/layer description. For performances, `inputFeatures`, `validationRole` and `originalRecordStatus` have different meanings: an original role/status can contain a subgroup label and must not be substituted for the audited evaluation role. Optional context fields are omitted when not projected; they are not assigned artificial NR values.

`reportedUse` on observations, groups or source features preserves the reader's broader source-use annotation. It is not transferred to a model as an audited clinical purpose. Model/performance `use` comes from the accepted S9 classification; an empty array remains unassigned or exploratory. Clinical-topic/row use identifies the supplementary-table domain, not the deployment status of every linked model.

## Edges

| Field | Meaning |
| --- | --- |
| id | Stable neutral identifier based on relation type and public endpoints; reported member occurrences are distinguished |
| source, target | Existing node IDs in the same graph |
| type | Controlled relation predicate; see RULES.md |
| context | Stated record/row/feature/mapping context and scientific limits, where applicable |
| sourceRefs | At least one `{tableId, recordId, locator}` identifying a specific accepted reader entry or table row |
| rule | Stable neutral rule identifier, REL01–REL11 |

`relationStatus: explicit` means that the edge was supplied by an explicit reader link or a reviewed source key/membership selection. It does not certify chemical identity, participant non-overlap, model locking or clinical benefit. Eligibility and evidence limitations must be read separately.

For reported compound mappings, `membershipOccurrence` retains the member's source occurrence and `reportedMemberLabel` retains its original annotation. Repeated KEGG codes are not silently collapsed. For theme membership, `limits` and any stated source-independence qualifier are part of the relation context.

Blank CSV scalar cells denote a missing or inapplicable projection key, not a new scientific missing-value judgment. Real NR/UNC/NA/NE tokens remain in context or the linked original record. The JSON graph is the primary typed representation.

## Boundaries

The graph does not construct a chemical-identity registry by name matching, connect all results from the same report to one another, cross report-level source arrays, calculate a total quality score, rank models by AUC, infer causal pathways or transfer validation from one record to another. The 1,101 quality-domain assessments remain available through their original report records and retain framework-specific meanings.

The accompanying public generator reads the public reader dataset and reviewed relation input only. Internal source IDs, private crosswalks, source-review files and local project paths are excluded from the public rebuild dependency.

