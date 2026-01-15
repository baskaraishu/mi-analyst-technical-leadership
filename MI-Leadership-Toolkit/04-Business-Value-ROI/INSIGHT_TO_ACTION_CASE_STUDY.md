# Insight-to-Action Case Study Template

> Use this template to document **how an MI insight led to a concrete business outcome** (e.g., 10% churn reduction, cost avoidance, revenue uplift). Each section includes guiding questions and example bullets to help you write a clear, executive-ready narrative.

---

## 1. Background

**Purpose:** Set the context in simple business language.

- What business area is this about? (e.g., Customer Retention, Sales Performance, Operational Efficiency)
- Which products, channels, or regions are in scope?
- What was happening in the business at the time (growth, crisis, regulatory change)?

**Example framing:**
- "In Q2 FY26, the Retail division observed rising customer churn in the digital channel despite record acquisition volumes."
- "Operational costs in the contact centre had increased by 15% year-on-year with no improvement in customer satisfaction."

---

## 2. Business Problem

**Purpose:** Define the problem in measurable terms and from the stakeholder’s point of view.

Guiding questions:
- What specific problem were stakeholders worried about?
- How was it measured (KPIs, targets, trends)?
- What was the scale of the impact (customers, revenue, cost, risk)?

**Example bullets:**
- Churn rate increased from **18% to 24%** over 6 months in the subscription product.
- Estimated **annual revenue at risk: £3.5m** from lost customers.
- No clear view of **where** churn was highest (segment, channel, product) or **why** it was happening.

---

## 3. Data Approach

**Purpose:** Explain how data was used to understand and size the problem.

Guiding questions:
- Which data sources were used? (CRM, billing, web analytics, contact centre logs, etc.)
- What key dimensions and metrics were analysed? (customer segment, tenure, channel, product, campaign)
- What time period and granularity (daily/weekly/monthly) were in scope?

**Example bullets:**
- Joined **CRM**, **billing**, and **digital analytics** data to build a unified customer journey view.
- Defined churn as: *"no successful bill and no activity for 90 days"*.
- Analysed **12 months of history** at a **monthly** granularity, segmented by **tenure band**, **channel**, and **plan type**.

---

## 4. MI Solution (Report / Dashboard / Model)

**Purpose:** Describe the MI asset that enabled new understanding.

Guiding questions:
- What did you build? (dashboard, recurring report, model output, alerting mechanism)
- Who was the primary audience? (e.g., Retention Squad, Ops Leadership, ExCo)
- How often does it refresh? (daily, weekly, monthly)

**Example bullets:**
- Built a **Churn Risk Dashboard** in Looker Studio with:
  - Churn rate by **segment, tenure, channel, and product**.
  - Trend lines vs **target** and **previous year**.
  - Drill-down capability to customer-level cohorts.
- Outputs refreshed **daily** using the BigQuery MI dataset.
- Distribution list: **Head of Retention, Marketing Leads, Product Owners, and MI Business Partners**.

---

## 5. Key Insights

**Purpose:** Highlight the *new information* the business gained from the MI solution.

Guiding questions:
- What did the analysis reveal that was not previously understood or quantified?
- Which segments, channels, or behaviours stood out?
- Were any assumptions disproved?

**Example bullets:**
- Identified that **new customers (tenure < 90 days)** had **2x higher churn** than long-tenure customers.
- Found that customers acquired via **Paid Social** had a churn rate of **32%**, vs **18%** via **Organic Search**.
- Discovered that customers who contacted support more than **3 times in first month** were **4x more likely** to churn.

> Keep insights **short, specific, and actionable**. Each insight should answer: *"So what?"*

---

## 6. Actions Taken

**Purpose:** Document what the business actually changed because of the insight.

Guiding questions:
- What decisions were made? (pricing, product, operations, communications)
- What concrete actions were implemented? (campaigns, process changes, system changes)
- Which teams were involved? (Marketing, Product, Operations, Finance)

**Example bullets:**
- **Retention team** launched a targeted onboarding campaign for new customers:
  - Proactive welcome emails and in-app guides in first 30 days.
  - Priority routing to experienced agents for early-life calls.
- **Marketing** tightened acquisition criteria for Paid Social campaigns and rebalanced budget towards higher-retention channels.
- **Operations** introduced a "first-contact resolution" KPI for early-life support interactions.

---

## 7. Measured Impact & ROI

**Purpose:** Quantify the outcome and link it directly to MI-driven actions.

Guiding questions:
- How did key metrics move after the intervention? (churn, NPS, cost-to-serve, revenue)
- Over what time period was impact measured?
- What is the estimated financial benefit (savings, uplift, cost avoidance)?

**Example structure:**

- **Impact on KPIs**:
  - Overall churn reduced from **24% to 21.5%** within 6 months.
  - New customer churn (tenure < 90 days) reduced by **10 percentage points**.
- **Financial Outcome**:
  - Estimated **10% churn reduction in the highest-risk segment** → **£1.2m annual revenue preserved**.
  - Contact centre repeat calls reduced by **8%**, saving **£150k per year** in handling costs.
- **Attribution**:
  - 70% of the uplift attributed to onboarding & retention interventions informed by MI analysis (supported by A/B test or time-series analysis).

> Where possible, use simple, credible calculations and state assumptions clearly.

---

## 8. Lessons Learned

**Purpose:** Capture what worked, what didn’t, and how the MI function will improve.

Guiding questions:
- What would you do differently next time (data, process, stakeholder engagement)?
- Were there any data quality or definition issues uncovered during the work?
- How did stakeholder behaviour change (use of dashboards, engagement with MI)?

**Example bullets:**
- Early alignment on **churn definition** avoided conflicting numbers in later forums.
- Involving **Retention and Product** teams in dashboard design increased adoption and trust.
- Need to invest in **better tagging of acquisition campaigns** to improve attribution accuracy.

---

## 9. Reusable Assets & Next Steps

**Purpose:** Show how this work can be **scaled or replicated**, demonstrating enduring value of MI.

Guiding questions:
- What assets were created that others can reuse? (SQL models, views, dashboards, data quality checks)
- Can this pattern be applied to other areas (upsell, cross-sell, operational efficiency)?
- What are the agreed next steps?

**Example bullets:**
- **Reusable Assets**:
  - BigQuery view: `customer_churn_features_v1` (used for churn modelling and other retention analysis).
  - Standardised **Churn KPI definition** in the MI KPI dictionary.
  - Looker Studio template: **"Customer Retention – Executive Overview"**.
- **Next Steps**:
  - Extend approach to **B2B segment** with different churn dynamics.
  - Develop a **predictive churn model** (Stage 4 of KPI maturity roadmap) to move from descriptive to proactive interventions.

---

## 10. Case Study Summary (1-Slide Executive View)

> Optional but recommended: summarise this case study in a single slide / section for ExCo.

Suggested one-slide structure:

- **Problem:** One sentence on the business issue + scale (e.g., "Churn up 6pp, £3.5m at risk").
- **Insight:** One sentence on the key MI finding (e.g., "New customers via Paid Social churn 2x more").
- **Action:** One sentence on what was done (e.g., "Targeted onboarding + channel rebalancing").
- **Impact:** One sentence on measured benefit (e.g., "10% churn reduction, £1.2m annual revenue preserved").

---

By consistently documenting Insight-to-Action stories using this template, the MI function can demonstrate **clear, repeatable business value**, moving the conversation from *"reporting"* to *"strategic impact and ROI"*.  
Use this as a living repository of wins to support investment cases, performance reviews, and MI capability roadmaps.