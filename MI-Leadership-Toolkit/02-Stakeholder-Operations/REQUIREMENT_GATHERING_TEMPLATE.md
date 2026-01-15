# MI Requirement Gathering Template

> Use this template to structure conversations with stakeholders and translate **business questions** into **data requirements and MI deliverables**.

---

## 1. Stakeholder & Context

- **Business Area / Function:**  
- **Primary Stakeholder (Role & Name):**  
- **Secondary Stakeholders (Roles):**  
- **Date & Version:**  

**Business Context (1–3 sentences):**  
- What is happening in the business that drives this request? (growth, risk, regulatory, cost pressure, strategy change)

---

## 2. Business Questions & Decisions

**2.1 Core Business Questions**  
_List the questions the stakeholder wants to answer, in their own words._

1. Q1:  
2. Q2:  
3. Q3:  

**2.2 Decisions to Be Made**  
_For each question, identify the decisions or actions it should enable._

| # | Business Question | Decision / Action Enabled | Priority (H/M/L) |
|---|-------------------|---------------------------|------------------|
| 1 |                   |                           |                  |
| 2 |                   |                           |                  |
| 3 |                   |                           |                  |

> If there is no clear decision linked to a question, challenge whether it should be in scope.

---

## 3. KPIs & Metrics

**3.1 Existing KPIs**  
_Which KPIs are already used in this area? Are they trusted?_

- Existing KPIs:  
- Known issues (definition, trust, data quality):  

**3.2 New or Refined KPIs Needed**

| KPI Name | Business Definition (Plain English) | How It Will Be Used | Owner |
|----------|-------------------------------------|----------------------|-------|
|          |                                     |                      |       |
|          |                                     |                      |       |

_Link to Data Dictionary entries where they exist._

---

## 4. Data Requirements

**4.1 Subject Areas & Dimensions**

- Customers / Accounts (e.g., segment, tenure, region)  
- Products / Services (e.g., plan, category)  
- Channels (e.g., web, app, branch, partner)  
- Time (e.g., day, week, month, cohort)  
- Other dimensions:  

**4.2 Source Systems (Known or Suspected)**

| System | Type (CRM, Billing, Web, etc.) | Usage in MI | Owner / SME |
|--------|----------------------------------|-------------|-------------|
|        |                                  |             |             |
|        |                                  |             |             |

**4.3 Filters & Grain**

- Required grain:  
  - e.g., daily by channel, monthly by region, customer-level, transaction-level.  
- Typical filters:  
  - e.g., date range, region, channel, product, segment.  

---

## 5. Reporting & UX Requirements

**5.1 Consumers & Access**

- Who will use this? (roles, approximate number of users)  
- Access level: Exec / Manager / Analyst / Operational  
- Any data sensitivity considerations? (PII, commercially sensitive, regulatory)

**5.2 Delivery Format**

- [ ] Dashboard (interactive)  
- [ ] PDF / Slide pack  
- [ ] Self-service dataset  
- [ ] Email summary / alerts  

**5.3 Refresh Frequency & Latency**

- [ ] Real-time / near real-time  
- [ ] Intra-day (e.g., hourly)  
- [ ] Daily (e.g., 06:00 local time)  
- [ ] Weekly / Monthly  

**5.4 User Experience Notes**

- Key views/pages required (e.g., Executive overview, Operational drill-down).  
- Top 3 visualisations (e.g., funnel, trend line, segmentation tree, heatmap).  
- Device usage: desktop, tablet, mobile.

---

## 6. Non-Functional Requirements

| Aspect | Requirement | Notes |
|--------|-------------|-------|
| Performance | Max acceptable load time, typical query complexity |  |
| Availability | Hours of operation, downtime tolerance |  |
| Security | Role-based access, row-level security, masking |  |
| Auditability | Need for refresh logs, change tracking |  |
| Compliance | GDPR/PCI/other obligations |  |

---

## 7. Risks, Assumptions & Dependencies

**7.1 Risks**

- Data not yet available / poor quality:  
- Conflicting KPI definitions between teams:  
- Over-reliance on Excel outside the MI stack:  

**7.2 Assumptions**

- Assumed behaviour (customer, system, process):  
- Assumed data availability and refresh:  

**7.3 Dependencies**

- Upstream projects (system changes, migrations):  
- Other data initiatives (e.g., master data, data warehouse upgrades):  

---

## 8. Success Criteria & Acceptance

Define **how we will know this MI deliverable is successful**.

- Business success criteria (e.g., "Used in monthly performance review", "Replaces legacy Excel pack"):  
- MI success criteria (e.g., "<2% reconciliation variance vs Finance", "Load completes by 07:00 daily"):  

**Sign-off**

- Business Sponsor:  
- MI Lead:  
- Date:  

---

This template ensures that MI requirements are framed around **decisions and outcomes**, not just data fields or charts, and provides a clear bridge between business stakeholders and the MI delivery team.