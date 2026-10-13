# Relationship rules

This graph links typed entities and records from the accepted evidence atlas. Connections describe the relation stated below. They do not establish causal effects, complete molecular identification, participant independence or clinical utility beyond the original record's qualifications.

| Rule | Relation | Interpretation |
| --- | --- | --- |
| REL01 | observation_group | An observation is a member of its accepted result group. Group membership is not proof of identical chemical identity or independent replication. |
| REL02 | performance_model | A performance record concerns a registered model/marker. Repeated results, subgroups and companion reports do not create additional independent tests. |
| REL03 | feature_observation | An original source feature corresponds to an observation by an exact, reviewed feature key within the same source. |
| REL04 | feature_model_input | The original source feature is a model input according to its explicitly keyed performance record. The relation does not establish structural identification or independent validation. |
| REL05 | topic_cites_report | The topic explicitly cites the report. The relation does not assign every finding in that report to the topic. |
| REL06 | clinical_row_observation / performance / model | A clinical supplementary-table row refers to the explicitly keyed record or model. The row is not a new participant, study or performance record. |
| REL07 | record_report / study / cohort_context / dataset_context | The record retains its explicit report, study and source-context references. A context link is different from a judgment of source independence or synthesis eligibility. |
| REL08 | source_study / dataset_source / dataset_report | A registered source or dataset link is stated by an explicit ledger row. Multiple report-level arrays are never crossed to generate pairs. |
| REL09 | support_pathway_mapping / support_compound_mapping | A support record preserves a reported mapping to a pathway or compound identifier. It is not a new support-to-observation match, measurement confirmation or proof of mechanism. |
| REL10 | topic_observation / support / performance / group / priority | A reviewed, selected record is an example or research programme for that exact topic. Its original context, role and limitations remain attached. Selection is not an exhaustive result census or a new evidence grade. |
| REL11 | topic_row | A reader table row belongs to its clinical-use topic. Its counting unit remains the supplementary-table row, including continuation rows. |

## Counting and interpretation

- Reports, study units, source-cohort nodes, analytic datasets, observations, support records, performance records, model identifiers and table rows are different units. Node and edge totals must not be interpreted as patient totals or independent validations.
- The 3,704 groups retain their identity qualifications and synthesis categories. They do not represent 3,704 chemically confirmed molecules. Their existing partition is 19 narrative-synthesis groups, 3,675 evidence-map/direction groups and 10 groups not synthesizable with the available information; there are 0 eligible quantitative synthesis endpoints.
- The 307 original-feature links belong to one registered report/source context, R008. They trace a reported feature through its observation and single-feature model input. They are not 307 independent cohorts or confirmations of chemical structure.
- A model can have several performance records, roles and report contexts. The graph does not assign the strongest role to every result for that model. Evaluation and validation remain properties of the specific performance record.
- Animal, cell, organoid, ex vivo, human and mixed support retain the evidence layer of the original record. A source-context link does not turn experimental support into human replication.
- Reported KEGG member occurrences are retained, including repeated annotations to the same code. A KEGG compound node identifies the reported external code, not a confirmed measured molecular entity. Names or same-report co-occurrence are not used to create support-to-OBS edges.
- Negative, conflicting, NR, UNC and NE information remains in the original reader record and in the relevant graph context. A missing relation is not a negative result. A visible relation is not an evidence score.

Every edge has a stable neutral endpoint-based identifier, a rule and at least one specific supplementary-table/reader-record locator. The original records and tables remain the authority for the scientific result and its full precision and limitations.

