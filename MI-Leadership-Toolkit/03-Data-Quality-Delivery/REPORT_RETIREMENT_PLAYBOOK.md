# Data Decommissioning & Report Retirement Playbook

> **Status:** Reusable playbook. Retention periods and approvals are placeholders; follow the organisation's records-management, security and legal requirements. It makes no decision about any real MoJ/HMPPS report.

Retire a report because it is no longer needed, duplicated or unsafe—not merely because usage is low. Low usage can mean an infrequent but critical decision, such as a quarterly assurance review.

---

## 1. Retirement Triggers

- The decision it supported no longer exists.
- Superseded by a governed replacement.
- Source system or data feed is ending.
- Persistent unresolved quality or definition problems.
- Duplicate of another report.
- Maintenance cost exceeds value, confirmed with the owner.

## 2. Process

| Step | Action | Output | Accountable |
|---|---|---|---|
| 1. Nominate | Record report, reason and proposed date | Retirement request | Analyst |
| 2. Assess usage | Review access and distribution over a full reporting cycle | Usage summary | Analyst |
| 3. Assess dependencies | Find downstream reports, extracts, spreadsheets, KPIs and audits relying on it | Dependency list | Analyst / Tech Support |
| 4. Consult | Ask users and data owner which decisions are affected and what alternative they need | Consultation record | Report Owner |
| 5. Decide | Approve, defer or reject, with conditions | Signed decision | Report Owner |
| 6. Communicate | Notify users with date, replacement and contact | Notice | Analyst |
| 7. Freeze | Stop refresh; label as retired; keep read access during grace period | Frozen report | Tech Support |
| 8. Archive | Preserve definitions, final outputs, run evidence and decision per retention rule | Archive record | Data Steward |
| 9. Remove | Withdraw access, schedules and unused storage after grace period | Removal confirmation | Tech Support |
| 10. Review | Confirm no unexpected requests; update catalogue and RACI | Closure note | MI Lead |

## 3. Pre-Retirement Checklist

- [ ] Report Owner approval recorded.
- [ ] Usage evidence covers at least one full reporting cycle.
- [ ] Dependencies identified and resolved or accepted.
- [ ] Replacement or alternative communicated, if any.
- [ ] Audit, legal and retention requirements checked.
- [ ] Sensitive data handling confirmed for archive and deletion.
- [ ] Grace period and rollback route agreed.
- [ ] Report catalogue and documentation updated.

## 4. Archive Contents

For a pipeline-based report such as this project, preserve as policy allows:

- Run ID, source hash and `pipeline_summary.json`.
- Quality-gate result and reconciliation summary.
- KPI mapping and rule versions used.
- Final Gold output or its documented location.
- Retirement decision and approvals.

## 5. Retirement Request Template

| Field | Entry |
|---|---|
| Report / data product | |
| Report Owner | |
| Reason for retirement | |
| Usage evidence (period and source) | |
| Dependencies found | |
| Users consulted and outcome | |
| Replacement / alternative | |
| Retention and archive location | |
| Proposed freeze / removal dates | |
| Risks and mitigations | |
| Decision (Approve / Defer / Reject) | |
| Approved by and date | |

## 6. Common Risks

| Risk | Mitigation |
|---|---|
| Hidden dependency on a spreadsheet or extract | Ask users directly; do not rely only on system lineage |
| Deleting evidence needed for audit | Check retention first; archive before removal |
| Users lose a needed measure | Provide replacement before freeze |
| Infrequent report mistaken as unused | Review usage across the full cycle |
| Retired report stays reachable and is reused | Label as retired; remove access after grace period |
