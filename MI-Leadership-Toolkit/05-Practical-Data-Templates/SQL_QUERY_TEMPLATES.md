# SQL Query Templates for MI Analysts

These templates provide **ready-to-adapt SQL patterns** for common Management Information (MI) metrics. They are written in **standard SQL** compatible with modern warehouses such as **BigQuery, Snowflake, Redshift**, and others (with minor syntax adjustments).

Included:
1. **Year-over-Year (YoY) Growth**  
2. **Rolling 7-Day Average**  
3. **Churn Rate (Subscription / Customer Base)**

---

## 1. Year-over-Year Growth (e.g., Revenue by Month)

### Business Explanation
Year-over-year (YoY) growth compares performance in a given period (e.g., month) to the **same period in the previous year**. This is essential for:
- Seasonality-aware performance tracking
- Executive reporting (e.g., "Revenue up 12% YoY in Q1")
- Identifying structural growth vs. short-term fluctuations

### Assumptions
- Fact table: `fact_revenue`
- Key columns:
  - `txn_date` (DATE) – transaction date
  - `revenue_amount` (NUMERIC/FLOAT) – revenue value
- Grain: one row per transaction (will be aggregated to month)

### SQL Template (Monthly YoY Growth)

```sql
WITH monthly_revenue AS (
  SELECT
    DATE_TRUNC(txn_date, MONTH) AS month_start,
    EXTRACT(YEAR FROM txn_date) AS year,
    EXTRACT(MONTH FROM txn_date) AS month,
    SUM(revenue_amount) AS revenue
  FROM `project.dataset.fact_revenue`
  WHERE txn_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 3 YEAR)
  GROUP BY month_start, year, month
),

current_vs_prior AS (
  SELECT
    curr.month_start,
    curr.year AS current_year,
    curr.revenue AS current_revenue,
    prev.year AS prior_year,
    prev.revenue AS prior_revenue,
    SAFE_DIVIDE(curr.revenue - prev.revenue, prev.revenue) * 100 AS yoy_growth_pct
  FROM monthly_revenue curr
  LEFT JOIN monthly_revenue prev
    ON curr.month = prev.month
   AND curr.year = prev.year + 1
)

SELECT
  month_start,
  current_year,
  current_revenue,
  prior_year,
  prior_revenue,
  yoy_growth_pct
FROM current_vs_prior
ORDER BY month_start;
```

### How to Present This in MI
- **Executive KPI tile**: "Revenue YoY %" for the latest completed month.
- **Line chart**: 24–36 months of revenue with YoY % as a secondary series.
- **Table**: Month, Revenue, YoY %, colour-coded for positive/negative change.

---

## 2. Rolling 7-Day Average (Daily KPI Smoothing)

### Business Explanation
A rolling 7-day average smooths short-term volatility in **daily metrics** (e.g., daily sign-ups, logins, transactions). This helps:
- Reduce noise from day-of-week effects (weekends vs weekdays)
- Spot underlying trends earlier
- Communicate a more stable view to stakeholders

### Assumptions
- Fact table: `fact_events`
- Key columns:
  - `event_date` (DATE) – date of the event
  - `metric_value` (INT/FLOAT) – count or value (e.g., sign-ups, orders, sessions)
- Grain: one row per event (we will aggregate by date)

### SQL Template (Rolling 7-Day Average)

```sql
WITH daily_metric AS (
  SELECT
    event_date,
    SUM(metric_value) AS metric_total
  FROM `project.dataset.fact_events`
  WHERE event_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 60 DAY)
  GROUP BY event_date
),

rolling_window AS (
  SELECT
    event_date,
    metric_total,
    AVG(metric_total) OVER (
      ORDER BY event_date
      ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS rolling_7d_avg
  FROM daily_metric
)

SELECT
  event_date,
  metric_total,
  rolling_7d_avg
FROM rolling_window
ORDER BY event_date;
```

### How to Present This in MI
- **Dual-line chart**: Plot `metric_total` (daily) vs `rolling_7d_avg` on the same graph.
- Use **rolling average** for commentary (e.g., "7-day average sign-ups increased by 8% week-on-week").
- Highlight periods where daily value deviates significantly (>20%) from the rolling average (potential incidents or campaigns).

---

## 3. Churn Rate (Subscription / Customer Base)

### Business Explanation
Churn rate measures **the percentage of customers who stop using a service** over a given period. This is critical for:
- Subscription and SaaS businesses
- Retention, CRM, and lifecycle marketing
- Revenue forecasting and customer lifetime value (CLV) analysis

There are many valid definitions; this template uses a **cohort-based monthly churn rate**.

### Assumptions
- Snapshot/Status table: `customer_status_monthly`
- Key columns:
  - `month_start` (DATE) – first day of the month
  - `customer_id` (STRING/INT)
  - `is_active` (BOOLEAN) – whether the customer is active in that month
- Definition:
  - A customer is **churned in month M** if they were active in **month M-1** and not active in **month M**.

### SQL Template (Monthly Churn Rate)

```sql
WITH base AS (
  SELECT
    customer_id,
    month_start,
    is_active,
    LEAD(is_active) OVER (
      PARTITION BY customer_id
      ORDER BY month_start
    ) AS is_active_next_month,
    LEAD(month_start) OVER (
      PARTITION BY customer_id
      ORDER BY month_start
    ) AS next_month_start
  FROM `project.dataset.customer_status_monthly`
  WHERE month_start >= DATE_SUB(DATE_TRUNC(CURRENT_DATE(), MONTH), INTERVAL 24 MONTH)
),

churn_events AS (
  SELECT
    month_start AS cohort_month,
    next_month_start AS churn_month,
    customer_id,
    is_active,
    is_active_next_month,
    CASE
      WHEN is_active = TRUE
       AND is_active_next_month = FALSE
       AND next_month_start IS NOT NULL
      THEN 1 ELSE 0
    END AS churn_flag
  FROM base
),

monthly_churn AS (
  SELECT
    churn_month,
    COUNTIF(is_active = TRUE) AS customers_at_start,
    SUM(churn_flag) AS customers_churned,
    SAFE_DIVIDE(SUM(churn_flag), COUNTIF(is_active = TRUE)) * 100 AS churn_rate_pct
  FROM churn_events
  WHERE churn_month IS NOT NULL
  GROUP BY churn_month
)

SELECT
  churn_month,
  customers_at_start,
  customers_churned,
  churn_rate_pct
FROM monthly_churn
ORDER BY churn_month;
```

### How to Present This in MI
- **Headline KPI**: Monthly churn % with trend over 12–24 months.
- **Segmentation**: Break down churn by acquisition channel, tenure band, product, or region using additional dimensions.
- **Retention Story**: Pair churn chart with **new acquisition** and **net growth** to tell a complete customer base story.

---

## Usage Notes for MI Analysts

- Treat these templates as **starting points**; always validate definitions with business stakeholders (Finance, Product, CRM).
- Store final, agreed versions in a **version-controlled repository** and reference them in your **KPI dictionary**.
- Where possible, wrap these queries into **views or models** (e.g., in dbt or as BigQuery views) to standardise across dashboards and reports.

By using well-defined, reusable SQL templates, you reduce time-to-insight, improve consistency across MI outputs, and strengthen trust in your numbers.