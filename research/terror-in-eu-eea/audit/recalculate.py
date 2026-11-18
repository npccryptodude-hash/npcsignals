"""Run with Python 3. Reads archived data, emits independent row totals as CSV."""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTCOMES = ('completed', 'failed', 'foiled', 'unresolved_outcome')
CLASSES = ('adequate', 'candidate', 'unidentified')
META = {'country_iso2', 'geography_component', 'total', 'printed_row_total',
        'source_id', 'source_ids', 'printed_page'}
COUNTRIES = set('AT BE BG HR CY CZ DK EE FI FR DE GR HU IE IT LV LT LU MT NL PL PT RO SK SI ES SE GB NO IS LI'.split())
issues = []


def read(path):
    with (ROOT / path).open(newline='') as handle:
        return list(csv.DictReader(handle))


def check(condition, detail):
    if not condition:
        issues.append(detail)


def counts(rows, keys, value='total'):
    result = Counter()
    for row in rows:
        result[tuple(row[key] for key in keys)] += int(row[value])
    return +result


def cols(rows, columns):
    return +Counter({key: sum(int(row[key] or 0) for row in rows) for key in columns})


def margins(rows, reserved):
    result = Counter()
    for row in rows:
        for key in row.keys() - reserved:
            result[row['country_iso2'], key] += int(row[key] or 0)
    return +result


def ids(rows, key):
    values = [row[key] for row in rows]
    return len(values) == len(set(values))


def phase6_cells():
    # Historical document remains the source of allocation counts.
    lines = (ROOT / '2025_INCIDENT_IDENTIFICATION_PHASE6.md').read_text().splitlines()
    cells = {}
    for line in lines:
        match = re.match(r'^\| (.+?) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|', line)
        if not match:
            continue
        label, *figures = match.groups()
        country, body = label.split(' ', 1)
        category, outcome = body.rsplit(' ', 1)
        countries = dict(zip('Austria Belgium France Germany Greece Ireland Italy Malta Netherlands Spain'.split(),
                             'AT BE FR DE GR IE IT MT NL ES'.split()))
        categories = {'jihadist': 'jihadist', 'right-wing': 'right_wing',
                      'left-wing/anarchist': 'left_wing_anarchist', 'other': 'other_unspecified'}
        key = countries[country], categories[category], outcome
        check(key not in cells, f'2025 duplicate cell {key}')
        cells[key] = dict(zip(('total', *CLASSES), figures))
    return [dict(country_iso2=key[0], category=key[1], outcome=key[2], **data)
            for key, data in cells.items()]


def compact(counter):
    return ';'.join(f'{key}={counter[key]}' for key in sorted(counter))


def annual(year):
    if year == 2025:
        crosswalk = phase6_cells()
        source = [row for row in read('data/terror_2025_country_statistics.csv')
                  if row['source_system'] == 'TE-SAT 2026' and row['country_iso2'] in COUNTRIES
                  and row['measure'] in OUTCOMES]
        expected = counts(source, ('country_iso2', 'ideology_normalized', 'measure'), 'value')
        check(counts(crosswalk, ('country_iso2', 'category', 'outcome')) == expected,
              '2025 joint cell mismatch')
        coverage = read('data/terror_2025_coverage.csv')
        arrests = read('audit/arrests_2025.csv')
        annex = read('data/eu_2025_attack_outcomes_by_country_provisional.csv')
        check(counts(crosswalk, ('country_iso2', 'outcome')) ==
              margins(annex, set(annex[0]) - set(OUTCOMES)), '2025 outcome margin mismatch')
    else:
        prefix = str(year)
        crosswalk = read(f'{prefix}/crosswalk.csv')
        coverage = read(f'{prefix}/coverage.csv')
        arrests = read(f'{prefix}/arrests.csv')
        incidents = read(f'{prefix}/incidents.csv')
        sources = read(f'{prefix}/sources.csv')
        source_ids = {row['source_id'] for row in sources}
        check(ids(crosswalk, 'cell_id'), f'{year} duplicate cell ID')
        check(ids(sources, 'source_id'), f'{year} duplicate source ID')
        check(ids(incidents, 'incident_id'), f'{year} duplicate incident ID')
        seen = set()
        indexed = {row['incident_id']: row for row in incidents}
        for row in crosswalk:
            linked = list(filter(None, row.get('incident_ids', '').split(';')))
            for incident_id in linked:
                check(incident_id not in seen, f'{year} multiple allocations of {incident_id}')
                seen.add(incident_id)
                incident = indexed.get(incident_id)
                check(incident is not None, f'{year} missing incident {incident_id}')
                if incident:
                    check(incident['country_iso2'] == row['country_iso2'], f'{year} country {incident_id}')
                    check(incident['outcome_cell'] == row['outcome'], f'{year} outcome {incident_id}')
                    event_year = re.match(r'^\d{4}', incident['event_date'])
                    check(event_year is None or int(event_year[0]) == year,
                          f'{year} event date {incident_id}')
                    check(incident['category'] == row['category'], f'{year} category {incident_id}')
            if 'incident_ids' in row:
                check(len(linked) >= int(row['adequate']) + int(row['candidate']),
                      f"{year} too few linked IDs for {row['cell_id']}")
        if year >= 2023:
            category, outcome = (('category', 'outcome_cell') if year == 2023
                                 else ('eu_category', 'eu_outcome_cell'))
            allocated = Counter((row['country_iso2'], row[category], row[outcome], row['confidence'])
                                for row in incidents)
            expected_ids = Counter({(row['country_iso2'], row['category'], row['outcome'], confidence):
                                    int(row[confidence]) for row in crosswalk
                                    for confidence in CLASSES[:2]})
            check(allocated == +expected_ids, f'{year} incident confidence allocations differ')
            check(all(row['event_date'].startswith(str(year)) for row in incidents),
                  f'{year} incident outside the reference year')
        else:
            for row in crosswalk:
                linked = [indexed[key] for key in row['incident_ids'].split(';') if key in indexed]
                check(sum(incident['confidence'] == 'adequate' for incident in linked) == int(row['adequate']),
                      f"{year} adequate incident count differs for {row['cell_id']}")
        for table in (crosswalk, coverage, incidents, arrests):
            for row in table:
                references = set(filter(None, row.get('source_id', row.get('source_ids', '')).split(';')))
                check(references <= source_ids, f'{year} broken source reference {references - source_ids}')
        if year <= 2022:
            source = read(f'{prefix}/attacks.csv')
            keys = ('country_iso2', 'category', 'outcome')
            check(counts(crosswalk, keys) == counts(source, keys), f'{year} joint cell mismatch')
        else:
            outcome_source = read('2023/attacks.csv' if year == 2023 else
                                  'data/eu_2024_attack_outcomes_by_country.csv')
            category_source = outcome_source if year == 2023 else read('data/eu_2024_attacks_by_country_ideology.csv')
            source = outcome_source
            check(counts(crosswalk, ('country_iso2', 'outcome')) ==
                  margins(outcome_source, set(outcome_source[0]) - set(OUTCOMES)),
                  f'{year} outcome margin mismatch')
            reserved = (set(OUTCOMES) | META | {'year', 'source_url', 'source_page', 'source_scope'})
            labels = ({'other': 'other_combined', 'not_specified': 'other_combined'}
                      if year == 2023 else {'separatist': 'ethno_nationalist_separatist'})
            normalized = [dict(row, category=labels.get(row['category'], row['category']))
                          for row in crosswalk]
            check(counts(normalized, ('country_iso2', 'category')) == margins(category_source, reserved), f'{year} category margin mismatch')
    check({row['country_iso2'] for row in coverage} == COUNTRIES and len(coverage) == 31,
          f'{year} malformed coverage grid')
    for row in crosswalk:
        check(row['country_iso2'] in COUNTRIES, f'{year} invalid country')
        check(int(row['total']) == sum(int(row[key]) for key in CLASSES),
              f'{year} partition mismatch: {row}')
    by_country = counts(source, ('country_iso2',), 'value' if year == 2025 else 'total')
    check(by_country == counts(crosswalk, ('country_iso2',)), f'{year} total by country mismatch')
    fixed_attacks = sum(total for (country,), total in by_country.items() if country != 'GB')
    arrest_totals = arrest_categories = None
    if arrests is not None:
        for row in arrests:
            check(sum(int(value or 0) for key, value in row.items() if key not in META) == int(row['total']),
                  f"{year} arrest components differ in {row['country_iso2']}")
        arrest_totals = counts(arrests, ('country_iso2',))
        arrest_categories = cols(arrests, arrests[0].keys() - META)
    categories = Counter()
    outcomes = Counter()
    for row in crosswalk:
        categories[row['category']] += int(row['total'])
        outcomes[row['outcome']] += int(row['total'])
    classes = cols(crosswalk, CLASSES)
    return dict(year=year, attacks=sum(by_country.values()), uk_attacks=by_country['GB',],
                eu27_attacks=fixed_attacks,
                arrests=sum(arrest_totals.values()) if arrest_totals is not None else '',
                uk_arrests=arrest_totals['GB',] if arrest_totals is not None else '',
                eu27_arrests=sum(n for (country,), n in arrest_totals.items() if country != 'GB') if arrest_totals is not None else '',
                **{key: outcomes[key] for key in OUTCOMES}, **{key: classes[key] for key in CLASSES},
                attack_categories=compact(categories), arrest_categories=compact(arrest_categories or {}))


def main():
    results = [annual(year) for year in range(2015, 2026)]
    corrections = read('2021/provenance.csv')
    check(ids(corrections, 'adjustment_id'), 'duplicate historical adjustment')
    revisions = Counter()
    sensitivity = Counter()
    for row in corrections:
        year = int(row['occurrence_year'])
        count = int(row['affected_records'])
        action = row['entry_action']
        if action == 'removed_after_court_reclassification':
            revisions[year] -= count
            sensitivity[year] -= count
        elif action == 'omitted_then_backfilled_in_historical_reference':
            revisions[year] += count
            sensitivity[year] += count
        elif action == 'omitted_then_included_in_later_reference_cohort':
            sensitivity[year] += count
            sensitivity[int(row['later_reference_year'])] -= count
        else:
            check(False, f'Unreviewed historical adjustment action {action}')
    for result in results:
        year = result['year']
        result['later_official_attacks'] = result['attacks'] + revisions[year] if year in revisions else ''
        result['occurrence_sensitivity_attacks'] = result['eu27_attacks'] + sensitivity[year]
    expected = read('data/eu_statistical_reconciliation_2015_2025.csv')
    fields = {'attacks': 'original_attacks', 'uk_attacks': 'included_uk_attacks',
              'eu27_attacks': 'fixed_eu27_attacks', 'arrests': 'original_arrests',
              'uk_arrests': 'included_uk_arrests', 'eu27_arrests': 'fixed_eu27_arrests',
              'later_official_attacks': 'later_official_attack_revision',
              'occurrence_sensitivity_attacks': 'occurrence_sensitivity_attacks',
              **{key: f'{key}_slots' for key in CLASSES}}
    for result, archived in zip(results, expected, strict=True):
        check(str(result['year']) == archived['reference_year'], 'annual register order mismatch')
        for left, right in fields.items():
            if result[left] != '':
                check(str(result[left]) == archived[right], f"{result['year']} summary mismatch: {left}")
    writer = csv.DictWriter(sys.stdout, fieldnames=results[0], lineterminator='\n')
    writer.writeheader()
    writer.writerows(results)
    for issue in issues:
        print(issue, file=sys.stderr)
    return bool(issues)


if __name__ == '__main__':
    sys.exit(main())
