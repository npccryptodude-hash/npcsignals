# data model v0.1

all identifiers are stable strings; all dates use iso 8601 with date precision recorded. null means unknown, not zero.

## tables

- sources: source_id, publisher, title, publication_date, url, document_version, access_date, archival_locator, page_or_section, source_type, language, license
- incidents: incident_id, event_date, country_iso2, locality_general, status [completed|failed|foiled|disputed], ideology_source_label, ideology_normalized, deaths, injuries, source_id, evidence_status, notes
- actors: actor_id, actor_type [person|organisation|cell], public_name_or_pseudonym, description, evidence_status, source_id, privacy_review
- relationships: relation_id, subject_id, predicate, object_id, valid_from, valid_to, source_id, evidence_status, qualification, contested
- judicial_records: record_id, jurisdiction, proceeding_type, case_reference, decision_date, outcome, linked_incident_ids, source_id
- financial_records: finance_id, high_level_mechanism, jurisdiction, period, linked_actor_ids, public_case_reference, source_id, evidence_status; no operational transfer instructions
- statistics: statistic_id, reporting_year, geography_definition, source_edition, category, measure, value, denominator, inclusion_notes, completeness
- review_log: record_id, reviewer, review_date, change_summary, reason, supporting_sources

## integrity constraints

each factual record requires at least one source_id. never collapse multiple national reports into one eu/eea total before checking overlaps and definitions. record original terminology and translated/normalised terminology separately. source-supported edges only; no inferred relationship from co-location or shared ideology.

## initial data state

no incident-level dataset populated. source register provides the first ingestion queue. the 2025 europol eu totals are not imported as eu/eea totals.

## Historical event and reporting dates

The occurrence year belongs to the physical event. A disruption date may anchor a foiled entry, with the date basis recorded. Investigation and judicial decision years belong to dated procedural records and can differ from one another and from the occurrence year.

For each official statistic, preserve the reporting reference year, edition identifier and publication year. Record actual submission year separately when evidenced. A retrospective entry can have an occurrence year earlier than the reporting reference year, and revised editions can share the same publication year. Record the edition version with the source.

The [cross-year cohort register](2022/cross_year_events.csv) links these dimensions and preserves an unresolved event list as an empty field. Cohort IDs identify aggregate rows only. Join to stable physical event IDs only when both the incident and allocation can be supported. Track inclusion evidence and duplicate risk separately. Original edition totals stay fixed. Any occurrence-date reassignment belongs in a labelled analytical series.

The [retrospective reporting provenance ledger](2021/provenance.csv) adds an adjustment ID, original and later editions, count, entry action and identity status. The later reference year describes the host edition's main reporting period; it need not be the year to which a historical comparison inside it refers. Distinguish omitted entries later shown in a same-year comparison from older entries included in another year's cohort and entries removed after reclassification. A cohort adjustment can be verified while its individual identities remain unknown.

The [2020 reclassification supplement](2020/provenance_evidence.csv) links a candidate incident to an existing provenance adjustment ID. Candidate confidence refers to the revision linkage and is independent of confidence in the original publication allocation. Unknown outcomes can remain in a country/category aggregate without being allocated to completed, failed or foiled.

For pre-withdrawal reference years, record membership at occurrence, membership at publication and actual statistical contribution separately. A fixed-geography subset can be derived using identified jurisdiction rows and matching scopes, with the original edition totals retained. The [2019 geography audit](2019/GEOGRAPHY_AUDIT.md) supplies the first example and preserves additional Northern Ireland arrests that were excluded from the original UK row.

The [2018 geography audit](2018/GEOGRAPHY_AUDIT.md) records both independent UK row subtractions and later official corroboration. Preserve original numeric cell anomalies separately from reconciled rows. Later legal classification can be recorded against an identified incident while the original statistical allocation remains in force unless a numeric revision is evidenced.

The [2017 allocation](2017/BASELINE.md) distinguishes an aggregate outcome margin from outcomes verified at joint country/category level. Use unresolved cells where the join is unavailable and retain source margins separately. The [classification record](2017/provenance_evidence.csv) allows a later court outcome to be recorded without converting a candidate into a confirmed statistical match or assuming a numerical correction.

The [2016 baseline](2016/BASELINE.md) separates edition-level victim counts, case-level figures and later national measurements. A shared trial can link several incident records without duplicating the proceeding; named candidates may be alternatives for a single slot. Record the number of candidate slots separately from the number of alternative IDs.

The [consolidated historical CSV](data/eu_statistical_reconciliation_2015_2025.csv) records original reporting scope, included UK contributions, later official revisions, alternate observations of unresolved status, fixed geography, sensitivity delta and original-scope slot confidence as separate fields. Blank revision values mean no verified numeric revision. A zero UK subtraction means the UK was already outside that aggregate. The annual source locator resolves relative to this research directory.
