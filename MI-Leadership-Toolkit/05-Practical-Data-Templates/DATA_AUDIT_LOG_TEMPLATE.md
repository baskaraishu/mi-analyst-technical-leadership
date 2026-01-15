# Data Audit Log – Manual Adjustments & Corrections

This template records **manual data changes** and significant one-off corrections made to MI datasets or KPI outputs.

> The aim is to ensure transparency, traceability, and regulatory defensibility for any non-automated data changes.

---

## 1. Audit Log Table Structure (Conceptual)

Use this structure in your warehouse or tracking tool (e.g., BigQuery table, SharePoint list, or ticketing system).

| Field | Description |
|-------|-------------|
| **Audit_ID** | Unique identifier for the adjustment (e.g., AUD-2026-001). |
| **Date_Logged** | When the adjustment was recorded. |
| **Logged_By** | Person who logged the adjustment (name/role). |
| **Dataset_Name** | Table/view/report impacted. |
| **KPI_Name** | Specific KPI(s) affected, if applicable. |
| **Adjustment_Type** | E.g., Backfill, Override, Exclusion, Reclassification. |
| **Adjustment_Detail** | Description of what was changed (plain language). |
| **Technical_Detail** | SQL / script / process used to make the change. |
| **Reason_For_Adjustment** | Business or technical rationale. |
| **Amount_or_Records_Affected** | Magnitude of change (e.g., rows updated, value delta). |
| **Approval_By** | Approver (name/role), if required. |
| **Effective_From / To** | Time period to which the change applies. |
| **Linked_Incident_or_RCA** | Reference to `ANOMALY_DETECTION_LOG` or `RCA` record. |
| **Reversibility** | How the change could be reversed, if needed. |

---

## 2. Example Record

| Field | Example |
|-------|---------|
| Audit_ID | AUD-2026-004 |
| Date_Logged | 2026-01-15 |
| Logged_By | MI Analyst – Revenue |
| Dataset_Name | `finance_mart.fact_revenue` |
| KPI_Name | "Total Monthly Revenue" |
| Adjustment_Type | Backfill |
| Adjustment_Detail | Backfilled missing revenue for 2025-12-31 due to late file from payment provider. |
| Technical_Detail | Re-ran ETL job `job_revenue_daily` for 2025-12-31 after file arrival; verified against Finance GL. |
| Reason_For_Adjustment | Ensure MI aligns with audited Finance figures; original run missed late-arriving data. |
| Amount_or_Records_Affected | +£125,000 revenue, 42 transactions added. |
| Approval_By | Finance Controller |
| Effective_From / To | 2025-12-31 / 2025-12-31 |
| Linked_Incident_or_RCA | DQ-2026-003 (Anomaly: Revenue below Finance) |
| Reversibility | Re-run job without late file (or remove impacted partition) if needed. |

---

## 3. Process Guidelines

1. **When to Log an Adjustment**
   - Manual backfills or corrections to production MI tables.  
   - One-off overrides / exclusions requested by Finance, Risk, or Compliance.  
   - Any fix that changes reported historical values for key KPIs.

2. **Approval & Segregation of Duties**
   - For Tier 1 KPIs, require approval from **data owner** or relevant senior stakeholder (e.g., Finance controller).  
   - Where possible, separate the person implementing the change from the approver.

3. **Reconciliation & Validation**
   - After applying the adjustment, validate that MI outputs reconcile with source-of-truth systems.  
   - Update relevant dashboards and, if necessary, re-issue packs with clear notes.

4. **Communication**
   - Inform impacted stakeholders (e.g., via pack notes or email) when adjustments materially change historical figures.  
   - Reference the **Audit_ID** so stakeholders can find more detail if needed.

---

## 4. Integration with Other MI Processes

- Link audit records to **Anomaly Detection** and **RCA** documents for a full chain of evidence.  
- Use the audit log to identify **recurring issues** that may justify upstream system or process changes.  
- Periodically review the log with Finance / Risk for control and compliance purposes.

By maintaining a robust Data Audit Log, the MI function shows that it treats data changes with the same seriousness as **financial journal entries or policy decisions**.