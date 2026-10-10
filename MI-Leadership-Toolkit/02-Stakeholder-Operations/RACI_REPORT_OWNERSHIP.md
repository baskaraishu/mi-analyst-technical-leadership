# Stakeholder RACI Matrix Template: Report Ownership

> **Status:** Reusable, implementation-neutral template. Roles and assignments are illustrative; they are not an MoJ/HMPPS organisation chart. Agree real roles with the service before use. Evidence fields are placeholders: map them to your pipeline's own artefacts (for `MI-Technical-Project`: run logs, the data-quality report, `src/config.py` thresholds and the BigQuery destination table).

Clear ownership prevents a report being trusted by many and owned by no one. Use one RACI per report or data product.

**Key:** **R** Responsible (does the work) · **A** Accountable (one person who signs off) · **C** Consulted (before) · **I** Informed (after).

Rule: exactly **one A** per row; at least one **R**.

---

## 1. Report Register Entry

| Field | Entry |
|---|---|
| Report / data product | e.g., Monthly Establishment Performance KPI Pack |
| Purpose and decision supported | |
| Intended audience | |
| Frequency and publication date | |
| Source data and published output | e.g., source feed and destination table |
| KPI definitions reference | e.g., data dictionary or KPI definition document |
| Release control | e.g., quality-check configuration and recorded pass/fail decision |
| Review date | |

## 2. Roles

| Role | Typical responsibility | Named person / team |
|---|---|---|
| Report Owner (business) | Owns purpose, audience and continued need | |
| Data Owner | Owns source data accuracy and fixes at source | |
| MI / Performance Analyst | Builds, assures and publishes the report | |
| MI Lead / Manager | Approves release and quality exceptions | |
| Data Steward | Maintains definitions and rule changes | |
| Operational Manager (user) | Interprets results and decides follow-up | |
| Technical Support | Runs and maintains the pipeline | |

## 3. RACI Matrix

| Activity | Report Owner | Data Owner | Analyst | MI Lead | Data Steward | Ops Manager | Tech Support |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Define purpose and decisions supported | A | C | R | C | I | C | I |
| Agree KPI definitions and targets | A | C | R | C | R | C | I |
| Maintain data dictionary and rules | I | C | R | C | A | I | C |
| Supply and correct source data | I | A | C | I | C | I | I |
| Run pipeline and monitor stages | I | I | R | C | I | I | A |
| Investigate data-quality issues | I | A | R | C | C | I | C |
| Approve quality-gate exceptions | C | C | R | A | C | I | I |
| Review KPIs and exceptions | I | I | R | C | I | A | I |
| Decide operational follow-up | C | I | C | I | I | A | I |
| Publish and communicate report | A | I | R | C | I | I | C |
| Approve Low/Medium-risk changes (see change log) | C | C | R | A | C | C | C |
| Approve High-risk changes: business sign-off (see change log) | A | C | R | C | C | C | C |
| Approve High-risk changes: MI Lead sign-off (see change log) | I | C | R | A | C | C | C |
| Retire the report: business sign-off (see playbook) | A | C | R | C | C | C | C |
| Retire the report: MI Lead sign-off (see playbook) | I | C | R | A | C | C | C |

High-risk changes and retirements need **both** sign-offs, recorded as separate rows so each keeps one A.

Where one person holds several roles, record it and note the single-point-of-failure risk.

## 4. Escalation and Cover

| Situation | First contact | Escalate to | Timeframe |
|---|---|---|---|
| Gate blocked a scheduled release | Analyst | MI Lead, then Report Owner | |
| Source defect needs correction | Analyst | Data Owner | |
| Definition dispute | Data Steward | Report Owner | |
| Named owner unavailable | Deputy: | | |

## 5. Quality Checks

- [ ] One accountable person per activity.
- [ ] Named individuals or teams, not just job titles.
- [ ] Deputies recorded for each A.
- [ ] Owners have seen and accepted their role.
- [ ] Reviewed at least annually and after any restructure.

## 6. Sign-off

| Name | Role | Date |
|---|---|---|
| | | |
