# DDR-01 Robustness Matrix v0.1

Status: FIRST ROBUSTNESS PASS COMPLETE  
Date: 2026-09-18  
Parent: DDR-01 // Demographic Voting Alignment  
Method status: FROZEN v0.1  
Signal status: NOT A SIGNAL

## Purpose

This pass tests whether the current DDR-01 mechanism survives when weaker or more controversial evidence is removed.

The frozen mechanism-level formulation is:

> Demographic change can alter electoral competition through both direct voting and indirect electorate responses. Neither channel has a fixed ideological direction. Their magnitude and direction depend on turnout, origin composition, geography, party supply and time.

The matrix below does not ask whether every country remains in the analysis. It asks whether the mechanism-level conclusion survives under progressively stricter evidence rules.

---

# Test set

Current main evidence cases:

- Sweden
- Norway
- Germany
- Great Britain
- United States
- Denmark
- Italy

Current weaker / non-comparable cases remain outside the core robustness set.

---

# Robustness matrix

| Test | Evidence retained | Evidence removed | Result for DDR-01 | Status |
|---|---|---|---|---|
| R1 Baseline | Sweden, Norway, Germany, Great Britain, US, Denmark, Italy | None | Direct + indirect mechanisms both present; direction varies | SURVIVES |
| R2 Remove Sweden | Norway, Germany, Great Britain, US, Denmark, Italy | Sweden | Direct heterogeneity, turnout composition and counter-mobilization remain | SURVIVES |
| R3 Remove Denmark + Italy | Sweden, Norway, Germany, Great Britain, US | Historical causal counter-mobilization evidence | Direct demographic realignment survives; indirect channel loses strongest causal support | PARTIAL SURVIVAL |
| R4 A/B individual-level only | Sweden, Norway, Germany, Great Britain, US | Denmark, Italy and ecological/local evidence | Broad background effects, heterogeneity and turnout-composition remain | SURVIVES DIRECT CHANNEL |
| R5 2020–2026 only | Sweden, Norway, Germany, Great Britain, US + contemporary Italy association where relevant | Older historical studies | Direct mechanism survives strongly; causal counter-mobilization becomes unresolved | SURVIVES, NARROWER |
| R6 Remove aggregate/ecological evidence | Sweden official survey, Norway official election study/panel, Germany survey, Britain individual survey/BES, US validated voters | Constituency/municipality-only claims | No homogeneous bloc; turnout and origin heterogeneity still hold | SURVIVES |
| R7 Remove model-derived outcome estimates | All source-reported evidence retained | Sweden 30–35k comparison as causal evidence; Norway ~60k standardized estimate | Mechanism remains; outcome-relevance claims become less quantitative | SURVIVES |
| R8 Remove Great Britain | Sweden, Norway, Germany, US, Denmark, Italy | Britain | Core findings still present | SURVIVES |
| R9 Remove United States | Sweden, Norway, Germany, Britain, Denmark, Italy | US validated-voter turnout-composition case | Direct/indirect mechanism survives; strongest turnout-composition proof weakens | SURVIVES |
| R10 Remove Germany | Sweden, Norway, Britain, US, Denmark, Italy | strongest origin-divergence counterexample | Non-homogeneity still visible in Norway, Britain and US | SURVIVES |
| R11 Exclude all historical causal evidence | Sweden, Norway, Germany, Britain, US | Denmark/Italy causal mechanism evidence | Only direct channel is strongly established | DIRECT CHANNEL SURVIVES / INDIRECT CHANNEL OPEN |
| R12 Require fixed ideological direction | All cases | N/A | Cases contradict one common left/right direction | FAILS BY DESIGN |
| R13 Require immigrant-background variable to dominate controls | Norway, Britain, Germany, US, Sweden | N/A | Evidence mixed; background sometimes remains independent but composition often matters strongly | FAILS AS UNIVERSAL RULE |

---

# Detailed stress results

## R2 — Sweden removal

Removing Sweden eliminates:
- the strongest current case of renewed left-green preference alignment;
- the narrow-margin 2026 outcome-relevance example.

What remains:
- Norway: historical left tilt + fragmentation;
- Germany: origin groups pull in opposite directions;
- Britain: broad Labour alignment + subgroup fragmentation;
- US: rapid convergence via turnout composition;
- Denmark/Italy: indirect counter-mobilization evidence.

Conclusion:

**DDR-01 does not depend on Sweden.**

Sweden is an illustrative case, not the structural foundation of the model.

---

## R3 — Remove Denmark and Italy

This is the most important negative test.

Without Denmark and Italy:
- the direct channel remains well supported;
- the indirect counter-mobilization channel loses its strongest causal-identification evidence;
- Britain/Norway/Germany/US still show subgroup variation, turnout effects and changing alignment.

Conclusion:

**The full two-channel model weakens.**

The correct robustness statement becomes:

> The direct demographic-voting channel is robust. The indirect counter-mobilization channel is credible but depends disproportionately on historical causal studies from Denmark and Italy.

Status:
**PARTIAL SURVIVAL**

This prevents overclaiming DDR6.

---

## R4 — A/B individual-level evidence only

Retained:
- Sweden SCB individual survey
- Norway SSB election study + panel research
- Germany KAS representative survey
- Britain Focaldata/BES individual survey evidence
- US Pew validated-voter panel

Removed:
- Denmark municipality studies
- Italy municipality studies
- ecological constituency observations where not tied to individual surveys

What still survives:
1. immigrant/minority-origin electorates are not homogeneous;
2. broad left alignment exists in some systems but not all;
3. alignment can change rapidly;
4. origin subgroup matters;
5. turnout composition can materially reshape aggregate results;
6. demographic-background effects sometimes persist after controls.

Conclusion:

**The central direct-channel model survives without ecological evidence.**

This is one of DDR-01's strongest robustness results.

---

## R5 — 2020–2026 evidence only

This removes most historical causal studies and older trajectory evidence.

Retained:
- Sweden 2022–2026
- Norway 2021–2025
- Germany 2025
- Britain 2024
- US 2020–2024
- Italy 2022 contemporary association

Result:
- Sweden: strong current left-green background gap;
- Norway: fragmentation and Frp gains;
- Germany: strong origin divergence;
- Britain: aggregate Labour advantage with subgroup fragmentation;
- US: sharp convergence among naturalized voters;
- Italy: no uniform current immigration→right relationship.

Conclusion:

**Direction-context dependence becomes even clearer.**

But:
- the historical existence of counter-mobilization as a causal mechanism becomes much less secure without Denmark/older Italy.

Status:
**SURVIVES, NARROWER**

---

## R6 — Remove ecological evidence

Removed:
- immigrant-dense district interpretation in Sweden;
- Britain seat-level demographic associations;
- Denmark/Italy local aggregate evidence unless tied to causal research;
- any neighbourhood-based inference.

Retained:
- individual surveys, official election studies, validated-voter evidence.

Conclusion:

**The claims that matter most survive.**

The project does not need ecological inference to establish:
- subgroup heterogeneity;
- changing alignment;
- turnout composition;
- residual background effects in some systems.

Ecological evidence is useful for geographic translation, not foundational to the model.

---

## R7 — Remove model-derived vote estimates

Removed from inferential core:
- Sweden's 30k–35k new-citizen estimate as evidence of causal decisiveness;
- Norway's approximately 60k standardized left-minus-right estimate.

Retained:
- source-reported turnout;
- source-reported party choice;
- certified/preliminary election totals;
- official electorate-size estimates.

Result:

The model still shows:
- who participates matters;
- vote alignment differs by background;
- subgroup alignment changes over time.

What weakens:
- exact statements about outcome relevance.

Conclusion:

**DDR-01 is not dependent on NPCsignals calculations.**

This is methodologically important.

---

## R9 — Remove United States

The US supplies the cleanest evidence that aggregate demographic realignment can be driven by turnout composition rather than mass persuasion.

Without the US:
- turnout still matters in Norway and Sweden;
- but the direct decomposition of entrants, dropouts and switchers becomes much weaker.

Conclusion:

**The broad model survives, but DDR-CF12 becomes provisional rather than strongly supported.**

This identifies the US as a high-leverage evidentiary case.

---

## R12 — Force a fixed ideological direction

Test:
Can DDR-01 be summarized as "demographic change helps the left" or "demographic change helps the right"?

Evidence:
- Sweden: stronger left-green alignment among foreign-background respondents;
- Norway: aggregate left tilt with rightward fragmentation;
- Germany: different origin groups support opposite blocs;
- Britain: Labour advantage plus internal fragmentation;
- US: naturalized electorate near parity after major Republican gains;
- Denmark/Italy: some historical indirect rightward responses among other voters.

Conclusion:

**FIXED-DIRECTION MODEL REJECTED**

No single left/right direction survives the country comparison.

This is not a weakness in DDR-01; it is one of the central falsified alternatives.

---

## R13 — Require broad background status to dominate all controls

Norway:
basic demographic controls do not eliminate the observed shift, but attitudes and religion matter.

Britain:
ethnicity retains predictive value in long-run multivariate BES models.

Germany:
origin-specific composition is critical and the broad migration-background category is too coarse.

US:
nativity clearly matters for turnout; residual party-choice effect after full controls is unresolved.

Sweden:
full residual multivariate effect remains unresolved in the current source set.

Conclusion:

**PURE BACKGROUND MODEL REJECTED**

Best surviving interpretation:

> Broad background status can retain independent electoral relevance in some systems, but much of the observed political pattern is compositional and mediated.

---

# Robustness summary

## Strongly robust

1. **No homogeneous immigrant/minority electoral bloc**
2. **No fixed ideological direction**
3. **Origin/subgroup heterogeneity matters**
4. **Turnout must be separated from preference**
5. **Outcome relevance is not equivalent to causal decisiveness**
6. **National averages can conceal local/subgroup divergence**
7. **Broad background categories are often too coarse**

## Moderately robust

8. **Historical left alignment can persist while fragmenting**
9. **Background effects sometimes survive demographic controls**
10. **Demographic realignment can occur through turnout composition**

## Evidence-dependent

11. **Indirect counter-mobilization**
   - strongest causal support currently depends on Denmark/Italy historical studies;
   - contemporary magnitude remains unresolved.

12. **Exact electoral outcome contribution**
   - sensitive to assumptions, electoral systems and data availability.

---

# Robustness verdict

DDR-01 survives the first robustness matrix, but in a narrower form than a simple demographic-voting hypothesis.

Current status:

**DIRECT CHANNEL — ROBUST**  
**INDIRECT COUNTER-MOBILIZATION — SUPPORTED BUT EVIDENCE-CONCENTRATED**  
**FIXED LEFT/RIGHT DIRECTION — FALSIFIED**  
**PURE COMPOSITIONAL EXPLANATION — NOT SUFFICIENT**  
**PURE BACKGROUND EXPLANATION — REJECTED**  
**EXACT CAUSAL MAGNITUDE — UNRESOLVED**

Overall:

**MECHANISM ROBUST / DIRECTION CONTEXT-DEPENDENT / MAGNITUDE UNRESOLVED**

Signal status:

**NOT A SIGNAL**

---

# Gate to DDR-01 v1.0

Before v1.0:

1. complete evidence-availability pass for France, Poland, Costa Rica, Chile and Japan;
2. retain Ghana, Botswana and Thailand as separate cleavage tracks unless comparable evidence emerges;
3. update Sweden only after final election certification where relevant;
4. ensure every model-derived number is labeled;
5. preserve Great Britain source correction;
6. rerun robustness matrix if any new A/B-quality country materially contradicts the current mechanism.

Only after those steps should DDR-01 move from v0.1 working module to v1.0 archived research module.

NPCsignals  
Observe → Filter → Validate → Stress → Archive → Review
