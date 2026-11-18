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
