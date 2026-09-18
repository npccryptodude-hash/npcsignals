# NPCsignals — DDR-01 // Demographic Voting Alignment

Status: EXPLORATORY MODULE v0.1  
Parent project: Democratic Representation Stress Test 2026  
Core framework status: UNCHANGED / FROZEN  
Placement: Dimension VI — Polarization / Realignment  
Signal status: NOT A SIGNAL

## Research question

Do immigrant-origin and minority electorates show persistent party/bloc alignment, does that alignment weaken or strengthen over time, and can demographic change also produce counter-mobilization among other voters?

This module is deliberately separate from the Mandate Integrity Score (MIS). It does not alter any of the 90 MIS cases or the frozen 7-variable scoring framework.

## Why this module exists

The 2026 Swedish election raised a testable question. Reporting and official pre-election statistics indicate that voters with foreign background were substantially more supportive of the centre-left than the electorate as a whole, while turnout increased in several immigrant-dense districts. That does not establish that "immigrants decided the election." It does establish a measurable demographic voting pattern worth comparing across countries.

The module therefore separates two mechanisms:

1. **Direct alignment effect** — how immigrant-origin/minority voters themselves distribute across parties or blocs.
2. **Indirect electorate-response effect** — whether demographic change or immigration exposure shifts voting behaviour among the wider electorate.

These mechanisms can move in opposite directions.

## Guardrails

- No claim that a demographic group "caused" an election outcome without a counterfactual design.
- No treatment of immigrants, ethnic minorities, religious minorities, naturalized citizens or foreign-born citizens as interchangeable categories.
- Citizenship and voting-eligibility rules must be documented country by country.
- Turnout differences must be separated from vote-choice differences.
- Aggregate neighbourhood results must not be used as individual-level proof.
- Origin groups must be disaggregated where evidence shows materially different voting behaviour.
- A left/right label is used only where party-system comparison is defensible.
- Missing or legally unavailable ethnicity data must remain missing; no proxy construction from names, religion or neighbourhood without a validated research design.
- This is a realignment module, not a democratic-quality score.

## Variables

DDR1 — Eligible-electorate share  
Share of eligible national-election voters who are foreign-born, naturalized, immigrant-origin, or minority-background under the best country-specific definition available.

DDR2 — Turnout gap  
Difference in turnout between the focal group and the rest of the eligible electorate.

DDR3 — Party/bloc alignment  
Observed difference in party or bloc support between focal group and reference electorate.

DDR4 — Origin heterogeneity  
Whether different origin groups show materially different party preferences.

DDR5 — Alignment trajectory  
Whether the group-party relationship is strengthening, weakening or changing direction over time.

DDR6 — Counter-mobilization  
Evidence that immigration/demographic exposure changes voting behaviour among the wider electorate.

DDR7 — Outcome relevance  
Whether the estimated demographic-vote margin is large enough to be electorally material. This is descriptive only unless supported by a causal/counterfactual design.

## Evidence tiers

**A — Direct individual-level data**  
Official election study, validated-voter study or high-quality representative survey linking background to vote choice.

**B — Strong survey / subgroup evidence**  
Representative subgroup polling or repeated high-quality survey, but not validated vote records.

**C — Aggregate / ecological evidence**  
District-level demographic and election results. Useful for hypothesis generation, not individual inference.

**D — Insufficient / non-comparable**  
No robust comparable evidence located, or available categories do not measure immigrant-origin voting in a defensible way.

---

## Initial 15-country audit

### Norway — Tier A

Official Statistics Norway election research directly measures party choice and turnout by immigrant background.

2025:
- turnout among immigrants: 56%
- turnout among Norwegian-born with immigrant parents: 60%
- turnout among people without immigrant background: 83%
- Labour remained the largest party among voters with immigrant background
- voters with immigrant background still leaned more toward parties of the left and the Greens than other voters
- however, the Progress Party gained about 9 percentage points among immigrants overall
- among voters with Asian background, Labour fell about 10 points while the Progress Party gained about 12 points

Interpretation:
The historical left alignment remains visible, but the 2025 result provides direct evidence of weakening bloc uniformity and meaningful rightward movement among some origin groups.

Source:
Statistics Norway, "Immigrants and the General Election 2025" / Reports 2026/3.

Status:
**DIRECT ALIGNMENT CONFIRMED / ALIGNMENT WEAKENING / ORIGIN HETEROGENEITY IMPORTANT**

---

### Sweden — Tier A/B

Sweden has unusually useful official party-sympathy series by Swedish/foreign background from Statistics Sweden, extending from 2006 to 2026.

Pre-election 2026 SCB data continued to show markedly higher Social Democratic support among people with foreign background than among those with Swedish background. The series also shows meaningful support for parties on the right, demonstrating that the group is not politically uniform.

The 2026 election additionally produced strong aggregate evidence from immigrant-dense districts: turnout rose in several such areas and the centre-left gained heavily. Reuters documented Rinkeby as an extreme example. This ecological evidence supports, but does not independently prove, individual-level voting behaviour.

Interpretation:
Sweden is a strong longitudinal test case because both party alignment and turnout effects can be studied over time.

Status:
**DIRECT ALIGNMENT CONFIRMED / LONGITUDINAL SERIES AVAILABLE / 2026 OUTCOME RELEVANCE TO BE ESTIMATED CAUTIOUSLY**

---

### Denmark — Tier C for direct alignment; strong evidence for indirect effect

The strongest clean causal evidence located concerns the response of the wider electorate rather than immigrant voters themselves.

Harmon (Scandinavian Journal of Economics) studied Danish municipalities from 1981–2001 and found that increases in ethnic diversity produced rightward shifts in election outcomes, moving support away from traditional big-government left parties and toward anti-immigration nationalist parties.

Interpretation:
Denmark is the clearest current example in this module of why the direct and indirect mechanisms must be separated. Even if immigrant-origin voters lean one way, demographic change can shift other voters in the opposite direction.

Status:
**COUNTER-MOBILIZATION EVIDENCE STRONG / DIRECT IMMIGRANT-VOTE ESTIMATE STILL TO SOURCE**

---

### Germany — Tier B

A 2025 Konrad Adenauer Foundation representative study, designed for comparison with earlier studies since 2015, shows that "migrant background" is not one electoral bloc.

Key findings:
- CDU/CSU was the strongest force overall among Germans with and without migrant background in the study
- SPD was clearly strongest among respondents of Turkish and Russian origin
- the Left performed above average among Turkish- and Russian-origin respondents
- AfD led among respondents of Polish origin and ethnic-German late repatriates, followed by CDU/CSU
- voting patterns changed materially over the previous five years

Interpretation:
Germany directly falsifies a simple "immigrants vote left" rule. Origin composition matters substantially.

Status:
**ALIGNMENT HETEROGENEOUS / ORIGIN EFFECT STRONG / SIMPLE BLOC HYPOTHESIS REJECTED**

---

### United Kingdom — Tier B

Focaldata's large 2024 post-election analysis and subsequent minorities report show continued left-of-centre advantage among ethnic-minority voters, but with substantial internal fragmentation.

2024:
- combined Labour + Green + Liberal Democrat vote among ethnic minorities: about 66%
- Conservative + Reform UK: about 26%
- Labour support among Asian voters fell materially compared with 2019
- Muslim-heavy constituencies showed unusually large Labour losses
- Hindu-heavy constituencies showed relatively stronger Conservative performance

Interpretation:
A broad left advantage remained, but religion, ancestry and issue salience produced increasingly divergent subgroup behaviour.

Status:
**BROAD LEFT ALIGNMENT CONFIRMED / INTERNAL DIVERGENCE INCREASING**

---

### France — Tier D for directly comparable official ethnicity-vote data

France's official statistical system places strict legal constraints on ethnic-origin data. INSEE states that processing personal data revealing racial or ethnic origin is prohibited in administrative statistical systems under the constitutional/legal framework.

This does not make demographic voting research impossible, but it means France is not directly comparable to Norway or Sweden using official ethnic-background election tables.

Interpretation:
France should remain in the module, but private survey evidence must be assessed separately and cannot be treated as equivalent to official register/election-study data.

Status:
**OFFICIAL COMPARABILITY LIMITED / PRIVATE-SURVEY TRACK REQUIRED**

---

### Italy — Tier C/D for direct alignment; evidence for indirect effect

Robust evidence was located for the electoral response to immigration rather than direct voting by naturalized/immigrant-origin citizens.

A causal municipal-level study covering 2006–2018 found immigration exposure increased support for Lega and widened its advantage over competitors.

Interpretation:
Like Denmark, Italy currently contributes more strongly to DDR6 counter-mobilization than to DDR3 direct immigrant-origin party alignment.

Status:
**COUNTER-MOBILIZATION EVIDENCE / DIRECT ALIGNMENT INSUFFICIENT FOR CURRENT CROSS-COUNTRY ESTIMATE**

---

### Poland — Tier D

No sufficiently comparable, high-quality source has yet been located that permits a defensible national estimate of immigrant-origin vote choice analogous to Norway, Sweden, Germany, the UK or the US.

Status:
**INSUFFICIENT DATA — DO NOT INFER**

---

### United States — Tier A

Pew Research Center validated-voter analysis provides strong individual-level evidence for naturalized citizens.

2024 presidential election:
- Harris: 51%
- Trump: 47%

2020:
- Biden: 59%
- Trump: 38%

Subgroups shifted toward Trump between 2020 and 2024:
- White naturalized citizens: Trump 55% in 2024 vs 41% in 2020
- Hispanic naturalized citizens: 51% vs 39%
- Asian naturalized citizens: 46% vs 35%

Pew found the change was driven largely by turnout composition rather than mass individual switching.

Interpretation:
The US is a strong example of rapid erosion of a previously clearer Democratic advantage among naturalized citizens.

Status:
**DIRECT ALIGNMENT NEARLY EVEN BY 2024 / STRONG REALIGNMENT / TURNOUT COMPOSITION MATERIAL**

---

### Costa Rica — Tier D

No sufficiently comparable individual-level national evidence has yet been located linking immigrant/naturalized background to party vote choice with the precision required for this module.

Status:
**INSUFFICIENT DATA — DO NOT INFER**

---

### Chile — Tier D

No sufficiently comparable individual-level national evidence has yet been located linking immigrant/naturalized background to party vote choice with the precision required for this module.

Status:
**INSUFFICIENT DATA — DO NOT INFER**

---

### Ghana — Non-comparable track

Ghana should not be forced into an "immigrant-origin" framework where ethnicity, region and partisan history are more relevant cleavages.

Afrobarometer comparative work shows that ethnicity can matter for African voting intentions, but policy performance and economic evaluation can matter at least as much or more. This is not equivalent to immigrant-origin voting in European receiving states.

Status:
**SEPARATE ETHNIC/REGIONAL CLEAVAGE TRACK — NOT DIRECTLY COMPARABLE**

---

### Botswana — Non-comparable track

As with Ghana, ethnicity/region and long-run dominant-party politics are more relevant than immigrant-origin electorate analysis.

Afrobarometer provides extensive public-opinion and voting-participation data, but the current evidence set does not justify translating that into an immigrant-origin party-alignment measure.

Status:
**SEPARATE ETHNIC/REGIONAL CLEAVAGE TRACK — NOT DIRECTLY COMPARABLE**

---

### Japan — Tier D

No sufficiently robust national evidence has yet been located on party choice among naturalized/foreign-born Japanese citizens that is comparable with the A/B-tier countries.

Foreign residents without citizenship cannot vote in national elections, which further limits direct comparability.

Status:
**INSUFFICIENT DATA — DO NOT INFER**

---

### Thailand — Non-comparable track

Thailand's strongest documented demographic cleavages are regional, religious and urban/rural rather than immigrant-origin citizenship.

Research on the 2019 and 2023 elections shows substantial regional and religious differences in party choice, particularly between the North/Northeast and other regions. Those cleavages are analytically important but are not equivalent to immigrant-origin voting.

Status:
**SEPARATE REGIONAL/RELIGIOUS CLEAVAGE TRACK — NOT DIRECTLY COMPARABLE**

---

## Initial cross-country findings

### DDR-CF01 — Immigrant-origin electorates are not a single ideological bloc
**SUPPORTED**

Norway, Germany, the UK and the US all show substantial internal variation by origin, religion, generation or time.

### DDR-CF02 — Left alignment exists in several receiving democracies but is not stable
**SUPPORTED WITH QUALIFICATION**

Norway, Sweden and the UK show clear historical or current left-of-centre advantages among broad immigrant/minority electorates. The US naturalized electorate moved from a clear Democratic advantage in 2020 to near parity in 2024. Germany shows strong origin-specific divergence.

### DDR-CF03 — Demographic effects can run in opposite directions
**SUPPORTED AS A MECHANISM**

Direct minority/immigrant voting can favour one bloc while immigration exposure simultaneously shifts other voters toward another bloc. Denmark and Italy provide evidence for the second mechanism.

### DDR-CF04 — Turnout can matter as much as preference
**SUPPORTED**

Norway 2025 and the US 2024 both show that who turns out can materially change the observed political effect of demographic groups. Sweden 2026 requires explicit turnout decomposition before any outcome attribution.

### DDR-CF05 — "Immigrants decided the election" is usually too strong without counterfactual evidence
**SUPPORTED METHODOLOGICAL RULE**

A demographic group can contribute more votes to one bloc than another without being uniquely causal for the final result. Counterfactual claims require estimates of eligibility, turnout, vote choice, substitution and the rest of the electorate.

---

## Sweden 2026 specific test

The Swedish case should be decomposed into:

1. eligible voters with foreign background;
2. turnout by background;
3. party preference by background;
4. change from 2022;
5. estimated net bloc-vote contribution;
6. uncertainty interval;
7. comparison with final national bloc margin.

Only after those seven steps should the project assess whether the demographic contribution was electorally material.

The language should remain:

> Voters with foreign background appear to have contributed disproportionately to the centre-left vote margin.

Not:

> Immigrants decided the election.

unless a robust counterfactual analysis supports that stronger claim.

---

## Next research pass

Priority A:
- Sweden 2006–2026 SCB time series
- Norway 2005/2009–2025 SSB time series
- Germany 2015–2025 KAS repeated design
- UK 2010–2024 ethnic-minority vote series
- US 2008–2024 naturalized-citizen / ancestry trajectory

Priority B:
- Denmark direct immigrant-origin vote-choice evidence
- France high-quality private survey series
- Italy naturalized-citizen vote-choice evidence

Priority C:
- assess whether Poland, Costa Rica, Chile and Japan have enough comparable evidence to enter DDR3 at all
- keep Ghana, Botswana and Thailand on separate non-comparable cleavage tracks unless a defensible immigrant-origin measure is found

## Source anchors

- Statistics Norway (SSB), *Immigrants and the General Election 2025*, Reports 2026/3.
- Statistics Sweden (SCB), Party Preference Survey by Swedish/foreign background, 2006–2026.
- Reuters, 17 Sep 2026, reporting on turnout and centre-left gains in immigrant-dense Swedish districts.
- Konrad Adenauer Foundation, *Voting behaviour of people with a migration background*, 30 Sep 2025.
- Focaldata, *How Britain Voted 2024* and *Minorities Report*, 2024.
- Pew Research Center, *How voting patterns changed in the 2024 election*, 26 Jun 2025.
- Harmon, N.A., *Immigration, Ethnic Diversity, and Political Outcomes: Evidence from Denmark*, Scandinavian Journal of Economics.
- Barone et al./European Journal of Political Economy research on immigration and right-populist voting in Italy.
- INSEE, legal framework for ethnic-based statistics in France.
- Afrobarometer, comparative voting-intention and democracy datasets.
- Larsson & Thananithichot / Alexander, research on demographic and regional voting cleavages in Thailand.

NPCsignals  
Observe → Filter → Validate → Stress → Archive → Review
