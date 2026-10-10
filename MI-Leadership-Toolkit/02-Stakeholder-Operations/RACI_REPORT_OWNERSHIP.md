# Stakeholder RACI Matrix Template: Report Ownership

> **Status:** Reusable template. Roles and assignments are illustrative for the synthetic-data project; they are not an MoJ/HMPPS organisation chart. Agree real roles with the service before use.

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
| Source data and Gold output | |
| KPI definitions reference | `rules/kpi_mappings.yml`, `docs/data_dictionary.md` |
| Release control | `rules/quality_gate.yml` decision recorded in `quality_gate.json` |
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
| Approve changes (see change log) | A | C | R | R | C | C | C |
| Retire the report (see playbook) | A | C | R | R | C | C | C |

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
