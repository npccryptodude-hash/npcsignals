"""Read-only reconstruction of deposited presidential workbook statistics.

Run with python3 from any directory. Uses only the standard library.
Prints JSON; never modifies a workbook or research record.
"""
from pathlib import Path
from collections import Counter
import hashlib
import json
import re
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / 'research/presidential-claim-stress-test-2025-2026'
MAIN = CASE / 'NPCsignals_Presidential_Claim_Stress_Test_Ledger_v1.0.xlsx'
BLIND = CASE / 'NPCsignals_Trump_Claim_Stress_Test_Blind_Second_Pass (1).xlsx'
NS = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main',
      'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}


def workbook(path):
    with zipfile.ZipFile(path) as z:
        strings = [''.join(x.itertext()) for x in ET.fromstring(z.read('xl/sharedStrings.xml'))]
        rel = {x.attrib['Id']: x.attrib['Target'].lstrip('/') for x in
               ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
        result = {}
        for sheet in ET.fromstring(z.read('xl/workbook.xml')).find('m:sheets', NS):
            target = rel[sheet.attrib['{' + NS['r'] + '}id']]
            if not target.startswith('xl/'):
                target = 'xl/' + target
            rows = []
            for row in ET.fromstring(z.read(target)).find('m:sheetData', NS):
                cells = {}
                for cell in row:
                    coordinate = cell.attrib['r']
                    letters = re.match('[A-Z]+', coordinate).group()
                    column = 0
                    for ch in letters:
                        column = column * 26 + ord(ch) - 64
                    value = cell.find('m:v', NS)
                    if value is None:
                        v = None
                    elif cell.attrib.get('t') == 's':
                        v = strings[int(value.text)]
                    else:
                        try:
                            number = float(value.text)
                            v = int(number) if number.is_integer() else number
                        except (ValueError, TypeError):
                            v = value.text
                    cells[column - 1] = v
                values = [cells.get(i) for i in range(max(cells, default=-1) + 1)]
                rows.append((int(row.attrib['r']), values))
            result[sheet.attrib['name']] = rows
        return result


def claims(rows):
    return {v[0]: (n, v) for n, v in rows if v and re.fullmatch(r'L\d{3}', str(v[0]))}


def kappa(a, b, linear=False):
    n = len(a)
    categories = sorted(set(a + b))
    ca, cb = Counter(a), Counter(b)
    if not linear:
        observed = sum(x == y for x, y in zip(a, b)) / n
        expected = sum(ca[x] * cb[x] for x in categories) / n ** 2
        return (observed - expected) / (1 - expected)
    distance = lambda x, y: abs(categories.index(x) - categories.index(y)) / (len(categories) - 1)
    observed = sum(distance(x, y) for x, y in zip(a, b)) / n
    expected = sum(ca[x] * cb[y] * distance(x, y) for x in categories for y in categories) / n ** 2
    return 1 - observed / expected


def run():
    main, blind = workbook(MAIN), workbook(BLIND)
    ledger = claims(main['Public Ledger v1.0'])
    eligible = {k: v for k, v in ledger.items() if v[1][22] != 'EXCLUDED'}
    comparisons = claims(main['Inter-Rater Analysis'])
    embedded = claims(main['Blind Second Pass'])
    separate = claims(blind['Blind Claims'])
    assert len(eligible) == len(comparisons) == len(separate) == 78
    assert set(eligible) == set(comparisons) == set(separate)
    normalization = {'SUPPORTED': 'PASS', 'MIXED / MISLEADING': 'MIXED',
                     'UNSUPPORTED': 'UNSUPPORTED', 'FALSE / SEVERE': 'FALSE'}
    for k, (_, row) in eligible.items():
        comp = comparisons[k][1]
        assert normalization[row[22]] == comp[2]
        assert row[15] == comp[5] and row[18] == comp[11]
        assert (comp[2] == comp[3]) == (comp[4] == 'AGREE')
        assert (comp[5] == comp[6]) == (comp[8] == 'AGREE')
        assert (comp[6] - comp[5]) == comp[7]
        for threshold, column in [(2, 9), (3, 10)]:
            assert ((comp[5] >= threshold) == (comp[6] >= threshold)) == (comp[column] == 'AGREE')
    rows = [v for _, v in eligible.values()]
    ir = [v for _, v in comparisons.values()]
    pi = [v for v in ir if v[11] is not None]
    inputs = lambda row: [row[i] for i in [0, 2, 3, 4, 9, 10, 11, 12]]
    embedded_diffs = [k for k, (_, row) in eligible.items() if embedded[k][1][:8] != inputs(row)]
    separate_diffs = [k for k, (_, row) in eligible.items() if separate[k][1][:8] != inputs(row)]
    pair_counts = Counter((v[2], v[3]) for v in ir)
    result = {
        'input_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in [MAIN, BLIND]},
        'ledger_rows': len(ledger), 'eligible': len(rows), 'excluded': ['L053'],
        'accuracy_counts': dict(Counter(v[22] for v in rows)),
        'recorded_second_accuracy_counts': dict(Counter(v[3] for v in ir)),
        'accuracy_confusion_pairs': [{'first': a, 'second': b, 'n': n}
                                     for (a, b), n in sorted(pair_counts.items())],
        'accuracy_exact_agreement': sum(v[2] == v[3] for v in ir),
        'accuracy_kappa': kappa([v[2] for v in ir], [v[3] for v in ir]),
        'cai_counts': dict(Counter(str(v[15]) for v in rows)),
        'cai_ge2': sum(v[15] >= 2 for v in rows), 'cai_ge3': sum(v[15] >= 3 for v in rows),
        'cai_exact_agreement': sum(v[5] == v[6] for v in ir),
        'cai_ge2_agreement': sum((v[5] >= 2) == (v[6] >= 2) for v in ir),
        'cai_ge3_agreement': sum((v[5] >= 3) == (v[6] >= 3) for v in ir),
        'cai_linear_weighted_kappa': kappa([v[5] for v in ir], [v[6] for v in ir], True),
        'pi_comparable_rows': len(pi), 'pi_exact_agreement': sum(v[11] == v[12] for v in pi),
        'pi_ge2_agreement': sum((v[11] in ['P2', 'P3']) == (v[12] in ['P2', 'P3']) for v in pi),
        'pi_kappa_comparable_rows': kappa([v[11] for v in pi], [v[12] for v in pi]),
        'pi_missing': sum(v[18] is None for v in rows),
        'pi_ge2_documented_floor': sum(v[18] in ['P2', 'P3'] for v in rows),
        'par_documented_floor': sum(v[18] in ['P2', 'P3'] and v[15] >= 2 for v in rows),
        'missing_statement_urls': [v[0] for v in rows if not v[10]],
        'missing_statement_dates': [v[0] for v in rows if not v[2]],
        'year_date_conflicts': [v[0] for v in rows if v[2] and str(v[1]) != str(v[2])[:4]],
        'blind_embedded_claim_rows': len(embedded), 'blind_separate_claim_rows': len(separate),
        'embedded_completed_score_rows': sum(any(x is not None for x in v[8:]) for _, v in embedded.values()),
        'separate_completed_score_rows': sum(any(x is not None for x in v[8:]) for _, v in separate.values()),
        'embedded_input_differences_from_eligible_ledger': embedded_diffs,
        'separate_input_differences_from_eligible_ledger': separate_diffs,
        'conditional_high_salience_control_ratio': (51 / 78) / .30,
        'ratio_limitation': 'arithmetic conditional on the reported 30 percent control rate; no 50-item control dataset reconstructed',
        'limits': 'reproduces stored values and derived statistics, not historical reviewer independence or all factual verdicts',
    }
    matrix = json.loads((Path(__file__).parent / 'verification-matrix.json').read_text())
    assert {v['claim_id'] for v in matrix['eligible_records']} == set(eligible)
    for v in matrix['eligible_records']:
        n, original = eligible[v['claim_id']]
        assert v['ledger_row'] == n and v['recorded_classification'] == original[22]
        assert v['statement_url'] == original[10] and v['benchmark_url'] == original[12]
        assert v['recorded_cai'] == original[15] and v['recorded_pi'] == original[18]
    result['matrix_original_field_crosschecks'] = 'pass for all 78 eligible records'
    return result


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, ensure_ascii=False))
