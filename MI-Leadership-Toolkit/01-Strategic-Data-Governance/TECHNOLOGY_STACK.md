# MI Technology Stack – Tools & Responsibilities

This document describes the **core technology stack** used by the MI function and how each tool contributes to delivering **trusted, scalable, and timely insight**.

The focus is on a modern cloud-based stack built around **SQL, Python, BigQuery, Looker Studio, and orchestration tooling (e.g., Airflow / GitHub Actions)**.

---

## 1. Architecture Overview

At a high level, the MI stack follows this flow:

```text
Source Systems → Ingestion & Storage → Transformation & Modelling → MI / BI Layer → Consumption
```

Typical components:

- **Source Systems** – CRM, billing, product/platform data, web analytics, operational systems.
- **Cloud Data Warehouse** – BigQuery (single source for MI-ready data).
- **Transformation Layer** – SQL + Python (dbt or custom pipelines) implementing business logic.
- **Orchestration** – Airflow, GitHub Actions, or similar for scheduling and dependency management.
- **BI / Visualisation** – Looker Studio, Power BI, or similar tools for dashboards and reports.
- **Metadata & Governance** – Data catalogue, KPI dictionary, access control and monitoring.

---

## 2. Core Tools and Their Roles

### 2.1 SQL – The Language of MI Logic

**Purpose**
- Define data models, KPIs, and aggregations in a **transparent, reviewable** manner.

**Usage Patterns**
- Building **fact** and **dimension** tables (e.g., `fact_sales`, `dim_customer`).
- Implementing KPI logic and views (e.g., `v_latest_crypto_prices`, `v_daily_kpi_summary`).
- Performing ad-hoc investigations and reconciliations.

**Good Practices**
- Use consistent naming conventions (`snake_case`, `dim_`, `fact_`, `v_`).
- Store all production SQL in **version control** (Git) with peer review.
- Prefer **set-based** logic over procedural/row-by-row operations.

---

### 2.2 Python – Automation, Data Quality, and Advanced Analytics

**Purpose**
- Orchestrate ETL/ELT workflows, perform complex transformations, integrate with APIs, and enable data science use cases.

**Usage Patterns**
- Ingestion from APIs (e.g., CoinGecko, third-party providers).
- Data quality checks (nulls, ranges, anomalies) as part of pipelines.
- Feature engineering and model scoring (e.g., churn, propensity models).

**Good Practices**
- Structure code into **modules** (e.g., `data_fetcher.py`, `data_quality.py`, `bigquery_loader.py`).
- Use **environment variables** for secrets and configuration.
- Package repeatable code for reuse across pipelines.

---

### 2.3 BigQuery – Cloud Data Warehouse

**Purpose**
- Provide a **single, scalable repository** for MI data, designed for analytical workloads.

**Usage Patterns**
- Store curated datasets (e.g., `crypto_analytics.crypto_prices`).
- Partition and cluster tables for performance and cost efficiency.
- Implement semantic views for MI (e.g., `v_latest_crypto_prices`, `v_daily_price_summary`).

**Good Practices**
- Partition large tables by **date** (`extraction_timestamp`, `event_date`).
- Cluster by common filter keys (`customer_id`, `crypto_id`).
- Use **views** to encapsulate KPI logic and simplify BI connections.
- Implement **row-level and column-level security** where needed.

---

### 2.4 Looker Studio (or Similar BI Tool)

**Purpose**
- Deliver **interactive dashboards and reports** to business stakeholders.

**Usage Patterns**
- Connect directly to BigQuery views and curated tables.
- Build thematic dashboards (e.g., Executive Overview, Operations, Retention).
- Embed metric descriptions and references to Data Dictionary.

**Good Practices**
- Treat dashboards as **products**: define audience, purpose, and refresh cadence.
- Minimise complex logic in BI; push calculations into BigQuery views where possible.
- Use consistent colour palettes, naming, and layouts across MI assets.

---

### 2.5 Orchestration – Airflow / GitHub Actions

**Purpose**
- Ensure **reliable, repeatable** execution of data pipelines and MI refresh processes.

**Usage Patterns**
- Schedule daily ETL jobs (e.g., crypto price ingestion at 06:00 UTC).
- Define dependencies between tasks (extract → transform → quality checks → load).
- Capture logs and metrics for monitoring and incident response.

**Good Practices**
- Treat pipelines as code (DAGs / workflows defined in version control).
- Implement **retry policies** and **alerting** for failures.
- Keep jobs small and composable (extract, transform, load, validate as separate tasks).

---

## 3. RACI – Who Owns What?

| Component | Primary Owner | Supporting Roles |
|----------|---------------|------------------|
| **SQL Models & Views** | MI Engineering / Analytics Engineer | MI Analysts, Data Modeller |
| **Python ETL Pipelines** | Data Engineering / Analytics Engineer | MI Analysts (requirements), DevOps |
| **BigQuery Datasets** | Data Platform / MI Team | Security, Infrastructure |
| **BI Dashboards** | MI Analysts / Product Owners | Business Stakeholders, UX |
| **Orchestration Workflows** | Data Engineering / Platform | MI Ops, DevOps |
| **Data Dictionary & KPI Definitions** | Data Owners (Business) | MI Stewards, Governance Council |

---

## 4. Non-Functional Requirements

Regardless of tool, the MI stack must meet the following **non-functional** criteria:

- **Reliability** – Pipelines complete on time; dashboards are refreshed as per SLA.
- **Scalability** – Can handle growth in data volume and user base without major redesign.
- **Security & Compliance** – Access controls, encryption, and audit logging in place.
- **Cost Efficiency** – Queries and storage optimised; unnecessary processing avoided.
- **Observability** – Monitoring for data quality, pipeline health, and user adoption.

---

## 5. Technology Roadmap (Example)

Short- to medium-term improvements to the MI stack might include:

- Introduce a **metrics layer** (e.g., dbt metrics or dedicated semantic layer) to centralise KPI logic.
- Implement a **data catalogue** with lineage and business definitions surfaced in BI tools.
- Add **automated anomaly detection** on key KPIs using Python-based models.
- Migrate remaining Excel-based critical reports onto the **cloud BI platform**.

---

By clearly articulating the MI Technology Stack, we demonstrate that our insights are built on a **robust, governed, and scalable foundation**, aligning technical choices with business needs and MI strategy.