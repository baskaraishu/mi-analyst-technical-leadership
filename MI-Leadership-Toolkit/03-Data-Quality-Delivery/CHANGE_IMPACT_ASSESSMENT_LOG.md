# Change Management & Impact Assessment (Change Request Log)

> **Status:** Reusable, implementation-neutral template. The example entry is hypothetical, not a record of an approved change. File names are placeholders: map them to where your pipeline keeps rules and thresholds.

Use this log for any change to KPI definitions, validation rules, quality thresholds, cleaning policies, reference data, source feeds or published outputs. Changes should be traceable, reviewed and tested.

---

## 1. Change Process

1. **Raise** the request in the log.
2. **Assess impact** using section 2.
3. **Classify** risk: Low, Medium or High.
4. **Approve** by risk (Report Owner for definitions; MI Lead for rules and thresholds; both for High).
5. **Test** — update or add pytest cases, run affected stages, compare with the previous run.
6. **Release** with an effective date and run reference.
7. **Communicate** to affected users, including any break in comparability.
8. **Review** after release; close or roll back.

## 2. Impact Assessment Checklist

| Question | Assessment |
|---|---|
| Which KPIs, rules or outputs change? | |
| Does it alter historic comparability? Restate or annotate? | |
| Which reports, users and extracts are affected? | |
| Does it change quality-gate outcomes or DQ scores? | |
| Which files change? (e.g., validation code, configuration or threshold files, KPI definitions, data dictionary) | |
| Are documentation and assumptions updated? | |
| What tests prove it works, and what could regress? | |
| What is the rollback route? | |
| Does it introduce unvalidated measures or unsupported claims? | |

## 3. Risk Classification

| Level | Examples | Approval |
|---|---|---|
| Low | Wording, documentation, formatting | Analyst with peer review |
| Medium | New or adjusted validation rule, report layout, new field | MI Lead |
| High | KPI formula or definition, gate threshold, source change, retirement | Report Owner and MI Lead |

## 4. Change Request Log

| ID | Raised | Requester | Description | Reason | Files / outputs affected | Impact summary | Risk | Approver(s) | Tests / evidence | Effective | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CR-001 | YYYY-MM-DD | | *Example:* add a configured consistency rule so the Consistency dimension can be scored | Dimension currently not available | Validation rule configuration, `tests/` | DQ score may change; some records may newly fail | Medium | | New tests; before/after run comparison | | Proposed |

**Status values:** Proposed · Under assessment · Approved · Rejected · Testing · Released · Rolled back · Closed.

## 5. Before/After Comparison Record

| Measure | Previous run | New run | Difference | Explained by change? |
|---|---:|---:|---:|---|
| Input rows | | | | |
| Eligible / quarantined / duplicate-held | | | | |
| Overall DQ score | | | | |
| Gate decision | | | | |
| KPI results affected | | | | |

An unexplained difference blocks release until investigated.

## 6. Communication Template

> **Change:** [what changed]  
> **Effective:** [date / run ID]  
> **Why:** [reason]  
> **Impact:** [reports affected; any comparability break]  
> **Action needed:** [if any]  
> **Contact:** [name]
