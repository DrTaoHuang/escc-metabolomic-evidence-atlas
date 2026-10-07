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
