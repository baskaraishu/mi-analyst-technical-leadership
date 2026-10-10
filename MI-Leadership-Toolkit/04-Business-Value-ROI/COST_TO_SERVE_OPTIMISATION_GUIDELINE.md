# Cost-to-Serve / Compute Optimisation Guideline

> **Status:** Reusable guideline. This project runs locally on a very small synthetic dataset; it has no measured cloud cost and makes no savings claim. Template figures are blanks to fill with real measurements.

Optimise only after measuring, and never at the expense of controls: reconciliation, quality gating, auditability and traceability are not optional savings.

---

## 1. Principles

1. **Measure first.** Record run time, storage and effort before changing anything.
2. **Protect trust.** Do not remove validation, reconciliation or gate steps to save compute.
3. **Optimise value, not just cost.** Cost per *used* report matters more than cost per report.
4. **Make the trade-off visible.** State benefit, cost, risk and who agreed.
5. **Prove no regression.** Compare outputs before and after.

## 2. What to Measure

| Area | Measure | Source |
|---|---|---|
| Compute | Wall-clock time per stage and per run | `pipeline_summary.json` |
| Storage | Size of Bronze, Silver, quarantine, Gold and report folders per run | File system |
| Data volume | Input rows, columns, retained runs | Ingestion metadata |
| Effort | Analyst hours for run, review, investigation | Time log |
| Rework | Reruns due to blocked gate or source defects | Run history |
| Usage | Users, views, decisions supported | Report catalogue / feedback |

## 3. Cost-to-Serve Template

| Report | Frequency | Compute per run | Storage per run | Analyst hours per cycle | Rework per cycle | Estimated cost | Active users | Decisions supported | Cost per active user |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| | | | | | | | | | |

State the unit rates and assumptions used. Leave unknown values blank rather than estimating without a basis.

## 4. Optimisation Options

| Option | Possible benefit | Control to keep | Check |
|---|---|---|---|
| Process only new or changed months | Less compute | Still reconcile the full reporting period | Totals match full run |
| Columnar storage (Parquet) for Gold | Smaller, faster | Schema documented | Values equal prior output |
| Run heavy profiling only when source changes | Less compute | Profile available when investigating a blocked gate | Gate evidence retained |
| Prune superseded run outputs | Lower storage | Keep runs needed for audit and release evidence | Retention rule applied |
| Cache reference data | Faster stages | Reference changes invalidate cache | Linked to change log |
| Fix defects at source | Less quarantine and rework | Needs data-owner action | Lower issue rate |
| Retire unused reports | Lower effort and storage | Follow the retirement playbook | Usage and dependencies checked |

## 5. Optimisation Decision Record

| Field | Entry |
|---|---|
| Proposal | |
| Baseline measurements (date / run) | |
| Expected benefit | |
| Risk to quality, audit or timeliness | |
| Tests and comparison evidence | |
| Approver | |
| Result after change | |
| Decision (Adopt / Reject / Revisit) | |

## 6. Guardrails

- Do not claim savings without before/after measurements on the same workload.
- Do not delete audit or release evidence to reduce storage.
- Route any change to rules, thresholds or definitions through the change log.
- In a cloud setting, add service-specific cost data (query bytes, storage tier, schedules) and agree budget alerts with the owner.

## 7. Review Cadence

Review quarterly alongside usage and ownership, and before adding a new report.
