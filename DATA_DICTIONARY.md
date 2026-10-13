# Reader data dictionary

This dictionary describes the accepted reader data used by the ESCC Metabolomic Evidence Atlas. It does not describe internal extraction or audit payloads. Scientific values and stored source wording remain unchanged. The English and Simplified Chinese views may apply verified display translations while retaining the original dataset, names and citation locators.

## Top-level structure

| Key | Type | Contents |
| --- | --- | --- |
| `counts` | object | Counts for distinct entity and record units; definitions below |
| `reports` | array, 113 | Registered report citations and source-entity relationships |
| `observations` | array, 3,846 | Source-specific molecular findings |
| `supports` | array, 614 | Pathway and biological-support findings |
| `performances` | array, 811 | Performance records linked to 692 model/marker identifiers |
| `groups` | array, 3,704 | Accepted molecular-result groups with identity qualifications retained |
| `topics` | array, 62 | 17 scientific, four clinical and 41 priority entries |
| `glossary` | array, 182 | Abbreviations, units, evidence states and reading guidance |
| `tables` | array, 20 | S1–S20 identifiers and titles |

The `studies`, `cohorts` and `datasets` counts refer to distinct registered IDs referenced by reports. There are no separate public arrays named `studies`, `cohorts` or `datasets` in this contract.

## Counts and identity layers

`counts` includes `reports: 113`, `studies: 95`, `cohorts: 124`, `datasets: 165`, `observations: 3846`, `supports: 614`, `performances: 811`, `models: 692`, `groups: 3704`, `qualityAssessments: 1101` and `quantitativeEndpoints: 0`.

The group partition is `groupNarrative: 19`, `groupMap: 3675` and `groupUnsynthesizable: 10`. These values sum to 3,704 and are grouping/eligibility categories, not independent replication counts.

Neutral IDs distinguish report (`R###`), study (`S###`), source cohort (`C###`) and analytic dataset (`D###`) entities. They are identifiers rather than rankings or clinical evidence grades. `tableIds` uses supplementary-table identifiers such as `S9` or `S17`; this field belongs to a different namespace from the three-digit study IDs. Source cohort nodes do not automatically establish participant independence.

## Report fields

| Field | Type | Meaning |
| --- | --- | --- |
| `id` | string | Registered neutral report ID |
| `title` | string | Original report title |
| `citation` | string | Reader-facing bibliographic citation |
| `doi` | string | Report DOI where identified; an unavailable value is not a resource DOI |
| `year` | number or string | Publication year retained in the source record |
| `studyIds`, `cohortIds`, `datasetIds` | arrays of strings | Registered entity links; consult source notes for independence and overlap |
| `details` | array of `{label, value}` | Human-readable source, dataset and relationship information |
| `quality` | array of objects | Separate assessments with `framework`, `domain`, `judgement`, `evidence` and `source`; no total score |

## Fields shared by the evidence-record arrays

The fields below describe `observations`, `supports`, `performances` and `groups`. A field's meaning depends on the record unit; the same key must not be given an inappropriate generic label.

| Field | Type | Meaning |
| --- | --- | --- |
| `id` | string | Stable reader record ID within its array |
| `title` | string | Reader name of the molecular finding, support, model or group |
| `reportIds` | array of strings | Explicit report links; one record may cite more than one report |
| `studyIds`, `cohortIds`, `datasetIds` | arrays of strings | Explicit registered relationships; missing links are not evidence of absence or independence |
| `matrix` | string | Sample or specimen matrix, with source qualification |
| `comparison` | string | Reported comparison, outcome or review grouping context |
| `timepoint` | string | Sampling or decision time and relevant source wording |
| `direction` | string | Observation/support/group direction; in performance records, the original evaluation-role or subgroup wording |
| `identity` | string | Observation/group identity qualification; support evidence-object or layer description; performance input-feature description |
| `use` | array of strings | Exact controlled values: `prevention`, `diagnosis`, `treatment`, `prognosis`; empty means unassigned |
| `validation` | string | Human-readable support/evaluation/synthesis relationship, with scientific limits |
| `source` | string | Citation and/or original report locator |
| `details` | array of `{label, value}` | Full approved reader fields, including original names, effect/precision, notes and limits where relevant |
| `tableIds` | array of strings | Relevant supplementary tables |

For observations, `groupId` links to the accepted `groups` entry. For groups, `observationIds` lists member observation IDs, and `synthesisClass` is `narrative`, `map` or `unsynthesizable`. Every observation belongs to exactly one accepted group. Group membership does not establish identical molecular identity or independent replication beyond the documented qualifications.

For performance records, `modelId` identifies the model/marker and `validationRole` contains the audited evaluation role. Multiple performances can share one `modelId`. The performance `direction` field can include source subgroup labels such as an ESCC or staging subgroup; it must not be presented as a verified validation-role classification. Read `validationRole`, `validation` and source details together. A role labelled external does not itself establish independent participants or a locked panel, algorithm or threshold.

For supports, the field labelled **Does not support** (rendered as **尚不能支持的主张** in the accepted reader details) is explicitly a negated boundary. Its value must not be displayed as a positively supported claim. Human associations, spatial evidence, animal/cell support and background literature context retain separate interpretations.

## Topics and nested records

Topics contain `id`, `title`, `category`, `description`, `reportIds`, `use`, `source`, `details`, `tableIds` and `records`, with registered entity arrays where present. `category` is `science`, `clinical` or `priorities`.

Nested `records` contain an `id`, `title`, `reportIds`, `source`, `details` and the applicable use/table links. The clinical topic arrays contain 210 prevention, 787 diagnosis, 413 treatment and 25 prognosis rows. Source citations inherited from their approved parent sections remain visible in each relevant row. Three treatment entries describe review-level scope/rules and legitimately have no single-report link.

Topic-specific scientific values are stored in `details` using the native approved table columns. Unprojected generic fields such as `matrix`, `timepoint` or `identity` are omitted instead of being filled with artificial NR values. A source-derived scientific-topic `validation` field can be present. Absence of a generic key is not a statement that the original study failed to report that item.

## Glossary and supplementary-table register

Glossary entries contain `id`, `term`, `description`, `category`, `details` and `tableIds`. Categories A–D follow the glossary's abbreviation, unit, evidence-state and reading-guidance sections. Table entries contain `id` and `title`; they reference S1–S20 rather than creating additional study entities.

## Uncertainty, negatives and precision

| Token or state | Interpretation |
| --- | --- |
| `NR` in source-reporting fields | Not reported in the specified available article, supplement or source context; not proof of non-performance or no effect |
| `NR` in S9/S16 | Not established from the available cited evidence for the relevant field; not a universal assertion about all materials |
| `UNC` | Unclear, ambiguous, conflicting or insufficiently resolved |
| `NA` | Not applicable to the specified field, role or comparison |
| `NE` in identification/confirmation fields | Confirmation or specified evidence not established; not non-detection |
| `NE` in numerical S13 fields | Not estimable from the available quantities; not zero |
| `NE` in S14/S15 | The specified usable result is not extractable; not an assertion that the study did not measure the item |
| Empty array | No assigned tag or public link in that field; not a negative finding |
| Absent topic summary key | No generic summary projection was provided; consult the full `details` |

Explicit no-difference findings, mixed/conflicting directions, reported precision and identity limitations are part of the evidence and must not be removed during export or translation. Numerical values with units, logarithmic scales, exponents, minus signs or inequality symbols must be retained exactly. The glossary's field-specific meaning takes precedence over an automatic global replacement of a short token.


## Integrated graph layer

The integrated view adds a separate relationship layer; it does not replace or renumber the reader evidence arrays above. Its files are:

- `atlas-data/graph.json`: the graph object.
- `atlas-data/graph-data.js`: the browser form used for offline access.
- `atlas-data/theme-guide.json` and `atlas-data/theme-guide.js`: theme-level orientation for the represented evidence; this guide does not create additional scientific relationships.
- `atlas-data/nodes.csv` and `atlas-data/edges.csv`: tabular forms of the node and relationship records.
- `atlas-source/reviewed_relations.json`: public, source-qualified relation input.
- `atlas-source/RULES.md` and `atlas-source/DATA_DICTIONARY.md`: the precise relation admission and graph-field contract.
- `atlas-source/build_graph.py` and `atlas-source/README.md`: reconstruction from the public evidence and relation input.
- `atlas.js`, `atlas.css` and the accompanying PNG outputs: interface/rendering source and graph representations.

The graph object has the following top-level fields:

| Field | Meaning |
| --- | --- |
| `schemaVersion` | Graph schema identifier; distinct from the software release version |
| `nodes` | Typed graph entities, with identifiers of the form `kind:publicId` |
| `edges` | Typed relationships between the declared entities |
| `counts` | Counts for the graph layer only; not additional reports, participants, compounds or independent validations |
| `coverage` | The represented scope and its counting units |
| `rules` | Relationship definitions and scientific interpretation restrictions |

Each relationship is interpreted through its declared type, endpoint context and `sourceRefs`. A source reference has `tableId`, `recordId` and `locator`. It points to the supporting reader table/record and source position, not a private extraction path. A `topicRow` can inherit the reviewed parent topic context; this is not an unrestricted join to every molecule, model or source in the parent report.

Use the enclosed graph field dictionary for the actual entity and relationship enumerations. Topic membership, input membership, source provenance, human association and experimental support must not be treated as interchangeable links. Source uncertainty, molecular resolution, sample matrix, comparison and timepoint remain attached to the interpretation. A model's validation evidence does not independently validate each input feature or a pathway.

Coverage and current filters define what appears in the graph. Absence from the graph or absence of a line is not evidence of biological absence, a null result, failure of validation or lack of literature. Counts in `counts` and `coverage` use their stated graph units and cannot be substituted for the full-resource denominators. Repeated representation of one model or source does not add independent evidence.

The accepted observation, support, performance, result-group and model registries remain in the graph. Scientific-theme membership is representative rather than exhaustive: 17 themes have 102 observation, 92 support and 32 performance links selected with source-specific context. The 307 original-feature bindings belong only to R008. Forty-one programme links involve 33 specific S19 programmes; eight general gates remain unassigned to a particular theme or use. Model/performance clinical-use values retain the accepted S9 classification, including an empty value for exploratory or unassigned use. An explicit clinical-table observation link can supply a clinical reading context without reclassifying a connected model or transferring validation.

No composite quality score, pathway score, maturity total or cross-study AUC ranking is encoded. Parallel evidence dimensions and declared relationships support source-aware comparison; they do not establish causal mechanisms, test-guided patient benefit or clinical deployment.
