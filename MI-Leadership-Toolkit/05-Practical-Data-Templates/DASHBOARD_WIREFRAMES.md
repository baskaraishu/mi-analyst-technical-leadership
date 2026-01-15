# Dashboard Wireframes – Standard Layouts for MI

This document provides **reusable wireframe patterns** for MI dashboards. Use these to design consistent, easy-to-read dashboards that answer stakeholder questions quickly.

---

## 1. Executive KPI Overview Dashboard

**Purpose:** Provide a single-page view of the most important business KPIs for senior leaders.

### 1.1 Layout

- **Top row (Hero KPIs – 3 to 5 tiles)**
  - Revenue / GMV
  - Margin / Profit
  - Customer count / Active users
  - Churn / Retention rate
  - NPS / Satisfaction (if available)

- **Middle row (Trends – line charts)**
  - Revenue vs target (YoY / MoM trend).  
  - Customer growth (new vs churned).  

- **Bottom row (Breakdowns – bar/column charts)**
  - Revenue by segment (e.g., region, channel, product line).  
  - Top 5 drivers / underperformers.

### 1.2 Design Guidelines

- Keep filters simple: time period, region, business line.  
- Use clear colour conventions (e.g., green = at/above target, red = below).  
- Limit text; focus on high-impact visuals.

---

## 2. Operational Performance Dashboard

**Purpose:** Support operational managers in monitoring daily/weekly performance and taking action.

### 2.1 Layout

- **Filter panel (left or top)**  
  - Date range, team/region, channel, product.

- **Row 1 (Operational KPIs – tiles)**
  - Volume (orders/tickets/calls).  
  - SLA / response time.  
  - Backlog / open items.  
  - Error rate / defect rate.

- **Row 2 (Trend & Workload)**
  - Daily volume trend (line).  
  - Workload vs capacity (stacked bar by team).

- **Row 3 (Actionable Detail)**
  - Table of top problem categories (e.g., longest SLA breaches).  
  - Drill-through links to detailed views.

### 2.2 Design Guidelines

- Prioritise readability on screens in meetings or control rooms.  
- Highlight thresholds (e.g., SLA < 90% in red).  
- Enable quick drill-down to root causes.

---

## 3. Customer Behaviour & Funnel Dashboard

**Purpose:** Help product and marketing teams understand customer acquisition, conversion, and retention.

### 3.1 Layout

- **Top row (Funnel Visual)**
  - Stages: Visits → Sign-ups → Activated → Paying → Retained.  
  - Show conversion rates between stages.

- **Middle row (Segmented Trends)**
  - Conversion rate by channel (bar).  
  - Cohort retention curves (line chart).  

- **Bottom row (Customer Segments Table)**
  - Segment, size, revenue, churn rate, LTV.

### 3.2 Design Guidelines

- Provide flexible segmentation (channel, device, geography, product).  
- Emphasise **rates and trends**, not just volumes.

---

## 4. Data Quality & Pipeline Health Dashboard

**Purpose:** Give MI and Engineering teams visibility into **data quality and pipeline reliability**.

### 4.1 Layout

- **Top row (Status Tiles)**
  - Number of failed jobs in last 24h.  
  - Data freshness for key datasets (time since last successful load).  
  - Open data incidents from `ANOMALY_DETECTION_LOG`.

- **Middle row (Trends)**
  - Job success rate over time (line).  
  - Row counts / volume checks vs expected (line with bands).

- **Bottom row (Detail Table)**
  - Recent ETL runs with status, duration, rows processed, and error snippets.

### 4.2 Design Guidelines

- Use traffic-light visuals for status (green/amber/red).  
- Provide direct links to logs / RCA records.

---

## 5. Design Checklist for Any Dashboard

Use this quick checklist when finalising any dashboard:

- [ ] **Clear question:** What primary question does this dashboard answer?  
- [ ] **Audience defined:** Who is this for (Exec / Manager / Ops / Analyst)?  
- [ ] **Minimal clutter:** Remove unused visuals and redundant filters.  
- [ ] **Consistent KPIs:** Metrics align with **Data Dictionary** and governance rules.  
- [ ] **Actionable:** Viewer can tell what to do next (escalate, investigate, decide).  
- [ ] **Performance:** Dashboard loads within acceptable time for typical users.  

These wireframes provide a **starting point**; adapt them to your organisation while keeping the **principles of clarity, consistency, and actionability**.