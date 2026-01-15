# GenAI for MI – Data Acceleration Playbook

Generative AI (GenAI) can significantly **accelerate the work of MI analysts** by assisting with SQL writing, documentation, narrative summaries, and stakeholder communication—when used responsibly.

This document outlines **safe, high-value use cases** for LLMs in the MI lifecycle and how to embed them without compromising governance or data quality.

---

## 1. Principles for Using GenAI in MI

1. **Human in the Loop**  
   - GenAI assists, but does not replace, human judgment—especially for KPI definitions and business narratives.

2. **No Raw Confidential Data in Prompts**  
   - Avoid pasting raw customer data, credentials, or commercially sensitive data into external tools.

3. **Consistency with Governance**  
   - All generated SQL or logic must still comply with **Data Dictionary**, **ETL standards**, and security policies.

4. **Traceability**  
   - Final code and text must be stored in version control or documentation, not just left in chat logs.

---

## 2. High-Value GenAI Use Cases

### 2.1 SQL Drafting & Refactoring

**Use GenAI to:**
- Draft initial SQL queries based on natural-language descriptions of requirements.  
- Refactor complex or legacy SQL into cleaner, modular CTE-based structure.  
- Convert queries between SQL dialects (e.g., SQL Server → BigQuery).

**Example Prompt Pattern:**
> "Given a table `fact_sales` with `order_date`, `customer_id`, `revenue`, and a `dim_customer` table with `customer_segment`, draft BigQuery SQL to calculate monthly revenue and churned customers by segment over the last 12 months. Follow window function best practices and avoid SELECT *."

**Controls:**
- Always review and test generated SQL.  
- Ensure naming conventions and filters match MI standards.

---

### 2.2 Narrative Summaries of Dashboards

**Use GenAI to:**
- Turn dashboard views or KPI tables into **executive summaries** (e.g., monthly performance packs).  
- Generate "MI Summary" text blocks for recurring reports.

**Example Prompt Pattern:**
> "Summarise this table of monthly revenue and YoY % into 3–5 bullet points suitable for an executive audience. Focus on key movements, risks, and opportunities."

**Controls:**
- Do not share raw data; instead, paste **aggregated tables or anonymised extracts**.  
- Validate that statements are numerically accurate and not over-interpreted.

---

### 2.3 Documentation & Data Dictionary Support

**Use GenAI to:**
- Draft initial **business definitions** for KPIs in the Data Dictionary.  
- Generate descriptions for columns, models, or dashboards based on existing logic.

**Example Prompt Pattern:**
> "Based on this SQL snippet that calculates `monthly_active_customers`, propose a clear business definition suitable for a KPI dictionary, including inclusions and exclusions."

**Controls:**
- Final wording must be reviewed and approved by **Data Owners** and **MI Stewards**.

---

### 2.4 Ad-Hoc Analysis Planning

**Use GenAI to:**
- Brainstorm **analysis plans** and decomposition of business problems.  
- Identify potential segments, metrics, and visualisations for a given question.

**Example Prompt Pattern:**
> "We are seeing higher churn in our subscription product. Suggest an analysis plan using our MI data warehouse to identify drivers by segment, tenure, and channel. Include potential SQL patterns and visuals."

---

## 3. Practices to Avoid

- Using GenAI outputs **without review or testing**.  
- Relying on GenAI to create "official" KPI definitions without governance.  
- Pasting **live PII or confidential tables** into external tools.  
- Treating GenAI as a source of truth for regulatory or financial reporting.

---

## 4. Measuring Impact of GenAI in MI

Track how GenAI contributes to productivity and value:

| Metric | Description |
|--------|-------------|
| **SQL_Delivery_Time_Reduction** | Estimated reduction in time to produce/modify analysis SQL. |
| **Documentation_Coverage_Improvement** | Increase in % of KPIs/tables with complete documentation. |
| **MI_Pack_Turnaround_Time** | Time from data availability to executive summary completion. |
| **User_Satisfaction_Score** | Analyst feedback on GenAI tools and workflows. |

---

## 5. Example Workflow – Assisted KPI Development

1. **Stakeholder requirement** captured using `REQUIREMENT_GATHERING_TEMPLATE`.  
2. MI analyst uses GenAI to **draft initial SQL** for KPI calculation.  
3. Analyst refines and validates SQL against source data.  
4. KPI definition and logic are documented in **Data Dictionary** (with GenAI assisting text).  
5. GenAI helps create **plain-language narrative** for performance commentary.  

At each step, ownership and accountability remain with **MI professionals**, with GenAI acting as a **productivity accelerator**, not a decision-maker.

---

By using GenAI **deliberately and safely**, the MI team can **increase throughput, improve documentation quality, and free up time** to focus on higher-value work such as stakeholder engagement and strategic insight.