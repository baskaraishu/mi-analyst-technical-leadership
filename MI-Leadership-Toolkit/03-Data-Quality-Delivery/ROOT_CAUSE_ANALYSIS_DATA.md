# Root Cause Analysis – Data Issues & "Numbers Don’t Look Right"

This template is used when stakeholders say **"the numbers don’t look right"** or when MI identifies discrepancies that require structured investigation.

> The goal is to move from subjective discomfort with numbers to a **clear, evidence-based root cause** and agreed corrective actions.

---

## 1. Issue Summary

| Field | Description |
|-------|-------------|
| **RCA ID** | Unique identifier (e.g., RCA-2026-004). |
| **Date Raised** | When the concern was raised. |
| **Raised By** | Stakeholder / team flagging the issue. |
| **MI Contact** | Lead analyst/engineer handling the RCA. |
| **Affected KPI(s)** | Names and technical codes. |
| **Affected Reports** | Dashboards / packs where issue was observed. |

**Issue Description (Stakeholder View):**  
- Capture the issue in the words of the stakeholder (e.g., "Churn looks too low compared to last month", "Sales don’t match Finance").

---

## 2. Initial Assessment

**2.1 Context & History**

- When was the issue first observed?  
- Did it coincide with any known business events (campaigns, system changes, seasonality)?  
- Has this issue occurred before?

**2.2 Initial Hypotheses**

List possible causes before deep analysis:

- [ ] Data quality issue (nulls, duplicates, missing days)  
- [ ] Source system change (new codes, new behaviour)  
- [ ] KPI definition misunderstanding (scope, filters, timing)  
- [ ] Pipeline failure or partial load  
- [ ] Legitimate business change  

---

## 3. Structured Investigation

### 3.1 Reproduce the Issue

- Recreate the exact view the stakeholder saw (filters, date range, segments).  
- Capture query and screenshot.

### 3.2 Sanity Checks

- Compare current period vs previous periods (YoY, MoM, WoW).  
- Check for missing dates or unusual gaps.

**Example SQL Skeleton:**

```sql
SELECT
  DATE(extraction_timestamp) AS dt,
  SUM(metric_value) AS metric_total
FROM `project.dataset.fact_kpi`
WHERE dt BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 60 DAY) AND CURRENT_DATE()
GROUP BY dt
ORDER BY dt;
```

### 3.3 Cross-System Reconciliation

Where relevant, reconcile against source-of-truth systems (e.g., Finance, CRM).

```sql
-- MI view
SELECT SUM(revenue) AS mi_revenue
FROM `project.dataset.fact_sales`
WHERE order_date BETWEEN '2026-01-01' AND '2026-01-31';

-- Finance ledger
SELECT SUM(gl_amount) AS finance_revenue
FROM `finance.gl_revenue`
WHERE gl_period = '2026-01';
```

Record variances and whether they are within agreed tolerance.

### 3.4 Definition & Filter Review

- Confirm KPI definition in the **Data Dictionary**.  
- Check for unexpected filters (e.g., excluding certain channels or segments).  
- Compare logic between old and new versions of reports if applicable.

---

## 4. Root Cause Determination

Summarise findings clearly:

**4.1 Root Cause Category**

- [ ] Data quality defect (missing/incorrect data)  
- [ ] Pipeline / ETL issue  
- [ ] KPI definition/logic issue  
- [ ] Business process/system change (numbers correct but expectation wrong)  
- [ ] User interpretation/training issue  
- [ ] Combination of the above  

**4.2 Root Cause Statement**  
- E.g., "KPI X dropped because a new product code was introduced in CRM but not mapped in the MI transformation, causing valid transactions to be excluded."

---

## 5. Corrective Actions

**5.1 Technical Fixes**

- Changes to ETL logic or mappings.  
- Backfills or data repairs.  
- New or updated data quality checks.  

**5.2 Process & Governance Fixes**

- Update to Data Dictionary definitions.  
- Changes to change-management process (e.g., involving MI earlier in system changes).  
- Additional training or documentation for stakeholders.

**5.3 Owner & Due Dates**

| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
|        |       |          |        |
|        |       |          |        |

---

## 6. Communication & Sign-Off

**6.1 Communication Summary**

- Who was informed of the root cause and fix?  
- Key messages sent to stakeholders:
  - What was wrong?  
  - What was impacted?  
  - What has been fixed?  
  - What still needs to be watched?  

**6.2 Stakeholder Acceptance**

- Business sponsor sign-off:  
- Date:  
- Notes (e.g., "Issue considered closed", "Residual risk accepted", "Follow-up review in 1 month").

---

## 7. Learning & Prevention

Capture learnings to reduce recurrence:

- What early-warning signal could have detected this earlier?  
- What dashboard/metric could be monitored to detect similar issues?
- Which MI or governance process needs strengthening?

> Over time, a library of RCA records becomes a powerful tool to **improve data governance, ETL standards, and stakeholder trust** in MI.