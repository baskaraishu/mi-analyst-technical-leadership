# ETL / ELT Pipeline Standards for MI

These standards define how we design, build, and maintain **data pipelines** that feed MI reporting and analytics. The goals are **reliability, transparency, and ease of change**.

> Apply these standards to all pipelines that populate MI datasets, particularly those used for Tier 1 and Tier 2 KPIs.

---

## 1. Naming Conventions

Consistent naming makes it easier for analysts and engineers to navigate the MI data landscape.

### 1.1 Database Objects

| Object Type | Convention | Example |
|-------------|------------|---------|
| Dataset / Schema | `domain_purpose` | `crypto_analytics`, `sales_mart` |
| Fact Tables | `fact_<subject>` | `fact_sales`, `fact_customer_events` |
| Dimension Tables | `dim_<subject>` | `dim_customer`, `dim_product` |
| Views (Semantic / MI) | `v_<purpose>` | `v_latest_crypto_prices`, `v_kpi_summary` |
| Staging Tables | `stg_<source>_<subject>` | `stg_billing_invoices`, `stg_crm_customers` |
| Audit / Metadata | `audit_<purpose>` | `audit_etl_jobs`, `audit_data_quality` |

### 1.2 Columns

- Use **snake_case**: `order_id`, `customer_segment`, `event_timestamp`.  
- Avoid ambiguous names: prefer `customer_id` over `id`.  
- Timestamps end with `_ts` or `_timestamp`, dates with `_date`.

---

## 2. Pipeline Design Principles

1. **Modular Steps**  
   - Separate extract, load, transform, and validate steps where possible.
   - Make each step idempotent (safe to re-run without duplicating data).

2. **Incremental Processing**  
   - Use **partitioned loads** (by date or surrogate key) rather than full reloads where feasible.
   - Track watermarks (last processed timestamp/ID) in an audit table.

3. **Data Quality by Design**  
   - Embed checks for nulls, duplicates, referential integrity, and ranges (`DATA_QUALITY_CHECKLIST`).
   - Fail fast on critical issues; log and flag warnings for non-critical ones.

4. **Observability**  
   - Log job start/end times, row counts, and error details to an **audit_etl_jobs** table.
   - Expose key metrics in a **Data Quality & Pipeline Health dashboard**.

5. **Documentation & Ownership**  
   - Each pipeline must have a clear **owner**, a short description, and a link to relevant KPIs.

---

## 3. ETL Job Metadata & Audit

### 3.1 Audit Table Structure (Example)

```sql
CREATE TABLE audit_etl_jobs (
  job_name STRING,
  execution_ts TIMESTAMP,
  status STRING,              -- SUCCESS / FAILED / PARTIAL
  records_processed INT64,
  records_inserted INT64,
  records_updated INT64,
  error_message STRING,
  started_at TIMESTAMP,
  finished_at TIMESTAMP
);
```

### 3.2 Logging Guidelines

- Log one row per job run (or per major task in orchestration frameworks like Airflow).  
- On failure, capture a **diagnostic error message** and a link to logs.  
- Retain sufficient history for trend analysis (at least 180 days for MI-critical jobs).

---

## 4. SQL Coding Standards

1. **Readable Queries**
   - Use **CTEs** (WITH clauses) to break complex logic into stages.  
   - Align keywords and indentation for readability.

2. **Deterministic Logic**
   - Avoid non-deterministic functions (e.g., random sampling) in production MI outputs.

3. **Safe Joins**
   - Always specify join types and conditions explicitly.  
   - For many-to-one joins, validate that the "one" side is unique to avoid duplication.

4. **Avoid SELECT *** in Production**
   - Explicitly list fields to protect against schema drift and unexpected column additions.

5. **Performance Consciousness**
   - Filter early, project only necessary columns, leverage partition pruning and clustering.

---

## 5. Error Handling & Retry

- Configure retries with **backoff** for transient issues (e.g., network glitch, temporary API failure).  
- Avoid infinite retries; escalate after defined attempts.

**Example Retry Policy (Conceptual):**
- Retry up to **3 times**, with **5-minute intervals**.  
- If still failing, mark job as **FAILED**, notify on-call MI/Engineering.

---

## 6. Security & Compliance in Pipelines

- Use **service accounts** for all automated jobs; no personal credentials.  
- Store secrets in a **secure vault** (e.g., Secret Manager), never in code or config files.  
- Apply minimum required permissions (least privilege) to service accounts.

---

## 7. Promotion & Change Management

- All pipeline code (SQL, Python, DAGs) must be in **version control** with pull requests and reviews.  
- Changes to Tier 1 KPI pipelines require:
  - Impact assessment (affected reports, KPIs).  
  - Stakeholder communication and planned deployment window.  
- Use environment separation: **dev → test → prod**, with clear promotion criteria.

---

## 8. Alignment with MI Strategy

These standards support the MI objectives of:

- **Trust** – Pipelines produce accurate, reconciled data.  
- **Timeliness** – Data is available when needed for decision forums.  
- **Transparency** – Logic is visible, reviewable, and owned.  
- **Resilience** – Failures are detectable, diagnosable, and recoverable.

By adhering to common ETL/ELT standards, the MI function can grow the platform **without sacrificing quality or control**.