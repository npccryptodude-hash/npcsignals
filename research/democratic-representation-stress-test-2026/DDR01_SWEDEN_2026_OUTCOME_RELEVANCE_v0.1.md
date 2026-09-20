# DDR-01 Sweden 2026 — Outcome Relevance Pass v0.1

Status: FINAL / CERTIFIED RESULT  
Parent module: DDR-01 // Demographic Voting Alignment  
Purpose: Estimate whether immigrant-origin/new-citizen voting was electorally material in Sweden's 2026 Riksdag election without overstating causality.

## 1. National result anchor

The Swedish Election Authority formally established the Riksdag result on 19 Sep 2026.

Final turnout:
- 6,834,413 voters
- 84.9% turnout

Final seat allocation:
- S: 99
- C: 25
- V: 30
- MP: 22
- M: 70
- SD: 62
- KD: 22
- L: 19

Grouped descriptively:
- S + C + V + MP: 176 seats
- M + SD + KD + L: 173 seats

Final national vote shares:
- S 28.02%
- M 19.85%
- SD 17.48%
- V 8.40%
- C 7.03%
- KD 6.17%
- MP 6.12%
- L 5.34%
- other 1.58%

The result is now certified.

## 2. Best available new-citizen estimate

SVT Verifierar examined the narrower group of people who became Swedish citizens after the Tidö government took office in October 2022.

Method:
- citizenship counts from the Migration Agency;
- origin-region shares;
- SVT Valu 2026 voting patterns by origin region;
- assumed turnout of 60%.

SVT estimated:
- roughly 35,000 net votes in favour of the centre-left before adjusting for minors;
- roughly 30,000 net votes after an approximate age adjustment.

SVT explicitly described this as a hypothesis/estimate rather than empirical proof that the group decided the election.

## 3. Outcome relevance against the certified result

The original v0.1 sensitivity pass compared SVT's 30,000–35,000 estimate with the then-current preliminary bloc margin.

The certified result preserved the same narrow 176–173 seat split and a sub-1-percentage-point difference between the two descriptive party groupings.

Because the published national percentages are rounded and SVT's 30,000–35,000 figure is itself assumption-based, v1.0 does not lock a false-precision ratio between the estimate and the certified vote margin.

Interpretation:

The estimated contribution from new citizens is clearly large relative to the final-scale bloc margin. It is therefore reasonable to classify the group as **electorally material** under DDR7.

It is not sufficient to say that new citizens uniquely "decided" the election, because:
- the turnout assumption is estimated rather than observed for this exact subgroup;
- Valu voting patterns are applied from broader origin groups;
- newly naturalized citizens may differ from longer-established citizens of the same origin;
- the result is sensitive to assumptions about minors and participation;
- many other voter groups can also be shown to exceed a narrow winning margin.

## 4. Broader foreign-background electorate

A broader claim about all voters with foreign background cannot yet be estimated with the same precision.

Relevant evidence:
- SCB's 2026 Party Preference Survey showed a large left-green preference gap between foreign-background and Swedish-background respondents;
- SCB's 2022 turnout study found turnout of 67% among foreign-born voters versus 89% among native-born voters;
- turnout among native-born voters with two foreign-born parents was 77%;
- Reuters documented a sharp increase in turnout and centre-left support in several immigrant-dense districts in 2026.

These facts strongly support the existence of a demographic contribution, but a national net-vote figure for the entire foreign-background electorate requires:
1. exact 2026 eligible electorate by background;
2. 2026 turnout by background;
3. actual 2026 vote choice by background;
4. a common definition of "foreign background";
5. uncertainty bounds.

## 5. DDR7 classification

DDR7 — Outcome Relevance

**FINAL: MATERIAL, NOT CAUSALLY DECISIVE**

Rationale:
SVT's assumption-based estimate for newly naturalized citizens alone is 30,000–35,000 net votes toward the centre-left. The certified election remained narrowly divided at 176–173 seats. The estimate is therefore electorally material, but it does not establish unique causation or prove that this group alone determined the result.

## 6. Language lock

Allowed:
> Newly naturalized voters appear to have made a materially large contribution to the centre-left margin in Sweden's 2026 election.

Allowed:
> Under SVT's assumptions, the estimated net contribution from post-2022 new citizens was on the order of 30,000–35,000 votes in an election ultimately certified at 176–173 seats between the two descriptive party groupings.

Do not write:
> Immigrants decided the election.

Do not write:
> Citizenship policy caused the centre-left victory.

Neither stronger causal claim is established by the current evidence.

## 7. Certification lock

Certification condition satisfied on 19 Sep 2026.

DDR7 Sweden 2026 is now frozen for v1.0 as:
**MATERIAL, NOT CAUSALLY DECISIVE**

Any future update must be evidence-driven and versioned.

## Source anchors

- Swedish Election Authority / SVT election results, 2026 Riksdag.
- SVT Verifierar, "Avgjorde 200 000 nya medborgare valet?", 16 Sep 2026.
- SCB, Party Preference Survey, May 2026.
- SCB, voter-turnout analysis, 2022.
- Reuters, 17 Sep 2026, reporting on turnout and centre-left gains in immigrant-dense districts.

NPCsignals  
Observe → Filter → Validate → Stress → Archive → Review
