# DDR-01 Compositional-Control Pass v0.1

Status: FIRST CONTROL PASS COMPLETE  
Method status: FROZEN v0.1  
Signal status: NOT A SIGNAL

## Purpose

This pass tests whether the top-level variable "immigrant-origin / minority background" still explains voting behaviour after accounting for other characteristics such as:

- age
- education
- income / class
- religion
- urbanization / geography
- origin region
- generation

The question is not whether demographic background correlates with vote choice. That is already established in several countries.

The question is whether the broad category retains explanatory value once composition is taken seriously.

---

# Norway

## Best evidence

Bergh & Kleven (2026), using high-quality panel data from the 2019 and 2023 Norwegian local elections, directly test the move toward centre-right parties among non-Western immigrant-background voters.

Their multivariate models include:
- gender
- age
- age squared
- higher education
- religion
- religious attendance
- political attitudes
- prior vote in the panel model

Key result:
The usual social-background controls — gender, age and education — did not explain the shift toward centre-right voting.

Religion mattered:
- Muslim respondents were significantly less likely to vote for centre-right parties.
- Religiosity itself provided only limited explanatory power for the aggregate rightward movement.

The authors also found that immigrant-background voters could hold relatively right-leaning issue positions even when voting for centre-left parties.

## Norway verdict

**THE OBSERVED RIGHTWARD SHIFT IN THE NORWEGIAN PANEL IS NOT EXPLAINED AWAY BY BASIC AGE/GENDER/EDUCATION CONTROLS; RELIGION AND POLITICAL ATTITUDES MODIFY THE PATTERN.**

This is evidence against a pure compositional explanation based only on age and education.

However, "immigrant background" remains too broad because origin and religion matter substantially.

Classification:
**RESIDUAL GROUP EFFECT / COMPOSITION PARTIAL**

---

# Great Britain

## Long-run multivariate evidence

A British Election Study analysis covering general elections from 1983–2019 regresses Labour vote choice on multiple social-group memberships.

Controls include:
- ethnicity
- class
- region
- religion
- education
- sex
- other group variables

Result:
Ethnicity remained a statistically and substantively significant predictor of Labour voting.

Holding other variables constant, the odds of South Asian and Black respondents voting Labour were roughly 4:1 across elections.

The analysis also finds that class and region declined in importance over time, while ethnic-minority groups became increasingly important components of Labour's coalition.

## 2024 evidence

The 2024 minority-voter evidence shows substantial fragmentation by:
- religion
- ancestry
- education
- local issue salience

Among ethnic-minority voters, higher education was associated with somewhat higher Conservative support:
- above degree level: Conservative 23%
- below degree level: Conservative 17%

Yet Labour still led strongly in both education categories.

## Great Britain verdict

**ETHNICITY RETAINS AN INDEPENDENT PREDICTIVE ASSOCIATION IN LONG-RUN MULTIVARIATE MODELS, BUT RELIGION, EDUCATION AND SUBGROUP IDENTITY MODIFY THE PATTERN.**

The broad category is not fully accounted for by class or education in these models. This is an adjusted association, not a causal estimate.

Classification:
**RESIDUAL ETHNIC EFFECT / STRONG SUBGROUP MODIFICATION**

---

# Sweden

## Available official evidence

SCB's Party Preference Survey publishes party preference separately by:
- foreign / Swedish background
- age
- education
- income
- region
- employment
- socioeconomic group
- other demographic variables

However, the public official tables are primarily cross-tabulations, not a published multivariate model estimating the independent effect of foreign background after simultaneously controlling for all covariates.

SCB also reports that uncertainty in party choice differs by:
- foreign-born status
- age
- sex
- education

This confirms that composition matters.

But it does not establish how much of the foreign-background party-preference gap remains after multivariate adjustment.

## Sweden verdict

**UNRESOLVED AFTER CONTROLS**

The raw foreign-background alignment is clear, but the current source set does not identify the residual independent effect after simultaneous controls.

Classification:
**DESCRIPTIVE GROUP EFFECT / MULTIVARIATE RESIDUAL UNKNOWN**

This is an important limitation and should remain visible.

---

# Germany

## Available evidence

The 2025 KAS study shows that broad migration-background categories mask large differences by origin.

It also reports that political attitudes on:
- taxation
- migration
- climate

differ by origin region and may help explain different party preferences.

Separate German voter-level work routinely includes migration background alongside:
- age
- gender
- education
- employment
- religion
- urbanity
- income / occupation

The current DDR-01 source set, however, does not yet provide one clean 2025 model that estimates the independent migration-background coefficient for overall party choice while simultaneously controlling for origin, class, religion and geography.

## Germany verdict

**BROAD MIGRATION-BACKGROUND STATUS IS TOO COARSE; ORIGIN AND ATTITUDES CARRY MUCH OF THE EXPLANATORY INFORMATION.**

This does not prove the broad variable has zero residual effect. It means the current evidence does not justify treating it as the principal explanatory variable.

Classification:
**COMPOSITION DOMINANT / RESIDUAL BROAD EFFECT UNRESOLVED**

---

# United States

## Composition differences

Naturalized eligible voters differ from U.S.-born eligible voters on several dimensions:
- older age profile
- somewhat higher bachelor-degree attainment
- somewhat higher median family income
- much lower English proficiency

These differences make raw nativity comparisons vulnerable to compositional confounding.

Historical Census regression work on turnout finds that naturalized citizens remained less likely to register and vote than native-born citizens even after controlling for:
- education
- income
- employment
- home ownership
- age
- sex
- marital status
- race and other characteristics

So for participation, nativity retained an independent association.

For 2024 party choice, Pew's validated-voter evidence clearly identifies the naturalized-citizen shift from 2020 to 2024 and decomposes turnout composition versus switching, but the current published DDR source set does not provide a full multivariate vote-choice model isolating nativity net of all socioeconomic controls.

## United States verdict

**NATIVITY RETAINS INDEPENDENT VALUE FOR TURNOUT; RESIDUAL EFFECT ON 2024 PARTY CHOICE IS NOT YET IDENTIFIED.**

Classification:
**PARTICIPATION EFFECT SURVIVES CONTROLS / PARTY-CHOICE EFFECT UNRESOLVED**

---

# Cross-country conclusion

The original possibility was:

> Perhaps "immigrant-origin" is mostly a proxy for age, education, class, religion and geography.

The evidence does not support a single answer.

### Clearly not fully explained by basic composition
- Norway: age, gender and education did not explain the rightward shift in the multivariate models.
- Great Britain: ethnicity remained a strong predictor of Labour vote after multiple social controls in long-run BES data.

### Broad category substantially decomposes into other variables
- Germany: origin group and political attitudes are more informative than the umbrella migration-background category.
- Great Britain 2024: religion and subgroup identity strongly modify the aggregate ethnic-minority pattern.

### Current evidence insufficient to isolate the residual
- Sweden: official cross-tabs are rich, but no equivalent multivariate residual estimate is currently in the source set.
- United States: party-choice shift is validated, but the residual nativity effect on party choice after socioeconomic controls is unresolved.

---

# Model decision

DDR-01 should **not** be replaced by a pure compositional-electorate model.

But it should be narrowed.

The best surviving model is:

> Immigrant-origin or minority background can retain independent electoral relevance in some systems, but the broad category is often only the first layer of explanation. Origin, religion, generation, turnout, geography, education and political attitudes frequently determine the direction and magnitude of the observed relationship.

This means:

**BROAD BACKGROUND EFFECT: PARTIALLY INDEPENDENT**  
**COMPOSITIONAL EFFECTS: SUBSTANTIAL**  
**SINGLE-CAUSE DEMOGRAPHIC MODEL: REJECTED**

---

# Updated DDR-01 conceptual structure

Layer 1 — Background
- immigrant origin
- ethnicity
- naturalization / nativity
- generation

Layer 2 — Composition
- age
- education
- income / class
- religion
- urbanization / geography
- employment

Layer 3 — Political mediation
- issue attitudes
- party supply
- candidate cues
- mobilization
- turnout

Layer 4 — Electoral translation
- party choice
- constituency concentration
- electoral system
- seat conversion

The research question therefore becomes:

> When does demographic background retain an independent relationship with voting after composition and political mediation are taken into account?

That is a stronger and more falsifiable question than asking simply whether immigrant-origin voters lean left or right.

---

# Status

**DDR-01 v0.1 SURVIVES, REFINED**

Current classification:

**BACKGROUND EFFECT PARTIALLY INDEPENDENT / COMPOSITION MATERIAL / DIRECTION CONTEXT-DEPENDENT**

Signal status:
**NOT A SIGNAL**

## Source anchors

- Bergh, J. & Kleven, Ø. (2026), "Social conservatism and changing party preferences among immigrants in Norway", Politics.
- British Election Study / Parliamentary Affairs, "Analysis of the Group Bases of British Politics: 1983–2019".
- UKICE / Focaldata, Minorities Report 2024.
- Statistics Sweden, Party Preference Survey 2026.
- Konrad-Adenauer-Stiftung, Voting behaviour of people with a migration background, 2025.
- Pew Research Center, naturalized-citizen electorate and validated-voter analysis, 2024–2025.
- U.S. Census Bureau, Voting Behavior of Naturalized Citizens working-paper series.

NPCsignals  
Observe → Filter → Validate → Stress → Archive → Review
