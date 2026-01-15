# Functional Data Testing – MI Data Quality Checklist

This checklist is designed for **Management Information (MI)** teams to ensure that data feeding dashboards, KPIs, and reports is **fit for decision-making**. It focuses on *functional data testing* across six dimensions:

1. **Schema & Types**  
2. **Nulls & Completeness**  
3. **Referential Integrity**  
4. **Business Rules**  
5. **Performance & Volumes**  
6. **Reconciliation & Auditability**

Each section includes: **Check Name**, **Description**, **Example SQL / Logic**, and **Owner** (who is accountable).

> Use this checklist as part of every MI pipeline deployment, data migration, or new KPI launch.

---

## 1. Schema & Types

Goal: Ensure that **tables, columns, and data types** match the expected design so downstream MI logic behaves predictably.

| Check Name | Description | Example SQL / Logic | Owner |
|------------|-------------|---------------------|-------|
| **Schema_Matches_Design** | Validate that all expected columns exist with correct data types (e.g., INT, STRING, TIMESTAMP). | ```sql
SELECT 
  column_name, data_type
FROM `project.dataset.INFORMATION_SCHEMA.COLUMNS`
WHERE table_name = 'fact_sales';
-- Compare vs. data model spec
``` | Engineering (with MI sign-off) |
| **Primary_Key_Defined** | Confirm primary key(s) are defined conceptually (even in warehouses without enforced PKs). | ```sql
SELECT
  COUNT(*) AS total_rows,
  COUNT(DISTINCT order_id) AS distinct_order_id
FROM `project.dataset.fact_sales`;
-- Expect total_rows = distinct_order_id
``` | MI / Data Modeller |
| **Enum_Values_Constrained** | Check that code/enum columns (e.g., status, channel) only contain expected values. | ```sql
SELECT DISTINCT order_status
FROM `project.dataset.fact_sales`
WHERE order_status NOT IN ('NEW','SHIPPED','CANCELLED','RETURNED');
-- Expect 0 rows
``` | MI (with Business SME) |
| **Timestamp_Fields_Valid** | Ensure date/timestamp fields are valid and parsable (no default/invalid dates). | ```sql
SELECT COUNT(*) AS invalid_dates
FROM `project.dataset.fact_sales`
WHERE order_date IS NULL 
   OR order_date < '2000-01-01' 
   OR order_date > CURRENT_DATE();
``` | Engineering |

---

## 2. Nulls & Completeness

Goal: Ensure that **critical fields are populated**, and overall completeness meets agreed thresholds.

| Check Name | Description | Example SQL / Logic | Owner |
|------------|-------------|---------------------|-------|
| **Critical_Columns_Not_Null** | Confirm that mandatory fields (e.g., `customer_id`, `order_date`, `revenue`) are non-null. | ```sql
SELECT 
  'customer_id' AS column_name,
  COUNTIF(customer_id IS NULL) AS null_count
FROM `project.dataset.fact_sales`
UNION ALL
SELECT 'order_date', COUNTIF(order_date IS NULL)
FROM `project.dataset.fact_sales`;
-- Expect 0 for critical columns
``` | MI / Engineering |
| **Null_Rate_Within_Threshold** | Measure null percentage for non-critical fields and compare to agreed thresholds. | ```sql
WITH stats AS (
  SELECT 
    COUNT(*) AS total_rows,
    COUNTIF(optional_field IS NULL) AS null_rows
  FROM `project.dataset.fact_sales`
)
SELECT 
  null_rows / total_rows * 100 AS null_pct
FROM stats;
-- Expect null_pct <= 5 (example)
``` | MI |
| **Daily_Load_Completeness** | Check that daily loads contain the expected number of records compared to historical patterns. | ```sql
SELECT 
  load_date,
  COUNT(*) AS row_count
FROM `project.dataset.fact_sales`
GROUP BY load_date
ORDER BY load_date DESC
LIMIT 14;
-- Compare today vs 7/14-day rolling average
``` | MI / Operations |
| **Source_To_Target_Record_Count** | Validate that full load or incremental load has not lost/gained unexpected rows. | ```sql
-- Source
SELECT COUNT(*) AS src_count FROM `source_sys.sales_orders`;
-- Target
SELECT COUNT(*) AS tgt_count FROM `project.dataset.fact_sales`;
-- Expect src_count ~ tgt_count (allowing for legitimate filters)
``` | Engineering |

---

## 3. Referential Integrity

Goal: Ensure that **relationships between tables are consistent**, so joins used in MI logic do not silently drop or duplicate data.

| Check Name | Description | Example SQL / Logic | Owner |
|------------|-------------|---------------------|-------|
| **Orphan_Fact_Records** | Check that all foreign keys in fact tables have a matching dimension record. | ```sql
SELECT COUNT(*) AS orphan_count
FROM `project.dataset.fact_sales` f
LEFT JOIN `project.dataset.dim_customer` c
  ON f.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
-- Expect orphan_count = 0 or within known tolerance
``` | Engineering / MI |
| **Many_To_One_Join_Integrity** | Confirm that dimension keys are unique to avoid unintentional data duplication in joins. | ```sql
SELECT 
  customer_id,
  COUNT(*) AS cnt
FROM `project.dataset.dim_customer`
GROUP BY customer_id
HAVING cnt > 1;
-- Expect 0 rows
``` | Engineering |
| **Lookup_Table_Coverage** | Validate that reference tables (e.g., `dim_channel`) cover all values used in facts. | ```sql
SELECT DISTINCT f.channel_code
FROM `project.dataset.fact_sales` f
LEFT JOIN `project.dataset.dim_channel` d
  ON f.channel_code = d.channel_code
WHERE d.channel_code IS NULL;
``` | MI / Business SME |
| **Date_Dimension_Continuity** | Ensure the date dimension covers all dates present in fact tables. | ```sql
SELECT DISTINCT f.order_date
FROM `project.dataset.fact_sales` f
LEFT JOIN `project.dataset.dim_date` d
  ON f.order_date = d.calendar_date
WHERE d.calendar_date IS NULL;
``` | Engineering |

---

## 4. Business Rules

Goal: Validate that **business logic and KPI rules** are correctly implemented and aligned with stakeholder expectations.

| Check Name | Description | Example SQL / Logic | Owner |
|------------|-------------|---------------------|-------|
| **Revenue_Non_Negative** | Revenue, margin, and cost fields should not be negative unless explicitly allowed. | ```sql
SELECT COUNT(*) AS neg_revenue_count
FROM `project.dataset.fact_sales`
WHERE revenue < 0;
-- Expect 0 or documented exceptions
``` | MI / Finance |
| **Order_Status_Lifecycle_Valid** | Ensure status transitions follow allowed lifecycle (e.g., NEW → SHIPPED → CLOSED). | ```sql
-- Example: detect invalid combinations
SELECT order_id, order_status
FROM `project.dataset.fact_sales`
WHERE order_status NOT IN ('NEW','SHIPPED','CANCELLED','RETURNED','CLOSED');
``` | MI / Operations |
| **Metric_Reconciliation_To_Finance** | Validate that MI revenue/cost totals reconcile to Finance GL within agreed tolerance. | ```sql
-- MI view
SELECT SUM(revenue) AS mi_revenue
FROM `project.dataset.fact_sales`
WHERE order_date BETWEEN '2026-01-01' AND '2026-01-31';

-- Finance GL
SELECT SUM(gl_amount) AS finance_revenue
FROM `finance.gl_revenue`
WHERE gl_period = '2026-01';
``` | MI / Finance |
| **Churn_Logic_Consistency** | Confirm that churn/retention logic matches agreed definition (e.g., 30/60/90-day rules). | ```sql
-- Example skeleton
SELECT 
  customer_id,
  churn_flag,
  last_active_date
FROM `project.dataset.customer_kpis`
WHERE churn_flag = TRUE
  AND last_active_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY);
-- Customers marked churned but active in last 30 days may indicate logic issues
``` | MI / Product / CRM |

---

## 5. Performance & Volumes

Goal: Ensure that **data volumes and pipeline performance** are in line with expectations, avoiding silent degradation.

| Check Name | Description | Example SQL / Logic | Owner |
|------------|-------------|---------------------|-------|
| **Row_Count_Trend_Monitoring** | Track row counts over time to detect sudden drops/spikes. | ```sql
SELECT 
  load_date,
  COUNT(*) AS row_count
FROM `project.dataset.fact_sales`
GROUP BY load_date
ORDER BY load_date DESC
LIMIT 30;
-- Visualise in a dashboard; alert on anomalies
``` | MI / Engineering |
| **Partition_Population_Check** | Ensure that daily/weekly partitions are being populated as expected. | ```sql
SELECT 
  DATE(order_date) AS dt,
  COUNT(*) AS cnt
FROM `project.dataset.fact_sales`
WHERE order_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 14 DAY)
GROUP BY dt
ORDER BY dt;
``` | Engineering |
| **Pipeline_Runtime_SLA** | Monitor total runtime of critical pipelines vs. SLA (e.g., complete by 6am). | ```sql
-- Example: log job start/end times in an audit table
SELECT 
  job_name,
  execution_date,
  start_time,
  end_time,
  TIMESTAMP_DIFF(end_time, start_time, MINUTE) AS duration_minutes
FROM `project.dataset.etl_job_audit`
ORDER BY execution_date DESC;
``` | Engineering / MI Ops |
| **Query_Performance_Baseline** | Check that key MI queries perform within acceptable thresholds as data grows. | ```sql
-- Use warehouse query history; example for BigQuery
SELECT 
  query,
  total_slot_ms,
  total_bytes_processed
FROM `region-us`.INFORMATION_SCHEMA.JOBS
WHERE user_email = 'mi-service-account@project.iam.gserviceaccount.com'
  AND creation_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY);
``` | Engineering |

---

## 6. Reconciliation & Auditability

Goal: Provide **end-to-end traceability** and assurance that MI outputs can be trusted and audited.

| Check Name | Description | Example SQL / Logic | Owner |
|------------|-------------|---------------------|-------|
| **Source_To_MI_Total_Reconciliation** | Compare key totals between source systems and MI aggregates (daily/monthly). | ```sql
-- Source system
SELECT SUM(amount) AS src_total
FROM `source_sys.transactions`
WHERE txn_date BETWEEN '2026-01-01' AND '2026-01-31';

-- MI layer
SELECT SUM(revenue) AS mi_total
FROM `project.dataset.fact_sales`
WHERE order_date BETWEEN '2026-01-01' AND '2026-01-31';
``` | MI / Finance |
| **Refresh_Status_and_Timestamp** | Ensure every MI artifact shows last refresh time and status. | ```sql
-- Example audit table
SELECT 
  data_asset_name,
  last_successful_refresh,
  status
FROM `project.dataset.mi_refresh_audit`
ORDER BY last_successful_refresh DESC;
``` | MI |
| **Lineage_Documentation_Complete** | Verify that critical KPIs have documented lineage from source to report. | *Logic*: Maintain lineage in a catalogue; check that all Tier-1 KPIs have lineage entries. | MI / Data Governance |
| **Change_Log_for_KPI_Logic** | Track changes to KPI definitions and calculation logic (who, when, what changed). | *Logic*: Use Git history + release notes; optionally log changes in a `kpi_change_log` table. | MI Lead |

---

## 7. How to Apply This Checklist

1. **Before Go-Live**  
   - Run all critical checks (Sections 1–4) for each new data pipeline or KPI.  
   - Document results in a simple test report (pass/fail, comments, owners).

2. **BAU Monitoring**  
   - Automate key checks (row counts, null rates, reconciliation, runtime) and surface them in a **Data Quality Dashboard**.  
   - Set clear thresholds and alert routes (who is notified, within what time).

3. **Ownership & Governance**  
   - Assign named owners for each check (MI, Engineering, Business).  
   - Review this checklist quarterly in MI/Data Governance forums and refine as the platform matures.

4. **Communication with Stakeholders**  
   - Translate results into business language (e.g., “99.5% of daily revenue data passed quality checks; variance vs. Finance is <0.3%”).  
   - Use the checklist to **build and sustain trust** in MI outputs.

This checklist should evolve over time, but its purpose remains constant: **to ensure that MI is not just available, but trustworthy and auditable for critical business decisions.**