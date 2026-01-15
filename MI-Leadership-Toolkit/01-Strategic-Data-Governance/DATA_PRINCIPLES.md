# MI Data Manifesto

As a Management Information (MI) function, our mandate is to deliver **trusted, timely, and actionable insight** that informs decision-making across the organisation.  
This manifesto sets out the core data principles that every MI Analyst, Engineer, and Leader must uphold.

We commit to three non‑negotiable pillars:

1. **Accuracy** – The numbers are correct, consistent, and reconciled.  
2. **Accessibility** – The right people can access the right information at the right time.  
3. **Security** – Data is protected, compliant, and used responsibly.

---

## 1. Accuracy

### 1.1 Definition

Accuracy means that **reported figures faithfully represent the underlying reality**, with clear lineage from source systems to MI outputs. Data must be complete, consistent, and reconciled so that stakeholders can make decisions with confidence.

> If Finance, Operations, and MI report different answers to the same question, *accuracy has failed*—regardless of how fast or pretty the dashboard is.

### 1.2 Why Accuracy Matters to MI Stakeholders

- **Executive Leadership**: Relies on MI for strategic decisions (investment, pricing, headcount). Inaccurate data erodes trust and delays action.
- **Operational Teams**: Use MI to manage performance (SLAs, throughput, conversion). Bad numbers drive bad behaviours (chasing the wrong targets).
- **Risk & Compliance**: Require auditable, reconciled figures for regulators. Data errors can lead to fines and reputational damage.
- **Data Teams**: Credibility of the MI function depends on consistent, explainable numbers across reports.

### 1.3 Expected Behaviours & Practices

1. **Reconciliation First, Visualisation Second**  
   - Always reconcile KPIs to a trusted source (e.g., Finance ledger, CRM totals) before publishing dashboards.
   - Maintain a documented reconciliation log for key metrics.

2. **Single Definition of Each KPI**  
   - Maintain a governed KPI dictionary (metric name, owner, definition, logic, and source).  
   - Challenge “spreadsheet logic” and undocumented variations of the same metric.

3. **Automated Data Quality Checks in Every Pipeline**  
   - Implement checks for nulls, duplicates, outliers, and schema changes.  
   - Block load or flag alerts when thresholds are breached.

4. **Versioned & Peer-Reviewed Logic**  
   - Store SQL, transformations, and metric definitions in version control (e.g., Git).  
   - Use peer review for any changes to production KPI logic.

5. **Explainability on Demand**  
   - Every MI Analyst should be able to explain, in plain language, how a headline metric is calculated and from which systems.

### 1.4 Example KPIs for Accuracy

| KPI Name                           | Description                                                | Target / Threshold                         |
|------------------------------------|------------------------------------------------------------|--------------------------------------------|
| **KPI_Reconciliation_Rate**        | % of key KPIs reconciled to source-of-truth each month     | ≥ 98% reconciled within 5 working days     |
| **Data_Quality_Issue_Count**       | Number of severity 1–2 data issues impacting MI outputs    | 0 Sev1, ≤ 2 Sev2 per quarter               |
| **Metric_Definition_Alignment**    | % of top 20 KPIs with a single, agreed definition          | 100%                                       |

---

## 2. Accessibility

### 2.1 Definition

Accessibility means that **trusted information is discoverable, understandable, and usable** by authorised stakeholders, without unnecessary friction. The MI function must balance **self-service capability** with controlled governance.

> If stakeholders are exporting data to Excel and manually re‑creating the same reports, *accessibility has failed*—even if the data is technically correct.

### 2.2 Why Accessibility Matters to MI Stakeholders

- **Executives**: Need a curated, high-level view with drill-down on demand—*without* waiting for ad-hoc packs.
- **Managers**: Need operational dashboards that align with their KPIs and review cadence (daily/weekly/monthly).
- **Analysts**: Need governed, well-documented datasets to perform deeper analysis quickly.
- **Technology & Data Teams**: Need clear access patterns to design scalable, cost-effective platforms.

### 2.3 Expected Behaviours & Practices

1. **Design for the Decision, Not the Data**  
   - Start with the decision stakeholders need to make, then work backwards to the metrics and visualisations.
   - Avoid “data dumps”; provide curated, decision-ready views.

2. **Self-Service with Guardrails**  
   - Provide certified datasets and standardised semantic layers (e.g., governed views, metrics layer).  
   - Label content clearly: **Certified**, **In Development**, **Legacy**.

3. **Consistent Navigation & Nomenclature**  
   - Use common naming conventions across dashboards and reports.  
   - Group content by business domain (Sales, Operations, Finance) and audience (Exec, Manager, Analyst).

4. **Documentation Embedded in Tools**  
   - Surface metric descriptions, data lineage, and refresh schedules *_inside_* BI tools (tooltips, info panels).  
   - Maintain a searchable MI catalogue.

5. **Inclusive Design**  
   - Ensure dashboards are usable by non-technical stakeholders: clear labels, minimal jargon, intuitive filters.  
   - Provide training guides and short walkthroughs for key reports.

### 2.4 Example KPIs for Accessibility

| KPI Name                               | Description                                                    | Target / Threshold                      |
|----------------------------------------|----------------------------------------------------------------|-----------------------------------------|
| **MI_Self_Service_Adoption_Rate**      | % of MI usage from self-service / interactive dashboards       | ≥ 70% of total MI consumption           |
| **Time_To_Find_Key_Report**            | Median time for a user to find and open a key MI asset        | ≤ 2 minutes                             |
| **Active_Dashboard_Users**             | Number of unique users viewing MI dashboards each month       | Growing trend, aligned with population  |

---

## 3. Security

### 3.1 Definition

Security means that **data is protected from unauthorised access, misuse, and loss**, while still enabling legitimate use. The MI function must comply with legal, regulatory, and internal policies, especially for personal and commercially sensitive data.

> If people can see data they shouldn’t—or cannot see data they are accountable for—*security has failed*.

### 3.2 Why Security Matters to MI Stakeholders

- **Customers & Regulators**: Expect responsible handling of personal and sensitive data (GDPR, PCI, etc.).
- **Executives & Board**: View data breaches as existential risks (fines, reputational damage, lost trust).
- **Business Teams**: Need confidence that MI platforms are safe for daily operations and strategic planning.
- **Data Teams**: Must manage access in a way that is auditable, consistent, and scalable.

### 3.3 Expected Behaviours & Practices

1. **Role-Based Access Control (RBAC)**  
   - Grant access based on role and legitimate business need, not individual favour or convenience.  
   - Regularly review and certify access lists (e.g., quarterly).

2. **Least Privilege by Default**  
   - Users receive the minimum access necessary to perform their role.  
   - Elevation of privileges is temporary and audited.

3. **Data Classification & Masking**  
   - Classify data (Public, Internal, Confidential, Restricted).  
   - Mask or anonymise sensitive fields in MI layers where full detail is not required (e.g., hashed IDs, aggregated metrics).

4. **Secure Development & Deployment**  
   - Credentials, keys, and secrets are stored in secure vaults, never in code or spreadsheets.  
   - Pipelines and reports are deployed via controlled CI/CD processes with audit logs.

5. **Incident Readiness & Auditability**  
   - Maintain logging of access, data extracts, and configuration changes.  
   - Have a clear runbook for suspected data incidents (who to inform, what to investigate, how to contain).

### 3.4 Example KPIs for Security

| KPI Name                                  | Description                                                   | Target / Threshold                            |
|-------------------------------------------|---------------------------------------------------------------|-----------------------------------------------|
| **Access_Review_Completion_Rate**         | % of scheduled MI access reviews completed on time           | 100% quarterly completion                     |
| **Least_Privilege_Compliance**            | % of users with access aligned to documented role profiles   | ≥ 95%                                         |
| **Security_Incident_Count_MI**            | Number of MI-related security incidents per quarter          | 0 major incidents; downward trend overall     |

---

## 4. How We Use This Manifesto

This manifesto is not a poster exercise—it is a **living standard** that guides how we design, build, and operate MI.

- **For MI Analysts**: Use these principles to challenge requirements, design robust datasets, and push back on shortcuts that compromise quality or security.
- **For MI Engineers**: Embed these principles into pipelines, models, and deployment processes (tests, access controls, monitoring).
- **For MI Leaders**: Align team objectives, performance reviews, and investment decisions to these pillars; regularly report on the KPIs listed above.

**If a deliverable conflicts with this manifesto, we fix the deliverable—not the principles.**