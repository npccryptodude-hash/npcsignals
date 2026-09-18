# DDR-01 Source Audit v0.1

Status: SOURCE AUDIT COMPLETE — FIRST PASS  
Date: 2026-09-18  
Parent: DDR-01 // Demographic Voting Alignment  
Method status: FROZEN v0.1  
Evidence status: OPEN  
Signal status: NOT A SIGNAL

## Audit purpose

This file checks whether the current DDR-01 claims are supported at the strength used in the working notes.

Each item is marked:

- **CONFIRMED** — source directly supports the claim.
- **TIGHTEN** — source supports the general claim but wording or scope should be narrowed.
- **MODEL-DERIVED** — value is an internal calculation, not a source-reported fact.
- **QUARANTINE** — do not reuse until source/value is independently rechecked.
- **OPEN** — evidence not yet sufficient for a firm claim.

The audit prioritizes official statistics, validated-voter studies and peer-reviewed research over press summaries.

---

# Norway

## Source set

Primary:
- Statistics Norway (SSB), *Immigrants and the General Election 2025*, Reports 2026/3.
- Bergh & Kleven (2026), *Social conservatism and changing party preferences among immigrants in Norway*, Politics.

## Claims

### 2025 turnout
- immigrants: 56%
- Norwegian-born with immigrant parents: 60%
- voters without immigrant background: 83%

**CONFIRMED**

SSB directly reports these values.

### Turnout increase from 2021
- immigrants: +6 percentage points
- Norwegian-born with immigrant parents: +8 percentage points

**CONFIRMED**

Directly reported by SSB.

### Historical left tilt / weakening alignment
The immigrant-background electorate has historically leaned centre-left, while more recent elections show movement toward centre-right parties.

**CONFIRMED**

SSB and Bergh/Kleven both support the broad trajectory.

### Explanation of the 2019–2023 rightward shift
Claim: age, gender and education do not explain the shift; social conservatism/religiosity is not the main driver; economic attitudes matter more.

**CONFIRMED WITH SCOPE LIMIT**

Bergh & Kleven directly test the 2019–2023 local-election panel and find that economic-policy attitudes explain the shift more strongly than social conservatism. This result should not be generalized automatically to the 2025 national election.

Status:
**CONFIRMED FOR 2019–2023 LOCAL-ELECTION PANEL / DO NOT EXTEND CAUSALLY TO 2025**

### Approx. 264,500 immigrant-origin votes cast in 2025

**MODEL-DERIVED**

This is obtained by multiplying group-level eligible-voter counts by rounded turnout percentages. It is not an official SSB count of ballots cast by background.

Use wording:
> approximately 264,500 implied votes under reported group turnout rates

Do not write:
> 264,500 immigrant-origin voters voted

without qualification.

### Approx. 60,000 additional net left-minus-right votes

**MODEL-DERIVED / SENSITIVE TO PARTY GROUPING**

This is an internal standardization that depends on:
- the selected left/right grouping;
- rounded turnout;
- survey estimates of party choice;
- the chosen reference group.

It must not be presented as an observed SSB figure.

Status:
**KEEP AS SENSITIVITY CALCULATION ONLY**

---

# Sweden

## Source set

Primary:
- Statistics Sweden (SCB), Party Preference Survey, May 2026.
- SCB PxWeb official series by Swedish/foreign background, 2006M05–2026M05.

## Claims

### SCB series exists from 2006 through 2026 by Swedish/foreign background

**CONFIRMED**

The official PxWeb table covers 2006M05–2026M05 and is official statistics.

### Party sympathy is not identical to actual vote choice

**CONFIRMED**

SCB explicitly states that *partisympati* means the party a respondent feels closest to and is not necessarily the party they would vote for.

This distinction must remain in every Sweden longitudinal interpretation.

### May 2026 broad foreign-background vs Swedish-background alignment

**CONFIRMED AT SOURCE-FAMILY LEVEL / EXACT VALUES REQUIRE TABLE-LEVEL LOCK**

The official SCB database contains the required subgroup estimates. The current working note's exact party percentages should be retained provisionally but should receive a table-export verification before v1.0.

Status:
**TIGHTEN — VERIFY EXACT CELL VALUES FROM PXWEB EXPORT BEFORE FINAL FREEZE**

### 2006–2026 trajectory

**CONFIRMED AS AN AVAILABLE SERIES**

The existence of a longitudinal official series is confirmed.

Any specific trend statement should be based on extracted table values rather than prose summaries.

### Sweden 2026 new-citizen 30k–35k estimate

**TIGHTEN**

This is a model-based media estimate, not an official Election Authority statistic.

It depends on assumptions regarding:
- turnout;
- origin-group vote patterns;
- age/minor adjustment;
- transfer of broader group behaviour to newly naturalized citizens.

Use:
> estimated under SVT's assumptions

Do not convert it into a measured vote count.

### "Material, not causally decisive"

**SUPPORTED AS A WORKING DESCRIPTIVE LABEL**

This is an NPCsignals research classification, not a source-reported conclusion.

It is defensible only if the assumptions and provisional election-margin comparison remain visible.

---

# Germany

## Source set

Primary:
- Destatis, 17 Dec 2024, electorate with immigration history.
- Destatis, estimated 2025 federal electorate.
- Konrad-Adenauer-Stiftung, *Voting behaviour of people with a migration background*, 30 Sep 2025.

## Claims

### 17.1m adults with immigration history in 2023; 7.1m eligible; 12% of eligible electorate

**CONFIRMED**

Destatis directly reports:
- 17.1 million adults with immigration history;
- 7.1 million would have been eligible;
- 12% of all eligible voters.

Destatis explicitly warns that this is an approximate 2023 benchmark for the 2025 election.

### 59.2m minimum eligible voters for 2025 Bundestag election

**CONFIRMED**

Official Destatis estimate.

### Origin-group party differences
- Turkish-origin: SPD strongest; Left above average.
- Russian-origin: SPD strongest; Left above average.
- Polish-origin: AfD strongest, CDU/CSU second.
- late repatriates: AfD strongest, CDU/CSU second.

**CONFIRMED**

Directly stated by KAS.

### "Migration-background electorate has no single national direction"

**CONFIRMED DESCRIPTIVELY**

The origin-group divergence directly supports rejecting a homogeneous-bloc interpretation.

### "Origin matters more than migration status"

**TIGHTEN**

The KAS evidence clearly shows strong origin heterogeneity, but "matters more" is a comparative explanatory claim requiring a multivariate model.

Preferred wording:
> Origin-specific differences are large enough that the broad migration-background category can obscure opposite partisan patterns.

---

# Great Britain

## Source set

Primary:
- Focaldata, *How Britain Voted 2024*, n=52,907.
- Focaldata / UK in a Changing Europe, *Minorities Report*, Oct 2024.
- Parliamentary Affairs, BES-based analysis of group bases of British politics, 1983–2019.
- House of Commons Library, ethnic diversity in politics/public life.

## Claims

### Labour fell 13 points among Asian voters to 43% in 2024

**CONFIRMED**

Directly reported by Focaldata.

### Five of seven Labour-lost seats had Muslim populations above 25%

**CONFIRMED**

Directly reported by Focaldata.

### Labour vote among Muslim voters fell by roughly 28 points

**CONFIRMED**

Directly reported in the Minorities Report summary.

### Leicester East / Hindu-concentration observation

**CONFIRMED DESCRIPTIVELY**

Focaldata reports Leicester East as the Conservative gain with the highest Hindu population, and strong Conservative performance in Harrow East.

This is an ecological/place-level observation, not proof that Hindu identity caused individual vote choice.

### Ethnicity remains predictive after controls in long-run BES analysis

**CONFIRMED**

The Parliamentary Affairs study finds ethnicity remains statistically and substantively significant while controlling for class, region, religion, education, sex and other group variables.

It reports roughly 4:1 odds of Labour voting among South Asian and Black respondents, holding other variables constant.

### "Locally decisive patterns"

**TIGHTEN**

The evidence establishes strong local association and material constituency-level shifts, but "decisive" can imply a causal counterfactual not directly identified.

Replace in v1.0 with:
**LOCALLY MATERIAL PATTERNS**

Preferred DDR7 language:
> MATERIAL NATIONAL ELECTORATE / LOCALLY MATERIAL SUBGROUP SHIFTS / NATIONAL GOVERNMENT EFFECT NOT IDENTIFIED

### Historical minority vote series in the current working note

**QUARANTINE**

The previously listed sequence:
- 2010 Labour 60 / Conservative 16
- 2015 Labour 65 / Conservative 23
- 2017 Labour 73 / Conservative 39
- 2019 Labour 64 / Conservative 20
- 2024 Labour 49 / Conservative 20

must not be reused as written until the original datasets and denominators are reconciled.

Reason:
some figures may originate from different surveys, subgroup definitions or denominators; the 2017 pair especially requires rechecking before publication.

Status:
**REMOVE FROM FINAL NARRATIVE UNTIL REBUILT FROM CONSISTENT SOURCES**

This is the most important correction generated by this audit.

---

# United States

## Source set

Primary:
- Pew Research Center validated-voter analysis, 26 Jun 2025.
- Pew validated-voter methodology.
- Pew/Census naturalized eligible-voter analysis.

## Claims

### Naturalized citizens: Harris 51 / Trump 47 in 2024

**CONFIRMED**

### Naturalized citizens: Biden 59 / Trump 38 in 2020

**CONFIRMED**

### Naturalized citizens were 9% of 2024 voters

**CONFIRMED**

### 22% of 2024 naturalized voters had not voted in 2020; 57% of that group voted Trump

**CONFIRMED**

### Among 2020 naturalized voters absent in 2024, 67% had voted Biden

**CONFIRMED**

### Candidate switching was roughly offset; turnout composition explains most aggregate change

**CONFIRMED**

Pew directly makes this interpretation.

### 23.8m naturalized eligible voters / about 10% of electorate

**CONFIRMED FOR 2022 ACS BENCHMARK**

Do not present it as an exact 2024 registered-voter count.

### "Rapid partisan convergence"

**SUPPORTED DESCRIPTIVELY**

The +21 Democratic margin in 2020 narrowing to +4 in 2024 supports this description.

Do not imply permanence from one election-to-election change.

---

# Denmark

## Source set

Primary:
- Harmon (2018), Scandinavian Journal of Economics.
- Dustmann, Vasiljeva & Damm (2019), Review of Economic Studies.

## Claims

### Increased local ethnic diversity shifted election outcomes rightward, 1981–2001

**CONFIRMED CAUSAL-STUDY CLAIM**

Harmon uses an IV strategy based on historical housing stock and reports shifts away from traditional big-government left parties toward anti-immigration nationalist parties.

Scope:
historical Danish municipalities, 1981–2001.

### Quasi-random refugee allocation increased anti-immigration/right vote outside the most urban municipalities

**CONFIRMED CAUSAL-STUDY CLAIM**

Dustmann et al. exploit quasi-random refugee assignment.

### Largest/most urban municipalities showed the opposite or no comparable anti-immigration shift

**CONFIRMED**

Directly stated in the published abstract.

### "Counter-mobilization is context-dependent"

**CONFIRMED AS SYNTHESIS**

Supported by the contrasting urban/non-urban effects.

### Applying the Denmark result to contemporary 2026 national politics

**NOT SUPPORTED**

The causal mechanism is historically credible, but current national magnitude/direction remains open.

Status:
**MECHANISM EVIDENCE ONLY**

---

# Italy

## Source set

Primary:
- European Journal of Political Economy (2023), *Italy: Immigration and the evolution of populism*.
- Regional Science Policy & Practice (2025), 2022 election spatial analysis.

## Claims

### Immigration caused increased Lega support in 2006–2018 municipality-level analysis

**CONFIRMED WITH DESIGN QUALIFICATION**

The EJPE paper uses an IV shift-share strategy and describes a sizable causal increase in Lega support.

### Effect stronger where fiscal autonomy was lower

**CONFIRMED**

Directly stated in the paper highlights.

### 2022 immigrant presence not uniformly associated with Lega/FdI support

**CONFIRMED**

The 2025 spatial study finds no significant or negative relationships across most of Italy, especially urban areas.

### Southern Italy exception for FdI

**CONFIRMED**

Higher immigrant shares were positively associated with FdI support in the South.

### "Historical counter-mobilization / current effect heterogeneous"

**CONFIRMED AS SYNTHESIS**

This is the appropriate current wording.

Do not say:
> immigration currently moves Italy right

---

# Cross-country methodological claims

## "Immigrant-origin electorates are not a single ideological bloc"

**CONFIRMED**

Strongly supported by Germany, Norway, Britain and the United States.

## "Left alignment exists in several receiving democracies but is not stable"

**CONFIRMED WITH QUALIFICATION**

Supported by Norway, Britain and U.S. temporal change; Sweden remains strong but exact 2026 cell values should be table-verified before final publication.

## "Direct and indirect effects can point in opposite directions"

**SUPPORTED AS A MECHANISM**

Direct-group voting evidence and Denmark/Italy counter-mobilization research justify separating the mechanisms.

Do not claim that both effects have been jointly estimated within the same election/country unless a specific study does so.

## "Turnout can matter as much as preference"

**TIGHTEN**

USA provides unusually strong evidence that turnout composition can dominate an observed aggregate shift.

"Can matter as much" is defensible as a possibility, but should not be universalized across all cases.

## "Outcome relevance is not causal decisiveness"

**CONFIRMED AS A METHODOLOGICAL RULE**

A contribution can be numerically large relative to a winning margin without being uniquely causal.

---

# Audit corrections required before DDR-01 v1.0

1. **Great Britain historical vote series**
   - quarantine current 2010–2024 percentage sequence;
   - rebuild from one consistent source family where possible.

2. **Great Britain DDR7 wording**
   - replace "locally decisive" with "locally material" unless a seat-level causal counterfactual is constructed.

3. **Sweden SCB values**
   - export and lock exact PxWeb cells for 2014, 2018, 2022 and 2026;
   - retain sampling margins where possible.

4. **Sweden new-citizen estimate**
   - label every 30k–35k reference as model-based / assumption-dependent.

5. **Norway 60k standardized net-vote estimate**
   - keep only as model-derived sensitivity analysis;
   - do not present as an observed vote count.

6. **Norway compositional-control result**
   - scope explicitly to the 2019–2023 local-election panel.

7. **Germany**
   - replace "origin matters more" with a narrower statement unless a formal multivariate comparison is obtained.

8. **Denmark / Italy**
   - keep historical causal evidence separate from claims about current national magnitude.

---

# Source-quality matrix

| Country | Strongest source type | Individual-level? | Causal? | Contemporary? | Main audit status |
|---|---|---:|---:|---:|---|
| Norway | Official election study + peer-reviewed panel | Yes | Partial/mechanism | Yes | Strong |
| Sweden | Official survey/time series | Yes | No | Yes | Strong descriptive; exact cells to lock |
| Germany | Official population stats + representative survey | Yes | No | Yes | Strong descriptive |
| Great Britain | Large survey + BES multivariate research | Yes | No | Yes | Strong, with one historical-series quarantine |
| United States | Validated-voter panel | Yes | Strong for turnout decomposition, not experimental | Yes | Very strong |
| Denmark | Peer-reviewed IV/quasi-random studies | Mostly aggregate/local | Yes | Historical | Strong mechanism, not current magnitude |
| Italy | Peer-reviewed IV + spatial studies | Aggregate/local | Historical causal + current association | Mixed | Strong mechanism, current heterogeneity |

---

# Overall audit result

**SOURCE BASE: ROBUST BUT UNEVEN**

Strongest current evidence:
- United States
- Norway
- Germany
- Great Britain
- Sweden

Strongest causal mechanism evidence:
- Denmark
- Italy

Main vulnerabilities:
- cross-country category non-equivalence;
- historical vs current evidence;
- model-derived outcome-relevance estimates;
- ecological inference at constituency/municipality level;
- one quarantined Great Britain historical vote series.

No major evidence failure invalidates DDR-01's mechanism-level conclusion.

However, the audit supports keeping status at:

**MECHANISM SUPPORTED / DIRECTION CONTEXT-DEPENDENT / CAUSAL MAGNITUDE UNRESOLVED**

Signal status:
**NOT A SIGNAL**

## Publication rule after this audit

Any public DDR-01 article should:
- distinguish source-reported facts from NPCsignals calculations;
- state the population definition for each country;
- state whether data are individual or ecological;
- label causal designs explicitly;
- retain null and non-comparable countries;
- avoid a universal left/right demographic narrative.

NPCsignals  
Observe → Filter → Validate → Stress → Archive → Review
