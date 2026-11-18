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
