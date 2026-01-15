# Anomaly Detection Log – Data Incidents Register

This log template is used to record **data anomalies and incidents** that impact MI outputs (e.g., unexpected spikes, drops, or missing data). It supports structured **triage, communication, and learning**.

> Treat this as the "MI incident log" for data quality events visible to business stakeholders.

---

## 1. Incident Header

| Field | Description |
|-------|-------------|
| **Incident ID** | Unique identifier (e.g., DQ-2026-001). |
| **Date Detected** | When the anomaly was first noticed. |
| **Detected By** | Person or monitoring system that raised the alert. |
| **Status** | Open / In Progress / Resolved / Closed. |
| **Severity** | Sev1 (Critical), Sev2 (High), Sev3 (Medium), Sev4 (Low). |
| **Affected Reports / Dashboards** | List of MI assets impacted. |
| **Affected KPIs** | Specific metrics that may be incorrect or missing. |

---

## 2. Anomaly Description

**2.1 Summary (1–2 sentences)**  
- Brief description of what looks wrong (e.g., "Daily revenue is 70% lower vs typical Mondays").

**2.2 Evidence**  
- Screenshots or links to dashboards where anomaly is seen.  
- SQL snippets or queries used to confirm the issue.  

**2.3 Impact Assessment (Initial)**

| Dimension | Notes |
|-----------|-------|
| Business Impact | Which decisions / meetings are affected? Revenue/cost at risk? |
| Time Window | From when to when is data unreliable? |
| Scope | Specific segments, regions, products, or channels affected? |

---

## 3. Detection & Monitoring

**3.1 Detection Method**

- [ ] Automated alert (threshold-based)  
- [ ] Automated alert (statistical / ML-based)  
- [ ] Manual observation by analyst  
- [ ] Stakeholder reported  

**3.2 Monitoring Query / Rule**

```sql
-- Example skeleton: detect abnormal drop in volume
SELECT
  event_date,
  metric_total,
  AVG(metric_total) OVER (
    ORDER BY event_date
    ROWS BETWEEN 7 PRECEDING AND 1 PRECEDING
  ) AS recent_avg
FROM `project.dataset.daily_metric`
WHERE event_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY);

-- Flag where metric_total < 0.5 * recent_avg
```

---

## 4. Root Cause Investigation (Summary)

**4.1 Suspected Cause Categories**

- [ ] Source System Issue (e.g., outage, delayed load)  
- [ ] ETL / Pipeline Failure (job error, missing partition)  
- [ ] Code / Logic Change (new transformation, refactor)  
- [ ] Upstream Data Model Change (schema drift, new field types)  
- [ ] Business Process Change (new product, changed workflow)  
- [ ] Other:  

**4.2 Investigation Notes**

- Key SQL queries and logs used.  
- Systems and teams involved.  
- What was ruled out and how.  

---

## 5. Resolution & Remediation

**5.1 Fix Applied**

- Technical fix (e.g., re-run job, backfill data, code change).  
- Temporary workaround (e.g., manual adjustment, caveat in reports).  

**5.2 Data Correction**

- Periods backfilled:  
- Manual data adjustments logged in: `DATA_AUDIT_LOG` (if applicable).  

**5.3 Communication**

- Stakeholders informed: who, when, and via what channel (email, Teams, change note).  
- Message summary: what was wrong, which data to ignore or re-use, when it was fixed.  

---

## 6. Lessons Learned & Preventive Actions

**6.1 Lessons Learned**

- What could have detected this earlier?  
- What made this issue harder to diagnose?  

**6.2 Preventive Actions**

- New monitoring rules or alerts to add.  
- Changes to ETL standards or documentation.  
- Additional validations to add to `DATA_QUALITY_CHECKLIST`.  

---

## 7. Closure

| Field | Description |
|-------|-------------|
| **Date Resolved** | When the data was corrected and validated. |
| **Validated By** | Name/role confirming data is now correct. |
| **Residual Risk / Limitations** | Any remaining caveats (e.g., unrecoverable history). |

By maintaining a structured **Anomaly Detection Log**, the MI team builds organisational memory, improves detection over time, and demonstrates **professional incident management** for data quality issues.