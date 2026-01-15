# Data Dictionary Governance – Single Source of Truth

A well-governed **Data Dictionary** is the backbone of a credible MI function. It defines **what each metric means**, **how it is calculated**, and **who owns it**, ensuring that the entire organisation speaks the same numerical language.

This document outlines how we **create, maintain, and govern** our Data Dictionary so that it remains a **single source of truth** for KPIs, attributes, and reference data.

---

## 1. Purpose & Scope

**Purpose**
- Provide clear, consistent definitions for **all critical KPIs and data elements** used in MI reporting and analytics.
- Reduce ambiguity, duplicate logic, and “multiple versions of the truth”.
- Enable faster onboarding of analysts and smoother collaboration across teams.

**Scope**
- Tier 1: Executive KPIs (Board / ExCo level)
- Tier 2: Operational KPIs (function-level performance)
- Tier 3: Supporting attributes and reference data (dimensions, statuses, codes)

The Data Dictionary **does not** attempt to catalogue every field in every source system; it focuses on **business-relevant concepts** used in MI.

---

## 2. Governance Model

### 2.1 Roles & Responsibilities

| Role | Responsibilities |
|------|------------------|
| **Data Owner** (Business Lead) | Ultimately accountable for KPI definition, target setting, and business usage. Signs off on changes. |
| **Data Steward** (MI / Analytics) | Maintains dictionary entries, coordinates impact analysis, ensures alignment across reports. |
| **MI Engineering / Data Platform** | Ensures technical implementation (views, models, metrics layer) matches dictionary definitions. |
| **Data Governance Council** | Arbitrates conflicts, approves Tier 1 KPI changes, sets standards and policies. |

### 2.2 Change Control

All **Tier 1 and Tier 2 KPI definitions** must follow a simple but formal change process:

1. **Request** – Change raised via ticket or governance form (new KPI, definition change, deprecation).
2. **Impact Assessment** – Steward + Engineering assess:
   - Affected dashboards, reports, and downstream models.
   - Data availability and quality.
3. **Review & Approval** – Data Owner and, for Tier 1, Governance Council sign off.
4. **Implementation** – MI Engineering updates code (SQL, models, metrics layer) and tests.
5. **Communication** – Change log updated; stakeholders and report owners notified.

---

## 3. Standard Dictionary Fields

Each entry in the Data Dictionary must include **at least** the following fields:

| Field | Description |
|-------|-------------|
| **Business Name** | Human-friendly name (e.g., "Monthly Active Customers"). |
| **Technical Name** | Column / metric name in the data model (e.g., `monthly_active_customers`). |
| **Tier** | 1 = Executive, 2 = Operational, 3 = Supporting. |
| **Business Definition** | Clear explanation in plain language, including inclusions and exclusions. |
| **Calculation Logic** | Pseudo-code or SQL expression. For complex KPIs, link to code repository. |
| **Aggregation Grain** | At what level the KPI is typically reported (e.g., daily by channel, monthly by segment). |
| **Data Sources** | Systems and tables involved (e.g., CRM, Billing, Web Analytics). |
| **Data Owner** | Business owner accountable for the KPI. |
| **MI Steward** | MI analyst responsible for maintenance and documentation. |
| **Refresh Frequency** | Real-time, hourly, daily, monthly, etc. |
| **Valid From / To** | Period during which definition is valid (supporting historical changes). |
| **Related KPIs** | Linked metrics (e.g., Churn Rate related to Retention Rate, Net Adds). |

---

## 4. Example Dictionary Entry (Template)

```text
Business Name       : Monthly Customer Churn Rate
Technical Name      : churn_rate_monthly
Tier                : 1 (Executive)

Business Definition :
  Percentage of active subscription customers at the start of a month
  who have churned by the end of that month.

Calculation Logic   :
  churn_rate_monthly = churned_customers / customers_at_start_of_month

  WHERE:
    customers_at_start_of_month =
      Count of customers with an active subscription on the first day of the month.

    churned_customers =
      Customers active at the start of the month who have no active
      subscription at the end of the month and no successful bill in the
      following 30 days.

Aggregation Grain   : Monthly, by business unit, product, and acquisition channel.

Data Sources        : `billing.subscription_status`, `crm.customer_master`
Data Owner          : Head of Customer Retention
MI Steward          : Senior MI Analyst – Retention Squad
Refresh Frequency   : Monthly (T+2 working days)
Valid From / To     : From 2026-01-01, supersedes previous definition `churn_rate_v1`.
Related KPIs        : Retention Rate, Net Subscriber Adds, Customer Lifetime Value (CLV)
```

---

## 5. Tooling & Implementation

To keep the Data Dictionary **live and integrated** with MI workflows:

- Store the dictionary in a **central, queryable store** (e.g., BigQuery table, data catalogue, or dedicated metadata tool).
- Surface key fields **directly inside BI tools** (metric descriptions, owners, refresh frequency).
- Link dictionary entries to **code repositories** (SQL models, dbt, or metrics layer) for traceability.
- Automate **checks** to ensure dictionary coverage for all Tier 1 KPIs.

Example storage pattern in a warehouse:

```sql
CREATE TABLE metadata.kpi_dictionary (
  business_name STRING,
  technical_name STRING,
  tier INT64,
  business_definition STRING,
  calculation_logic STRING,
  aggregation_grain STRING,
  data_sources ARRAY<STRING>,
  data_owner STRING,
  mi_steward STRING,
  refresh_frequency STRING,
  valid_from DATE,
  valid_to DATE,
  related_kpis ARRAY<STRING>
);
```

---

## 6. Quality Measures for the Data Dictionary

To ensure the dictionary remains **useful and trusted**, track:

| KPI | Description |
|-----|-------------|
| **Dictionary_Coverage_Rate** | % of Tier 1 and Tier 2 KPIs in production that have complete dictionary entries. |
| **Definition_Consistency_Issues** | Number of detected conflicts (same KPI name, different logic across domains). |
| **Update_Latency** | Average time between approved definition change and dictionary update. |
| **Usage_Metrics** | How often the dictionary is accessed/viewed by MI and business users. |

---

## 7. Operating Principles

1. **No KPI Without a Definition**  
   - Any new KPI exposed to executives must have a Data Dictionary entry before go-live.

2. **Code Must Match the Dictionary**  
   - If implementation diverges from the definition, this is treated as a defect—not a documentation issue.

3. **Business Ownership, MI Stewardship**  
   - The business owns the meaning and target; MI owns implementation and documentation.

4. **Transparent History**  
   - Changes to definitions are versioned and justified; historical reports remain interpretable.

By enforcing **strong Data Dictionary governance**, the MI function ensures that **every number in a deck or dashboard is explainable, defensible, and aligned** across the organisation.