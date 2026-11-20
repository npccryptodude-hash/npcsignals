# phase 26 — independent editorial challenge review (pre-human)

review date: 18 november 2026
reviewed checkpoint: `8a62754c008c3cfe0f544fb37cb94e15c1078000`
status: **independent model challenge completed; human editorial approval not granted**

## scope and independence

this is a separate adversarial reading of the phase 24 reader-facing draft and phase 25 claim/source/figure documentation. it tests likely reader inferences, not just arithmetic. it is not a substitute for an independent human editor, final export inspection or publication permission. no underlying statistical observations were altered.

## focused primary-source check: 193 / 211

- europol TE-SAT 2016, printed p. 10 and annex p. 44: the 2015 reporting cohort is 211; the 2016 edition's figure 1 also uses 211 (printed p. 11).
- europol TE-SAT 2017, printed p. 10: the retrospective prose states 211 for 2015.
- europol TE-SAT 2017, printed p. 11, figure 1: the retrospective 2015 chart value is 193.
- direct sources: https://www.europol.europa.eu/cms/sites/default/files/documents/europol_tesat_2016.pdf and https://www.europol.europa.eu/cms/sites/default/files/documents/tesat2017_0.pdf
- **finding:** the 193 figure is in the 2017 edition, not the 2016 original. the 2016 source supports 211. the later edition contains an unresolved within-edition inconsistency between prose and chart. neither a correction mechanism nor intent is established.
- **recommended reader wording:** "for the 2015 reporting year, europol's 2016 edition reports 211 attacks. its 2017 edition repeats 211 in the prose but plots 193 for 2015 in figure 1. the source of the discrepancy remains unverified."
- **citation action:** cite TE-SAT 2016 pp. 10–11 and 44 **and** TE-SAT 2017 pp. 10–11, figure 1; do not cite TE-SAT 2016 p. 44 as the source of 193.

## reader-inference stress test

| risk | plausible reader inference | actual evidence boundary | editorial action |
|---|---|---|---|
| high | "119 to 57 means terrorism fell by half" | 2019 includes the uk; fixed eu27 is 55 versus original 57 in 2020, with later 56 revision | retain scope in first sentence and image caption; never display 119 and 57 alone as a trend |
| high | "2023 surge is disproved" | 26 older french entries; the 44-entry delta is a conditional sensitivity calculation, not an official occurrence-year series | place "conditional scenario" in the same sentence as 44 and label all figure markers |
| high | "europol cannot document 926 attacks" | 926 are unidentified in the project's public-source crosswalk, not missing from europol's files | state ownership of the linkage method next to 926 and repeat in figure accessibility text |
| high | "national versus europol differences reveal suppression" | national and eu records use different units and lack a common event-key crosswalk | prohibit missing-event or concealment language; label issuer, unit, geography and reference year |
| high | "406 convictions out of 486 arrests" | court decisions and arrests are not linked populations or same-case cohorts | avoid adjacency without an explicit no-rate warning; distinguish eurojust judicial counts |
| medium | "the a100 deletion is proved" | the court's classification finding is supported, but the removed statistical slot has no verified event key | preserve candidate label; do not visually join the nodes with an unqualified solid arrow |
| medium | "is contacts commanded solingen" | official court summary records advice/encouragement, not verified operational command | use "contacts" and attribute to the court summary, not an independently verified chain of command |
| medium | "193 proves data manipulation" | different published values are established; cause, correction history and intent are unknown | cite exact editions and figure, preserve unknown cause |
| medium | "injury numbers are directly comparable" | 379 overall, 374 in annex, and three narratives summing 597 have unresolved units/definitions | describe as incompatible source observations; do not combine into an estimated injury total |
| medium | "the research covers every european terrorist incident" | 31-country research grid is not a harmonized event census; europol editions have changing scope | explicitly delimit territory and statistical unit in title/deck and conclusion |

## editorial assessment

**strengths:** the draft foregrounds geographic scope, reporting-year versus occurrence-year distinctions, incompatible institutional counting units, and the difference between a public-source identification exercise and europol's internal evidence. it does not accuse institutions or defendants of unproven conduct. the judicial examples are attributed and explicitly nonrepresentative.

**remaining edits before human signoff:**
1. clarify the 193/211 source attribution at the discrepancy paragraph and in the source guide; cite the later chart explicitly.
2. make the conditional nature of the 2022–2023 sensitivity result unmissable in any detached figure, social preview or excerpt.
3. ensure 926 always appears with "unidentified by this project's public-source linkage", not merely "unidentified attacks".
4. do not put the national and europol counts in an unlabelled comparative graphic; retain source-specific units.
5. have a human editor inspect all final exports and text alternatives, especially detached images and mobile captions.
6. have a human editor assess the risk of implying guilt, organisational command, suppression or wrongdoing beyond the court/source record.

## verdict

**PASS — suitable for independent human editorial review, with targeted wording and citation corrections identified.**

**NOT PASS — publication approval.** final human signoff, dissemination-format inspection and explicit authorisation remain outstanding. this model challenge does not constitute the requested independent human approval.
