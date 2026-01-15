# MI Report & Dashboard Catalog – Index

This index provides a **single entry point** to all key MI reports and dashboards, helping stakeholders know **what exists, who it is for, and how to access it**.

Use this as a catalogue to manage **visibility, ownership, and lifecycle** of MI assets.

---

## 1. Catalogue Structure

We group MI assets by **domain** and **audience**:

- **Domains**: Sales, Customer, Operations, Finance, Risk, Product, etc.  
- **Audience**: Executive, Management, Operational, Analyst.  

Each entry in the catalogue should capture at least:

| Field | Description |
|-------|-------------|
| **Report ID** | Unique identifier for the asset. |
| **Title** | Human-friendly report/dashboard name. |
| **Domain** | Business area (Sales, Ops, etc.). |
| **Primary Audience** | Exec / Manager / Operational / Analyst. |
| **Owner** | Business owner accountable for content. |
| **MI Contact** | MI analyst responsible for maintenance. |
| **Frequency** | Refresh cycle (real-time, daily, monthly). |
| **Source** | BI tool and link/URL. |
| **Certification Status** | Certified / In Development / Legacy. |
| **Description** | Short summary of purpose and key KPIs. |

---

## 2. Report Catalog Template

Use the following table as a working index (typically maintained in a BI catalogue, Confluence, or similar; mirrored here for portfolio clarity).

| Report ID | Title | Domain | Audience | Owner | MI Contact | Frequency | Tool / Location | Status | Description |
|-----------|-------|--------|----------|-------|-----------|-----------|-----------------|--------|-------------|
| RPT-001 | Executive Performance Overview | Enterprise | Executive | CFO | Head of MI | Monthly | Looker Studio (link) | Certified | Top-level revenue, cost, margin, and key operational KPIs vs plan and last year. |
| RPT-002 | Customer Retention Dashboard | Customer | Manager | Head of Retention | Senior MI Analyst | Daily | Looker Studio (link) | Certified | Churn, retention, NPS, and contact drivers by segment, channel, and product. |
| RPT-003 | Crypto MI – Market Intelligence | Product | Analyst / Manager | Head of Digital Assets | MI Analyst – Crypto | Daily | Looker Studio (link) | Certified | Cryptocurrency prices, market cap, and volatility sourced from BigQuery crypto_analytics dataset. |
| RPT-004 | Operational SLA Monitor | Operations | Operational | Ops Director | MI Partner – Ops | Hourly | Power BI (link) | In Development | Real-time SLA and backlog monitoring for key operational queues. |
| RPT-005 | Legacy Sales Excel Pack | Sales | Manager | Sales Controller | N/A | Weekly | Shared Drive (path) | Legacy | Historical Excel-based sales reporting due for migration to BI. |

_Add further rows for each MI asset._

---

## 3. Certification & Lifecycle Status

We classify report status to manage expectations and drive migration away from legacy artefacts:

| Status | Description |
|--------|-------------|
| **Certified** | Officially endorsed as the single source of truth for its scope. Meets data quality, documentation, and ownership standards. |
| **In Development** | Being built or piloted; may change frequently; not yet approved for wide consumption. |
| **Legacy** | Older asset maintained only for historical reasons; replacement exists or is planned. |

**Rules:**
- Only **Certified** reports should be used in Board/ExCo packs.
- **Legacy** items must have a **retirement plan** and owner.

---

## 4. Access & Permissions

For each catalogue entry, document:

- Access model: open to all / restricted by role / restricted by team.  
- Whether row-level or column-level security is applied.  
- How users request access (service desk, form, MI contact).

_Example:_
- "RPT-002 – Customer Retention Dashboard: Accessible to Retention, Marketing, and MI teams via SSO; request additional access via MI Service Desk ticket."

---

## 5. Governance & Maintenance

**5.1 Roles**

| Role | Responsibilities |
|------|------------------|
| **Report Owner (Business)** | Accountable for content accuracy, relevance, and decommissioning decisions. |
| **MI Contact** | Maintains data feeds, definitions, and layout; first point of contact for issues. |
| **MI Lead / Governance** | Reviews catalogue quarterly, manages certification process, ensures alignment with MI strategy. |

**5.2 Review Cadence**

- **Monthly**: Check for broken links, defunct assets, immediate issues.  
- **Quarterly**: Review certification status, usage statistics, and retirement candidates.  
- **Annually**: Strategic review aligned to MI roadmap and business planning.

---

## 6. Usage Metrics

To understand whether MI assets are being used, track:

- **Views per report** (over 30/90 days).  
- **Unique users per report**.  
- **Bounce rate** (users who open and close quickly).  
- **Reports unused for >90 days**.

Use these insights to:
- Retire low-value assets.  
- Focus improvements on high-usage reports.  
- Target training where adoption is low but potential value is high.

---

By maintaining a clear **Report Catalog Index**, the MI team provides transparency, reduces duplication, and ensures stakeholders know **where to go for trusted information** and who to contact when something doesn’t look right.