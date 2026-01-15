# BI Adoption & Usage Metrics

Delivering dashboards is not the goal; **driving sustained usage and decision impact** is. This document defines key metrics and patterns for measuring **BI adoption** across the organisation.

---

## 1. Objectives

- Understand **who is using MI assets**, how often, and for what.
- Identify underused or redundant reports for rationalisation.
- Target training and communication where adoption is low but potential value is high.

---

## 2. Core Adoption Metrics

### 2.1 User & Session Metrics

| Metric | Description | Example Target |
|--------|-------------|----------------|
| **Active_Users_Monthly** | Count of unique users accessing BI tools in the last 30 days. | Growing trend aligned with expansion of MI assets. |
| **Active_Users_By_Role** | Usage broken down by role (Exec, Manager, Analyst, Ops). | Coverage of key roles (e.g., 90% of managers active monthly). |
| **Sessions_Per_User** | Average number of sessions per active user. | ≥ 4 sessions/month for managers. |
| **Median_Session_Duration** | Typical time spent per session (excluding very short "bounces"). | 3–10 minutes, depending on use case. |

### 2.2 Report & Dashboard Metrics

| Metric | Description | Example Use |
|--------|-------------|-------------|
| **Report_Views_30D** | Number of views per report over 30 days. | Identify high-value vs low-usage content. |
| **Unique_Viewers_Per_Report** | Distinct users accessing a given report. | Detect "single-user" reports for potential consolidation. |
| **Reports_Unused_90D** | Count of reports with zero views over 90 days. | Candidates for deprecation. |
| **Certified_vs_Legacy_Usage** | Share of views on certified vs legacy reports. | Track migration from Excel/legacy packs to modern BI. |

---

## 3. Data Model for Adoption Tracking

Capture BI usage logs into a structured model in the warehouse.

### 3.1 Example Table Structure: `bi_usage_events`

```sql
CREATE TABLE analytics.bi_usage_events (
  event_ts TIMESTAMP,
  user_id STRING,
  user_role STRING,
  report_id STRING,
  report_title STRING,
  domain STRING,
  event_type STRING,  -- VIEW, EXPORT, FILTER_CHANGE, etc.
  session_id STRING
);
```

### 3.2 Derived Metrics Example

```sql
-- Active users in last 30 days
SELECT
  COUNT(DISTINCT user_id) AS active_users_30d
FROM analytics.bi_usage_events
WHERE event_ts >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY);

-- Reports unused in last 90 days
SELECT
  report_id,
  report_title
FROM analytics.report_catalog r
LEFT JOIN (
  SELECT DISTINCT report_id
  FROM analytics.bi_usage_events
  WHERE event_ts >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 90 DAY)
) u
ON r.report_id = u.report_id
WHERE u.report_id IS NULL;
```

---

## 4. Adoption Dashboard Design

An effective BI adoption dashboard should include:

1. **Executive Overview**
   - Total active users (monthly/quarterly).  
   - Usage by role (Exec, Manager, Analyst).  
   - Certified vs legacy usage.  

2. **Report Portfolio View**
   - Top 10 most-viewed reports.  
   - Reports with declining usage.  
   - Unused reports (>90 days).  

3. **Engagement Quality**
   - Median session duration.  
   - Repeat users vs one-off visitors.  
   - Exports/downloads of data.  

4. **Adoption by Domain / Function**
   - Usage heatmap across domains (Sales, Ops, Finance, etc.).  
   - Targeted opportunities for training and consolidation.

---

## 5. Targets & KPIs for BI Adoption

Suggested KPI set (to tailor per organisation):

| KPI | Definition | Owner |
|-----|------------|-------|
| **MI_Active_User_Rate** | Active BI users in last 30 days ÷ total eligible users. | MI Lead / Data Office |
| **Certified_Content_Share** | Views of certified reports ÷ total BI views. | MI Governance |
| **Report_Portfolio_Rationalisation** | % of reports with at least one view in last 90 days. | MI Lead |
| **Exec_Meeting_MI_Usage** | % of key exec forums using MI dashboards as primary source. | MI Business Partners |

---

## 6. Using Adoption Metrics in Practice

- **Rationalisation**: Use usage data to **retire or merge low-value reports**, simplifying the catalogue.  
- **Training & Change**: Target low-adoption areas with **data literacy initiatives** and champions.  
- **Product Management**: Treat major dashboards as **products** with roadmaps, feature requests, and satisfaction feedback.  
- **Storytelling**: Use adoption metrics in MI strategy updates to demonstrate **reach and influence**.

---

By tracking BI adoption systematically, the MI function moves from "deliver and forget" to **actively managing the value and lifecycle** of its reporting portfolio.