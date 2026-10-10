# MI Intervention Measurement & Learning Framework

Use this framework to evaluate whether a business action informed by MI achieved its intended outcome. It connects analysis and reporting to a documented decision, while avoiding unsupported claims that MI alone caused a result.

Apply it to interventions such as a process change, targeted campaign, operational alert, new dashboard-led review, or predictive insight. Scale the evaluation method to the decision's value, risk, and feasibility.

## 1. Frame the decision

Before analysis begins, agree:

- **Business problem:** What needs to change, for whom, and why now?
- **Decision owner:** Who can approve or take the action?
- **Intended action:** What will the team do differently when evidence supports it?
- **Hypothesis:** What outcome is expected, for which population, and through what mechanism?
- **Scope:** Which teams, customers, products, locations, and time period are included?
- **Decision date:** When will the evidence be reviewed and a decision made?

Write the hypothesis in a testable form:

> For **[population]**, applying **[intervention]** is expected to change **[primary outcome]** by **[amount or direction]** within **[time period]**, without breaching **[guardrail]**.

If no decision or action could change based on the result, revisit whether the work is worth measuring.

## 2. Define measures and establish a baseline

Record measures before the intervention starts. Link KPI definitions to the governed Data Dictionary.

| Measure | Definition to agree |
|---|---|
| **Primary outcome** | The single main measure used to judge the intended business result; specify numerator, denominator, grain, exclusions, and source. |
| **Guardrails** | Measures that must not worsen materially, such as complaints, cost, service level, errors, or fairness across groups. |
| **Leading indicators** | Earlier signals that the proposed mechanism is working; do not substitute these for the business outcome. |
| **Baseline** | Pre-intervention value, population, and period; record seasonality or known events that affect comparability. |
| **Value measure** | Agreed financial or operational translation, including assumptions, costs, and whether the benefit is realised, annualised, or estimated. |

Capture the baseline query or report version, extraction date, filters, and data-quality checks so another analyst can reproduce it. Confirm that the data is sufficiently complete, timely, and comparable before using it to support a decision.

## 3. Choose an evaluation design

Choose the strongest feasible design for the decision and record why it is appropriate.

| Design | When it can be useful | Key limitation to document |
|---|---|---|
| **Randomised A/B test** | Eligible units can be assigned to intervention and comparison groups without unacceptable risk or unfairness. | Contamination, non-compliance, sample size, or differences between assigned and actual exposure. |
| **Phased rollout** | An intervention must be introduced gradually across teams, sites, or time periods. | Rollout order and timing may correlate with readiness or expected outcomes. |
| **Matched comparison** | Randomisation is not feasible, but similar untreated units can be identified. | Matching only controls for observed characteristics; unobserved differences may remain. |
| **Interrupted time series** | A clear intervention date and sufficient consistent observations exist before and after it. | Seasonality, concurrent changes, and underlying trends can explain some or all of the movement. |
| **Pre/post monitoring** | A quick operational read is needed or a credible comparison is unavailable. | A change after launch is not, by itself, evidence the intervention caused the change. |

Do not imply causation from a simple before-and-after comparison. Where the design cannot isolate the intervention's effect, describe the result as an observed change or association and state plausible alternative explanations.

## 4. Plan the evaluation

Before launch, document:

- **Unit of analysis:** Customer, transaction, team, site, or time period; ensure this matches the intervention and KPI grain.
- **Exposure:** How and when a unit counts as receiving the intervention.
- **Comparison:** Who or what provides the counterfactual, and how comparability will be assessed.
- **Observation window:** Allow enough time for the outcome to respond; include relevant seasonal cycles where possible.
- **Decision rule:** What size and confidence of improvement would justify scaling, adapting, or stopping? Include guardrail thresholds.
- **Risks and confounders:** Concurrent campaigns, policy or system changes, seasonality, missing data, selection effects, and spillover between groups.
- **Analysis plan:** Define calculations, exclusions, segment cuts, and treatment of missing or late-arriving data before reviewing outcomes.
- **Ownership:** Name the intervention owner, analyst, data owner, and approver.

For tests with limited samples or noisy outcomes, agree in advance how uncertainty will be presented. Avoid treating a small numerical movement as meaningful without considering variability, practical importance, and the quality of the comparison.

## 5. Validate and analyse

1. Re-run the baseline and intervention-period extracts from documented sources and code.
2. Check completeness, freshness, duplicates, population changes, and reconciliation against relevant source systems.
3. Confirm that exposure and comparison groups were formed as planned; record deviations.
4. Compare the primary outcome and guardrails for the agreed periods and segments.
5. Quantify the observed difference and uncertainty using a method appropriate to the design and data.
6. Check whether the result persists across sensible sensitivity checks, such as alternate time windows or exclusions agreed in advance.
7. Separate measured results from estimated financial translation; show assumptions, intervention costs, and any uncertainty.

If data quality or design limitations undermine the comparison, report that limitation plainly and avoid presenting the result as a reliable effect estimate.

## 6. Make and record the decision

Use the agreed decision rule to choose one of the following:

- **Scale** – evidence and guardrails support wider rollout.
- **Adapt and re-evaluate** – the approach is promising, but the design, execution, or outcome needs improvement.
- **Stop** – the intended benefit was not supported, costs outweigh value, or a guardrail was breached.
- **Continue monitoring** – the observation period or evidence is not yet sufficient.

Record the decision owner, rationale, actions, due dates, unresolved risks, and next review date. Communicate the result in business language, distinguishing:

- what changed;
- what the evaluation can and cannot attribute to the intervention;
- the operational or financial value and how it was calculated; and
- what action follows.

## 7. Capture learning and make it reusable

Store the evaluation brief, approved KPI definitions, query or analysis version, validation evidence, decision record, and follow-up results together or cross-linked from the relevant MI catalogue and incident/change records.

After the follow-up period:

- compare realised outcomes with the original decision rule and value estimate;
- record unintended impacts and lessons;
- update the KPI dictionary, dashboard, or monitoring rules if definitions or controls changed; and
- note what should be reused or changed in the next evaluation.

## Reusable evaluation brief

Copy and complete this section for each intervention.

| Field | Entry |
|---|---|
| Evaluation ID / version | |
| Business problem and scope | |
| Decision owner and intervention owner | |
| Hypothesis | |
| Intervention and launch date | |
| Target population and unit of analysis | |
| Primary outcome and KPI dictionary reference | |
| Guardrails and thresholds | |
| Baseline value, period, query/report version | |
| Evaluation design and rationale | |
| Comparison group or counterfactual | |
| Observation window and review date | |
| Decision rule agreed before launch | |
| Data-quality checks and result | |
| Confounders, risks, and deviations | |
| Outcome and uncertainty | |
| Value estimate, costs, and assumptions | |
| Decision: scale / adapt / stop / monitor | |
| Follow-up actions, owners, and dates | |
| Limitations and learning | |

## Worked example (illustrative only)

**Question:** Does a targeted onboarding intervention improve first-90-day customer retention without increasing complaints or service costs?

- Define the eligible new-customer population, retention KPI, complaint-rate and cost guardrails, and baseline before launch.
- If operationally and ethically feasible, randomly assign eligible customers to the existing onboarding journey or the new journey. Otherwise, use a phased rollout and document how sites or cohorts differ.
- Set the observation window and decision thresholds with the business owner before looking at results.
- Validate assignment, exposure, customer-status completeness, and KPI consistency; then compare retention and guardrails.
- Report the measured difference and uncertainty. If the evaluation is pre/post only, call it an observed change rather than attributing it solely to onboarding.
- Record whether to scale, adapt, stop, or gather more evidence, then check outcomes after rollout.

This example specifies a repeatable method; it does not claim that an intervention was run or achieved a particular result.
