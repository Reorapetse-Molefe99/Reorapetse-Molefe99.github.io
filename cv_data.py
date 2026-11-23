"""
All content for the CV website lives in this one file.

To update the website: edit the text below, save, check it locally with `python app.py`,
then commit and push to GitHub. The site rebuilds and redeploys automatically.

Text inside **double asterisks** is shown in bold on the website.
"""

# ---------------------------------------------------------------------------
# Profile
# ---------------------------------------------------------------------------
PROFILE = {
    "name": "Reorapetse Molefe",
    "first_name": "Reorapetse",
    "initials": "RM",
    "title": "Data Scientist | Senior Quantitative Analyst",
    "location": "Sandton, Johannesburg, South Africa",
    "email": "rlmolefe1999@gmail.com",
    # Set SHOW_PHONE = False to hide the phone number on the public site.
    "phone": "+27 (0) 79 210 2948",
    "linkedin": "https://www.linkedin.com/in/reorapetse-molefe-4b5753214/",
    "github": "https://github.com/Reorapetse-Molefe99",
    "photo": "static/img/portrait.jpg",
    "cv_pdf": "static/cv/Reorapetse_Molefe_CV.pdf",
    "cv_updated": "November 2026",
}
SHOW_PHONE = True

# ---------------------------------------------------------------------------
# Opening section (hero) and "About me"
# ---------------------------------------------------------------------------
HERO = {
    "eyebrow": "Data scientist in banking since 2022",
    # These rotate in the typing animation under your name.
    "roles": [
        "Data Scientist",
        "Senior Quantitative Analyst",
        "Collections Strategist",
        "Financial Engineering Researcher",
        "Data & AI Engineer",
    ],
    "intro": (
        "I turn credit data into decisions that change outcomes for customers and lenders, "
        "and I measure every one of them."
    ),
}

ABOUT = {
    "statement": "Good strategy is *measured*, not assumed.",
    "paragraphs": [
        "I'm Reorapetse, a data scientist and quantitative analyst based in Johannesburg. "
        "I started out in **actuarial science and mathematical statistics at Wits**, then joined "
        "FNB's quantitative analyst graduate programme in 2022. I've spent nearly five years "
        "since then in credit risk and collections, building machine learning models, dialler "
        "strategies and dashboards that help banks reach the right customer at the right time "
        "with the right offer.",
        "I'm happiest where analysis meets action. A model is only as good as the decision it "
        "changes, so I build strategies with operations teams, test them against holdout groups "
        "and track them until the results are clear: **R3 million collected** by settlement offer "
        "models, **45% more promise-to-pay arrangements** and **activation rates that doubled**.",
        "Outside my day job, I'm finishing a **Master's in Financial Engineering at UJ**, "
        "researching how ESG ambiguity and climate policy uncertainty should shape sustainable "
        "portfolios. I'm also building an e-commerce and clickstream analytics platform for a "
        "craft cocktail company with AI coding agents and Databricks.",
    ],
    "facts": [
        ("Currently", "Manager & Senior Quant Analyst, Old Mutual Bank"),
        ("Studying", "Master of Financial Engineering, UJ"),
        ("Based in", "Sandton, Johannesburg"),
        ("Member", "TASSA, Actuarial Society of South Africa"),
    ],
}

# Scrolling ticker under the opening section.
TICKER = [
    "R3m+ collected by settlement offer models",
    "+45% promise-to-pay arrangements",
    "2× activation on escalated accounts",
    "~5 years in banking & credit risk",
    "Master's in Financial Engineering",
]

# Animated counters in the "Impact" section.
# value is counted up from zero; prefix/suffix are shown around it.
IMPACT = [
    {"prefix": "R", "value": 2.3, "decimals": 1, "suffix": "m",
     "label": "Collected by the Settlement Offer ML V2 model on its first implementation",
     "org": "FNB"},
    {"prefix": "+", "value": 45, "decimals": 0, "suffix": "%",
     "label": "Promise-to-pay arrangements in the first month of the CD0–CD1 inflow strategy",
     "org": "Old Mutual Bank"},
    {"prefix": "", "value": 10.75, "decimals": 2, "suffix": "%",
     "label": "Activation rate on escalated CD2 accounts, versus 5.21% for the holdout group",
     "org": "Old Mutual Bank"},
    {"prefix": "+", "value": 17, "decimals": 0, "suffix": "%",
     "label": "Arrangement volumes after automating PTP target-setting",
     "org": "Old Mutual Bank"},
    {"prefix": "", "value": 2, "decimals": 0, "suffix": " pp",
     "label": "Improvement in the CD2 forward roll rate since the EDC handover strategy",
     "org": "Old Mutual Bank"},
    {"prefix": "R", "value": 700, "decimals": 0, "suffix": "k",
     "label": "Collected in the Settlement Offer V1 trial campaign",
     "org": "FNB"},
]

# ---------------------------------------------------------------------------
# Technical skills
# ---------------------------------------------------------------------------
SKILLS = {
    "Programming and platforms": [
        "Python", "SQL", "SAS", "R", "PySpark", "Databricks", "Delta Lake", "AWS",
        "Cloud data lake storage", "Claude Code",
    ],
    "Data engineering": [
        "Medallion architecture", "Incremental ingestion (Auto Loader)", "Clickstream analytics",
        "Data migration and validation",
    ],
    "Machine learning": [
        "Supervised and unsupervised learning", "Predictive and statistical modelling",
        "Time series", "Neural networks", "MLOps", "MLflow",
    ],
    "Analytics and reporting": [
        "Power BI", "Excel", "Power Query", "BI dashboards", "Data extraction",
        "Campaign analytics",
    ],
    "Domain expertise": [
        "Credit risk", "Collections strategy", "Customer segmentation", "Portfolio optimisation",
    ],
}

# ---------------------------------------------------------------------------
# Experience (most recent first)
#
# Each role has:
#   highlights     - bullet points shown on the Experience page
#   achievements   - quantified results shown on the Accomplishments page
#                    (metric, label, detail)
# ---------------------------------------------------------------------------
EXPERIENCE = [
    {
        "id": "igc",
        "role": "Data Science & AI Engineer (Contract)",
        "company": "In Good Company",
        "team": "6-month data science contract",
        "start": "Oct 2026",
        "end": "Present",
        "current": True,
        "summary": (
            "Building an end-to-end e-commerce website and clickstream analytics platform for "
            "a craft cocktail company, using Claude Code agents and Databricks."
        ),
        "highlights": [
            "Developing the company's e-commerce website with Claude Code agents, translating the "
            "founder's brand, product and pricing information into a site with integrated "
            "checkout, age verification and consent management.",
            "Designing a clickstream event taxonomy and tracking layer to capture each visitor's "
            "journey through a six-stage purchase funnel, from first page view to completed "
            "purchase.",
            "Engineering a Medallion-architecture data pipeline (Bronze, Silver, Gold) in "
            "Databricks on a cloud data lake, using Auto Loader and Delta Lake for incremental "
            "ingestion, data cleaning, sessionisation and customer identity stitching.",
            "Building Gold-layer analytics tables to measure funnel drop-off, session behaviour "
            "and customer engagement, giving the founder visibility into where potential "
            "customers abandon the site.",
            "Developing an automated offer engine to issue targeted, single-use discounts based on "
            "how far customers progress before abandoning, with frequency caps, margin floors and "
            "a holdout group to measure true discount impact.",
            "Incorporating data privacy requirements (consent-gated tracking) and responsible "
            "alcohol marketing standards into the platform design.",
        ],
        "skills": ["Claude Code", "Databricks", "Delta Lake", "Auto Loader", "PySpark",
                   "Clickstream analytics", "Experimentation"],
        "achievements": [
            ("6-stage", "Purchase funnel instrumented",
             "Event taxonomy and tracking layer covering every step from first page view to "
             "completed purchase."),
            ("3-layer", "Medallion pipeline (Bronze → Silver → Gold)",
             "Incremental ingestion, sessionisation and identity stitching on Databricks."),
        ],
    },
    {
        "id": "omb",
        "role": "Manager and Senior Quantitative Analyst",
        "company": "Old Mutual Bank",
        "team": "Collections and ECM Strategy",
        "start": "Apr 2026",
        "end": "Present",
        "current": True,
        "summary": (
            "Leading collections strategy design, dialler prioritisation, target-setting "
            "automation and KRI reporting across the unsecured lending book."
        ),
        "highlights": [
            "Designed and implemented the CD0–CD1 intra-cycle inflow strategy, prioritising the "
            "pre-delinquent loan book in the dialler queue and introducing new call guides for "
            "agents. Promise-to-pay (PTP) arrangements rose by 45% in the first month with kept "
            "rates holding steady, and deterioration of the pre-delinquent unsecured loan "
            "portfolio has slowed by 6% since implementation in June 2026.",
            "Automated the Active Collections PTP target-setting framework, replacing a manual "
            "process and increasing arrangement volumes by 17% in its first month. Monthly targets "
            "now account for agent headcount and capacity, keeping them achievable for Old Mutual "
            "Finance (OMF) dialler teams while still set to materially improve collections "
            "performance.",
            "Developed a risk-based CD1 dialler prioritisation strategy targeting newly delinquent "
            "accounts, which make up 30% of CD1 loans but drive approximately 70% of forward "
            "rolls. New OMF CD1 inflows holding an Old Mutual Bank account are routed to Amazon "
            "Connect, with remaining accounts following the CD0–CD1 prioritisation queues, to "
            "limit progression into deeper arrears.",
            "Built an integrated collections KRI and performance dashboard tracking debit order "
            "strikes, collections productivity and PTP arrangements, enabling tactical changes to "
            "operations, including flagging high-risk accounts without a DebiCheck mandate so the "
            "DebiCheck team can reinstate mandates and contain forward roll rates.",
            "Supporting the migration of collections data from IBM AS/400 to AWS through code "
            "optimisation, staging-table testing and validation. Over 50% of collections tables "
            "have been migrated and validated, with the remaining staging tables due by November "
            "2026 and report automation by mid-December 2026.",
            "Developed an early external debt collector (EDC) handover strategy for CD2 accounts, "
            "projected to lift activations by 5–10% and improve the CD2 forward roll rate by "
            "0.98–1.96 percentage points. Since implementation in October 2026, activation rates "
            "on escalated accounts have doubled to over 10.75% (versus 5.21% for the holdout "
            "sample) and forward roll rates have improved by 2 percentage points, in line with "
            "pre-implementation estimates; full performance results are due in November 2026.",
            "Built automated Money Account incentive tracking and daily collections risk "
            "dashboards covering DebiCheck conversions, commission payables, debit order outcomes "
            "and channel performance, identifying underperforming branch agents and forecasting "
            "commission payments before the end of each collections cycle.",
        ],
        "skills": ["SQL", "SAS", "Python", "Power BI", "AWS", "Dialler strategy",
                   "Champion/challenger testing"],
        "achievements": [
            ("+45%", "PTP arrangements: CD0–CD1 inflow strategy",
             "First-month uplift with kept rates holding steady; pre-delinquent book "
             "deterioration slowed by 6% since June 2026."),
            ("+17%", "Arrangement volumes: automated PTP targets",
             "Replaced a manual target-setting process with capacity-aware monthly targets."),
            ("10.75% vs 5.21%", "CD2 activation rate: EDC handover vs holdout",
             "Activation rates on escalated accounts doubled; forward roll rate improved by "
             "2 percentage points."),
            ("30% → 70%", "Share of CD1 loans → share of forward rolls",
             "Risk-based CD1 prioritisation targets the newly delinquent accounts driving most "
             "roll-forward."),
            ("50%+", "Collections tables migrated to AWS",
             "AS/400 → AWS migration, with staging-table testing and validation."),
        ],
    },
    {
        "id": "abl",
        "role": "Manager: Collections Strategy",
        "company": "African Bank",
        "team": "Collections and Payments",
        "start": "Aug 2025",
        "end": "Apr 2026",
        "current": False,
        "summary": (
            "Portfolio diagnostics, cross-credit-obligation analysis and competitive "
            "benchmarking to shape collections and restructure strategy."
        ),
        "highlights": [
            "Analysed the portfolio, identifying high-risk bureau ratings across over 50% of the "
            "book and 47% monthly instalment compliance; findings informed provisioning and "
            "segmentation strategy.",
            "Developed cross-credit-obligation analysis to identify customers meeting commitments "
            "elsewhere, supporting targeted messaging and collections interventions.",
            "Benchmarked restructure offerings across major South African retail banks and "
            "presented product gaps and strategy recommendations.",
        ],
        "skills": ["SQL", "Bureau data", "Segmentation", "Competitive analysis"],
        "achievements": [
            ("50%+", "Of the book flagged with high-risk bureau ratings",
             "Portfolio diagnostic that informed provisioning and segmentation strategy."),
        ],
    },
    {
        "id": "fnb2",
        "role": "Data Scientist II",
        "company": "FNB",
        "team": "Dynamic Decisioning Collections Analytics",
        "start": "Nov 2024",
        "end": "Jul 2025",
        "current": False,
        "summary": (
            "Led the second-generation settlement offer ML model and owned campaign analytics "
            "end to end."
        ),
        "highlights": [
            "Led development of the Settlement Offer ML V2 Model for residual and debt review "
            "customers across Card and Loans, generating R2.3 million in collections on its first "
            "implementation.",
            "Engineered a longitudinal arrears movement feature for senior stakeholder dashboards "
            "to track delinquency migration and book stabilisation cycles.",
            "Managed campaign analytics end to end, from design and deployment to customer "
            "interaction tracking and payment conversion measurement.",
        ],
        "skills": ["Python", "SAS", "SQL", "Machine learning", "Feature engineering",
                   "Campaign analytics"],
        "achievements": [
            ("R2.3m", "Collections: Settlement Offer ML V2",
             "Generated on first implementation across Card and Loans."),
        ],
    },
    {
        "id": "fnb1",
        "role": "Data Scientist I",
        "company": "FNB",
        "team": "Dynamic Decisioning Collections Analytics",
        "start": "Jan 2023",
        "end": "Oct 2024",
        "current": False,
        "summary": (
            "Built the first settlement offer model and core collections features and "
            "automation."
        ),
        "highlights": [
            "Built the V1 Settlement Offer Model to estimate expected settlement values for "
            "late-stage and debt review accounts; the trial campaign generated approximately "
            "R700,000 in collections.",
            "Developed a minimum payment feature calculating the payment required to improve an "
            "account's arrears cycle, supporting collections communications.",
            "Automated call centre dialler lead provisioning and analysed the relationship "
            "between prime rates and default rates across the FNB Retail credit portfolio.",
        ],
        "skills": ["Python", "SAS", "SQL", "Predictive modelling", "Automation"],
        "achievements": [
            ("R700k", "Collections: Settlement Offer V1 trial",
             "Trial campaign for late-stage and debt review accounts."),
        ],
    },
    {
        "id": "fnb0",
        "role": "Quantitative Analyst Graduate Programme",
        "company": "FNB",
        "team": "Dynamic Decisioning Collections Analytics",
        "start": "Jan 2022",
        "end": "Dec 2022",
        "current": False,
        "summary": "Graduate rotations across collections analytics.",
        "highlights": [
            "Completed collections analytics rotations, building experience across the "
            "data-to-strategy pipeline that supports production decisioning systems.",
        ],
        "skills": ["SAS", "SQL", "Collections analytics"],
        "achievements": [],
    },
]

# ---------------------------------------------------------------------------
# Education
# ---------------------------------------------------------------------------
EDUCATION = [
    {
        "degree": "BCom Master Financial Engineering",
        "institution": "University of Johannesburg",
        "period": "2025 – Present",
        "note": "Minor dissertation submitted November 2026.",
        "has_research": True,
    },
    {
        "degree": "BSc Honours Actuarial Science",
        "institution": "University of the Witwatersrand",
        "period": "2021",
        "note": "",
        "has_research": False,
    },
    {
        "degree": "BSc Actuarial Science and Mathematical Statistics",
        "institution": "University of the Witwatersrand",
        "period": "2018 – 2020",
        "note": "",
        "has_research": False,
    },
]

# Professional affiliations. Clicking the card on the website opens a panel listing
# the exams below. To add a newly passed exam, add it to the right stage's "subjects".
AFFILIATIONS = [
    {
        "id": "assa",
        "name": "Actuarial Society of South Africa (ASSA)",
        "designation": "TASSA",
        "designation_full": "Technical Member of the Actuarial Society of South Africa",
        "exams_title": "Board exams and exemptions obtained",
        "exam_groups": [
            {
                "stage": "A1",
                "name": "Foundational Technical",
                "subjects": [
                    ("A111", "Actuarial Statistics"),
                    ("A112", "Business Economics"),
                    ("A113", "Business Finance"),
                ],
            },
            {
                "stage": "A2",
                "name": "Intermediate Technical",
                "subjects": [
                    ("A211", "Financial Mathematics"),
                    ("A212", "Risk Modelling and Survival Analysis"),
                    ("A213", "Contingencies"),
                    ("A214", "Actuarial Economic Modelling"),
                ],
            },
            {
                "stage": "A3",
                "name": "Core Principles",
                "subjects": [
                    ("A311", "Actuarial Risk Management"),
                ],
            },
        ],
    },
]

# ---------------------------------------------------------------------------
# Master's research (summarised from the final dissertation)
# ---------------------------------------------------------------------------
RESEARCH = {
    "title": (
        "Sustainable Investing under ESG Knightian Uncertainty and Climate Policy "
        "Uncertainty Regime-Changes"
    ),
    "supervisors": "Prof. Jules Mba and Dr Magdalene Wilson",
    "keywords": [
        "ESG ambiguity", "Knightian uncertainty", "Robust portfolio optimisation",
        "Time-consistent portfolio selection", "Mean-CVaR", "Climate policy uncertainty",
        "Regime switching", "Machine learning",
    ],
    "problem": (
        "ESG ratings are increasingly used to build portfolios, but different rating agencies "
        "often disagree sharply about the same company (correlations of only 0.38–0.71), and "
        "the probabilities of climate-related outcomes are unknown. ESG information is therefore "
        "better treated as **ambiguity** (Knightian uncertainty) than as measurable risk. "
        "Traditional portfolio models assume expected returns are known, and they usually add "
        "ESG as a hard constraint, so they cannot represent this ambiguity. This helps explain "
        "why past studies disagree on whether ESG investing helps or hurts performance."
    ),
    "approach": [
        "**Knightian framing:** ESG rating disagreement is modelled as uncertainty about each "
        "stock's expected return. Uncertainty sets built from ESG scores replace a fixed ESG "
        "constraint.",
        "**Two new robust frameworks:** the single-period ESG-robust Mean-Variance model of "
        "Müller and Joubrel (2025) is extended to a **multi-period, time-consistent** setting "
        "with an **ellipsoidal** uncertainty set. A new ESG-robust **Mean-CVaR** framework with "
        "a **box** uncertainty set is also built to target tail risk directly.",
        "**Climate policy regimes:** the size of the ambiguity set is scaled by the Climate "
        "Policy Uncertainty (CPU) index. High- and low-CPU regimes are identified with a "
        "two-state **Markov-switching** model.",
        "**Machine learning return forecasts:** expected returns come from 60-month historical "
        "means or from **Random Forest** and **XGBoost** models (with and without the CPU regime "
        "probability as a feature, plus an equal-weighted ensemble).",
        "**Large-scale empirical test:** **1,000 simulated portfolios** of STOXX Europe 600 "
        "constituents from 2010 to 2025, evaluated in-sample and out-of-sample "
        "(2019–2025) across a grid of risk-aversion and ambiguity-aversion levels.",
    ],
    "findings": [
        ("Consistent sustainability tilt",
         "Every ESG-robust framework tilted significantly towards sustainable stocks in every "
         "combination of risk and ambiguity aversion. The tilt grew as ambiguity aversion "
         "increased. ESG ambiguity alone produces greener portfolios, without imposing an ESG "
         "target."),
        ("Mean-Variance: greener and better",
         "With historical means, the ESG-robust Mean-Variance framework improved risk-adjusted "
         "returns in 95% of combinations in-sample and in 100% out-of-sample. It also improved "
         "tail risk and turnover, adding 4–8 ESG points at no performance cost."),
        ("Mean-CVaR: bigger tilt, at a cost",
         "The box uncertainty set produced a 2–3× larger tilt (12–21 ESG points), but it never "
         "meaningfully improved the Sharpe ratio. With machine learning forecasts it lowered the "
         "Sharpe ratio in 44% of combinations and raised tail risk in 83%."),
        ("Inputs and geometry matter",
         "The machine learning forecasts beat the historical mean out-of-sample "
         "(out-of-sample R² of 0.67%–1.22%). Even so, performance gains were smaller with these "
         "forecasts. The financial outcome depends on the shape of the uncertainty set, the risk "
         "measure and the quality of the expected-return inputs."),
        ("Climate policy regimes added no value",
         "Scaling ambiguity by CPU raised the tilt only marginally and did not improve "
         "performance. Contrary to the hypothesis, the gains were not concentrated in "
         "high-policy-uncertainty periods."),
        ("Sound model behaviour",
         "Setting the ambiguity radius to zero recovered the non-robust benchmark exactly, as "
         "theory requires. This was confirmed numerically for both frameworks."),
    ],
    "conclusion": (
        "Treating ESG information as ambiguity reliably produces more sustainable portfolios. "
        "The ellipsoidal Mean-Variance framework delivers that tilt with no loss, and often a "
        "gain, in risk-adjusted performance. The box-constrained Mean-CVaR framework, in its "
        "current form, does not."
    ),
    "future_work": [
        "Test alternative uncertainty sets for Mean-CVaR: ellipsoidal (second-order cone), "
        "budgeted polyhedral (Bertsimas & Sim), Wasserstein ambiguity sets and asymmetric "
        "downside-only sets.",
        "Refine the CPU scaling: compare against a constant-radius control and smooth the "
        "scaling ratio.",
        "Apply the frameworks to S&P 500 constituents to test whether the results differ "
        "between European and US investor sentiment.",
    ],
}

# ---------------------------------------------------------------------------
# Projects
#
# status: "In progress" or "Completed"
# Add new projects to this list when they are complete. Optional keys:
#   "link" (URL to a repo, demo or write-up) and "image" (path in assets/).
# ---------------------------------------------------------------------------
PROJECTS = [
    {
        "name": "E-commerce Website & Clickstream Analytics Platform",
        "client": "In Good Company (craft cocktail company)",
        "status": "In progress",
        "period": "Oct 2026 – Present",
        "description": (
            "An end-to-end e-commerce website built with Claude Code agents, together with a "
            "Databricks Medallion pipeline that turns clickstream data into funnel, session "
            "and engagement analytics, plus an automated offer engine to recover abandoning "
            "customers."
        ),
        "stack": ["Claude Code", "Databricks", "Delta Lake", "Auto Loader", "PySpark"],
        "link": "",
    },
    {
        "name": "Credit Risk ML Platform",
        "client": "Personal Project",
        "status": "Completed",
        "period": "Nov 2026",
        "description": (
            "An end-to-end probability-of-default platform on 307,511 Home Credit loans: a LightGBM "
            "model managed in MLflow, a FastAPI scoring service with reason codes, and an interactive "
            "dashboard for portfolio, strategy and drift monitoring."
        ),
        "stack": ["LightGBM", "MLflow", "FastAPI", "Streamlit", "Docker"],
        # Internal links (no "http") open in the same tab; see templates/index.html.
        "link": "projects/credit-risk/",
        "link_text": "Explore the live dashboard →",
    },
]

# ---------------------------------------------------------------------------
# Credit Risk ML Platform: project pages at /projects/credit-risk/<page>/
#
# Each page embeds one page of the Streamlit dashboard. "path" is the page's URL path on
# Streamlit Cloud. "?site=1" tells the dashboard to hide its own sidebar and menu, because
# the tabs on these pages handle navigation.
# ---------------------------------------------------------------------------
CREDIT_RISK = {
    "name": "Credit Risk ML Platform",
    "label": "Personal Project",
    "status": "Completed",
    "period": "Nov 2026",
    "intro": (
        "Predicts the probability that a consumer loan defaults, then turns it into decisions: "
        "risk grades, approval cut-offs, collections priorities and drift alerts. The model, API "
        "and dashboard below are live."
    ),
    "highlights": [
        ("0.769", "Test AUC"),
        ("0.537", "Gini"),
        ("3.5x", "Lift in the riskiest 10%"),
        ("307,511", "Loans modelled"),
    ],
    "stack": ["Python", "LightGBM", "scikit-learn", "SHAP", "MLflow", "FastAPI", "Streamlit",
              "Docker", "GitHub Actions"],
    "dashboard_url": "https://rl-credit-risk-platform.streamlit.app",
    "api_docs": "https://credit-risk-api-pdf9.onrender.com/docs",
    "github": "https://github.com/Reorapetse-Molefe99/credit-risk-ml-platform",
    # Each page: "about" (paragraphs above the dashboard), optional "sections" (extra text and tables
    # below it), and the "controls" and "variables" guide tables, as (name, meaning, effect) rows.
    # Real-data results are aggregates of the 61,503-loan test split; no loan-level data is published.
    "pages": [
        {
            "slug": "", "tab": "Overview", "path": "",
            "title": "Overview",
            "summary": "What the project does, what each dashboard is for, the data behind it, how the model "
                       "performed, and the regulatory context.",
            "about": [
                "An end-to-end credit risk platform, built the way a bank would run one. A machine-learning "
                "model predicts each applicant's **probability of default (PD)**: the chance they will struggle "
                "to repay. The platform turns that into risk grades, credit decisions, approval and collections "
                "strategies, and drift alerts, and explains every score.",
                "Behind the dashboards: a LightGBM **champion model** trained on 196,806 loans and tested on 61,503 "
                "it never saw, managed in MLflow, served by a FastAPI scoring service in Docker, and checked by "
                "automated tests on every change.",
            ],
            "sections": [
                {
                    "title": "What each dashboard is for",
                    "head": ["Tab", "Question it answers", "Typically used by"],
                    "rows": [
                        ("Portfolio", "How risky is the book, and where is the risk concentrated?", "Risk managers"),
                        ("Customer Scoring", "Should we lend to this applicant, and why?", "Credit officers"),
                        ("Model Performance", "Is the model accurate, and can its PDs be trusted?",
                         "Model validators"),
                        ("Strategy Simulator", "Where should the approval cut-off be, and whom should collections "
                         "call first?", "Credit strategy and collections teams"),
                        ("Model Monitoring", "Are applicants changing in a way that breaks the model?",
                         "Model risk and MLOps teams"),
                    ],
                },
                {
                    "title": "About the data",
                    "paragraphs": [
                        "The model was built on the Home Credit Default Risk data: 307,511 consumer loans with an "
                        "8.07% default rate. The competition's terms don't allow the data to be redistributed, so "
                        "the live demo scores 5,000 **simulated** applications instead. They have the real test set's "
                        "risk mix, but their outcomes are deliberately noisier. The model still performs well on "
                        "them (AUC about 0.70, against 0.769 on the real data), but less well than on its own test "
                        "set, as models do on new data. No real loan is published.",
                        "**Currency:** the data doesn't say. Amounts are in the lender's local currency, and even the "
                        "credit bureau's currency field is anonymised as \"currency 1\" to \"currency 4\". The "
                        "dashboards therefore show amounts as plain numbers, not rand or dollars.",
                    ],
                },
                {
                    "title": "How the model performed on the real data",
                    "paragraphs": ["61,503 held-out loans, shared here only as summary figures."],
                    "head": ["Measure", "Result", "What it means"],
                    "rows": [
                        ("Ranking power (AUC / Gini)", "0.769 / 0.537",
                         "Strong for an application scorecard (typical AUC: 0.70–0.80)."),
                        ("Separation (KS)", "0.400", "Good separation of defaulters from non-defaulters."),
                        ("Calibration", "8.00% predicted vs 8.07% actual", "PDs can be taken at face value."),
                        ("Riskiest 10% of applicants", "35.5% of all defaults", "3.5x better than random."),
                        ("Riskiest 20% of applicants", "54% of all defaults", "2.7x better than random."),
                        ("Riskiest vs safest tenth", "28.6% vs 1.1% default rate",
                         "Risk falls steadily from decile to decile."),
                        ("Validation vs test AUC", "0.763 vs 0.769", "Holds up on unseen data: no over-fitting."),
                        ("Challenger models (test AUC)", "Logistic regression 0.751, random forest 0.747",
                         "LightGBM was best on validation, so it became champion."),
                        ("Decisions (approve < 10% PD, decline ≥ 20%)",
                         "Approve 74.8%, refer 16.8%, decline 8.4%",
                         "Declined applicants default 7x as often as approved ones (30.3% vs 4.2%)."),
                    ],
                },
                {
                    "title": "Predicted vs actual default rate by risk grade",
                    "head": ["Grade", "Share of loans", "Predicted PD", "Actual default rate"],
                    "rows": [
                        ("A (PD < 2%)", "15.0%", "1.4%", "1.3%"),
                        ("B (2–5%)", "34.1%", "3.4%", "3.3%"),
                        ("C (5–10%)", "25.7%", "7.1%", "7.3%"),
                        ("D (10–20%)", "16.8%", "13.9%", "14.0%"),
                        ("E (20% or more)", "8.4%", "29.8%", "30.3%"),
                    ],
                    "caption": "Predicted and actual rates agree within half a percentage point in every "
                               "grade, so the grades can be used for pricing and limits.",
                },
                {
                    "title": "Regulation: South Africa vs the United States",
                    "paragraphs": [
                        "Credit default models are regulated differently in the two countries. Neither prescribes "
                        "an algorithm: both expect models to be validated, governed and explainable. They differ "
                        "in who approves the models and what they are used for.",
                    ],
                    "head": ["", "South Africa", "United States"],
                    "rows": [
                        ("Regulators", "Prudential Authority (South African Reserve Bank); National Credit "
                         "Regulator for consumer lending.", "Federal Reserve, OCC and FDIC; CFPB for consumer "
                         "lending."),
                        ("PD models for capital", "Basel III. Banks use standardised rules or internal "
                         "(IRB) models approved by the Prudential Authority; the large banks use IRB.",
                         "Internal models only at the largest banks; most use standardised rules. A 2023 "
                         "proposal would replace internal credit models with standardised rules."),
                        ("Loss provisions", "IFRS 9 expected credit loss (12-month or lifetime).",
                         "CECL: lifetime expected credit loss."),
                        ("Model governance", "Basel IRB minimum standards: independent validation, data history "
                         "and supervisory approval of material changes.",
                         "SR 11-7 / OCC 2011-12 model risk guidance: sound development, independent "
                         "validation and governance."),
                        ("Customer protection", "National Credit Act: affordability checks, no reckless lending. "
                         "POPIA restricts credit decisions based solely on automated processing.",
                         "ECOA / Regulation B: specific reasons for every decline, even from complex models. "
                         "Fair-lending rules ban discriminatory outcomes."),
                        ("Flexibility in model type", "Lower for capital models: they must be approved, stable and "
                         "explainable, so logistic-regression scorecards dominate. Machine learning is used more "
                         "for IFRS 9, decisioning and challenger models.",
                         "Higher: machine learning is common in underwriting, provided it is validated and can "
                         "give specific decline reasons."),
                    ],
                    "caption": "A short, high-level summary, not legal advice. This project follows these "
                               "expectations (hold-out validation, reason codes, gender excluded) but hasn't been "
                               "through any regulatory approval.",
                },
            ],
            "controls": [],
            "variables": [
                ("Champion model", "Model version in production (v2, LightGBM).",
                 "Replaced only by a model that beats it on hold-out checks."),
                ("Test AUC", "Chance a defaulter gets a higher PD than a non-defaulter.",
                 "0.5 is random and 1.0 is perfect. Higher is better."),
                ("Gini", "2 × AUC − 1, the form banks report.", "0 is random and 1 is perfect."),
                ("KS", "Largest gap between the score distributions of defaulters and non-defaulters.",
                 "Above 0.40 is good."),
                ("Portfolio", "Applications scored on the other tabs.",
                 "5,000 simulated applications in the demo."),
            ],
        },
        {
            "slug": "portfolio", "tab": "Portfolio", "path": "Portfolio_Overview",
            "title": "Portfolio overview",
            "summary": "Risk-grade mix, PD distribution, expected loss and default rates by segment.",
            "about": [
                "A risk manager's view of the whole book: how applications spread across risk grades, how much "
                "the portfolio is expected to lose, and which segments carry the most risk. Each application's "
                "**probability of default (PD)** sets its grade (A to E) and decision.",
            ],
            "controls": [
                ("Loss given default (LGD)", "Share of a defaulted loan that is lost (0–100%, default 45%).",
                 "Only expected loss changes, in proportion. PDs, grades and decisions stay the same."),
                ("Segment by", "Customer attribute used to split the portfolio.",
                 "Redraws the segment chart and table. Segments under 30 applications are hidden."),
            ],
            "variables": [
                ("Applications", "Number of applications scored.", "Context for the other numbers."),
                ("Mean PD", "Average predicted default probability.", "Higher means a riskier book."),
                ("Observed default rate", "Share that actually defaulted.",
                 "Close to mean PD means well calibrated (simulated outcomes in the demo)."),
                ("Exposure", "Total loan amount.", "The money at risk."),
                ("Expected loss", "Sum of PD × LGD × loan amount, also as a share of exposure.",
                 "Rises with risk or LGD."),
                ("Risk grades chart", "Applications per grade (bars), with mean PD and observed default rate "
                 "(lines).", "Both lines should rise from A to E and stay close together."),
                ("PD distribution", "PDs of loans that defaulted vs loans that did not.",
                 "Less overlap means better separation."),
                ("Segment chart and table", "Predicted and observed default rates, and expected loss, by segment.",
                 "Observed well above predicted means the model under-predicts that segment."),
                ("Decision mix", "Approve (PD < 10%), refer (10–20%) and decline (20% or more).",
                 "Try other cut-offs on the Strategy Simulator tab."),
            ],
        },
        {
            "slug": "scoring", "tab": "Customer Scoring", "path": "Customer_Scoring",
            "title": "Customer scoring",
            "summary": "Score a portfolio applicant or a new application through the live API, with a "
                       "risk grade, a decision and SHAP reason codes.",
            "about": [
                "Scores one customer through the live API, which returns the probability of default, risk grade "
                "and decision. The **reason codes** show which details pushed the risk up or down, which lenders "
                "need to explain a decline.",
            ],
            "controls": [
                ("Applicant ID and random buttons", "Pick a portfolio applicant, or a random (defaulting) one.",
                 "Rescores the applicant and shows the actual outcome."),
                ("New application form", "A hypothetical applicant, scored when you press Score application.",
                 "Missing fields are imputed. The effects below are from a default applicant with a PD of about "
                 "11%."),
                ("External scores 1–3", "Credit bureau scores (0–1). Untick if unavailable.",
                 "The strongest inputs. Score 3 at 0.80 gives a PD of about 5%, and at 0.20 about 23%."),
                ("Annual repayment", "Yearly instalment.", "Higher for the same loan raises the PD (45,000: 15%)."),
                ("Loan amount and goods price", "Amount borrowed and the price of what it finances.",
                 "Borrowing well above the goods price raises the PD (goods price 350,000: 16%)."),
                ("Years in current job", "Employment tenure.", "Longer lowers the PD (1 year: 15%, 15 years: 8%)."),
                ("Education, contract type, region and other profile fields", "Applicant profile.",
                 "Moderate effects. For example, higher education gives 7%. Income and age on their own move "
                 "the PD by under 3 points."),
            ],
            "variables": [
                ("Probability of default", "Estimated chance of payment difficulties.",
                 "Coloured bands mark the grade boundaries."),
                ("Risk grade", "A (< 2%), B (< 5%), C (< 10%), D (< 20%) or E.", "Sets pricing and limits."),
                ("Decision", "Approve below 10% PD, refer at 10–20%, decline at 20% or more.",
                 "Refer means a person reviews the application."),
                ("Riskier than", "Share of the portfolio with a lower PD.", "86% means riskier than 86% of applicants."),
                ("Actual outcome", "Whether this loan really defaulted.",
                 "A 10% PD means about 1 in 10 similar applicants default."),
                ("Reason codes", "Each feature's push on the score (SHAP).",
                 "Red raises risk and green lowers it. Longer bars matter more."),
                ("Credit- and repayment-to-income", "Loan ÷ income and repayment ÷ income.",
                 "Higher means a heavier debt burden."),
                ("Scored via", "Source of the score.", "API: live service. In-process: the API was asleep."),
            ],
        },
        {
            "slug": "performance", "tab": "Model Performance", "path": "Model_Performance",
            "title": "Model performance",
            "summary": "Discrimination, calibration, rank ordering, a confusion matrix at any cut-off "
                       "and global SHAP importance.",
            "about": [
                "How well the model ranks risk, and whether its probabilities can be trusted. The headline "
                "metrics, ROC, calibration and deciles come from the **real 61,503-loan test set**. The "
                "confusion matrix and SHAP chart use the portfolio shown (synthetic in the demo).",
            ],
            "controls": [
                ("Flag as high risk if PD ≥", "Cut-off for a high-risk flag (2–50%, default 10%).",
                 "Lower: more loans flagged, recall up, precision down. Higher: the opposite."),
                ("Model registry", "Model versions from MLflow.", "Not available on the public site."),
            ],
            "variables": [
                ("ROC AUC, Gini, KS", "Ranking power.", "Higher is better."),
                ("PR AUC", "Precision–recall area, suited to rare events.", "A random model scores about 0.08."),
                ("Brier score and log-loss", "Prediction error.", "Lower is better."),
                ("Mean PD vs observed", "Average predicted vs actual default rate.", "Close values mean calibrated."),
                ("Recall and lift at top 10%", "Share of defaults among the riskiest 10%, and the multiple "
                 "over random.", "35.5% and 3.55x."),
                ("ROC curve", "Defaulters caught vs good customers flagged, at every cut-off.",
                 "Further above the diagonal is better."),
                ("Calibration chart", "Predicted vs observed default rate in ten bands.",
                 "On the diagonal means PDs are accurate."),
                ("Deciles", "Loans in ten equal groups by PD (1 = riskiest).",
                 "Default rate should fall steadily from 1 to 10."),
                ("Confusion matrix", "Good loans passed or flagged, defaults missed or caught.",
                 "Moving the cut-off shifts loans between columns."),
                ("Recall, precision, share flagged", "Defaulters flagged, flagged who default, and loans flagged.",
                 "Accuracy is omitted: approving everyone is 92% 'accurate'."),
                ("Global SHAP importance", "Average influence of each feature.",
                 "Longer bars matter more. Colour shows the usual direction."),
                ("Validation vs test", "Metrics on the tuning data vs untouched data.",
                 "Similar values mean no over-fitting."),
            ],
        },
        {
            "slug": "strategy", "tab": "Strategy Simulator", "path": "Strategy_Simulator",
            "title": "Strategy simulator",
            "summary": "Approval cut-off trade-offs between growth, bad rate and profit, and "
                       "risk-based collections prioritisation.",
            "about": [
                "Turns scores into decisions. **Approval strategy** trades growth against risk and profit as the "
                "cut-off moves. A loan earns margin × term × amount if it performs and loses LGD × amount if it "
                "defaults. **Collections prioritisation** shows the gain from working the riskiest loans first.",
            ],
            "controls": [
                ("Approve if PD below", "Approval cut-off (1–50%, default 10%).",
                 "Higher: more approvals, higher bad rate and loss. Profit peaks at the best cut-off."),
                ("Loss given default (LGD)", "Share lost on a default (5–100%, default 45%).",
                 "Higher: more loss, less profit, stricter optimal cut-off."),
                ("Net interest margin", "Yearly income on performing loans (0–40%, default 12%).",
                 "Higher: more profit, more lenient optimal cut-off."),
                ("Term (years)", "Years the margin is earned (0.5–5, default 1).", "Works like the margin."),
                ("Collections capacity", "Share of the book the team can work (1–50%, default 20%).",
                 "More capacity: higher capture, lower lift."),
            ],
            "variables": [
                ("Approval rate", "Share of applications approved.", "The growth side of the trade-off."),
                ("Bad rate (approved)", "Default rate among approved loans, vs approving everyone.",
                 "Negative change means risk is being filtered out."),
                ("Defaults avoided", "Share of all defaulters declined.", "Higher means fewer losses."),
                ("Expected loss", "Sum of PD × LGD × amount over approved loans.", "Rises with the cut-off and LGD."),
                ("Realised profit", "Profit from actual outcomes, vs approving everyone.",
                 "Positive means the cut-off beats lending to all."),
                ("Profit by cut-off", "Expected and realised profit at every cut-off.",
                 "Green line: maximum profit. Close curves mean PDs are reliable."),
                ("Strategy curve", "Approval rate vs bad rate for every cut-off.",
                 "A steep end means the last approvals are much riskier."),
                ("Break-even PD", "margin × term ÷ (margin × term + LGD).", "Loans above it lose money on average."),
                ("Default capture and random capture", "Share of defaults among the loans worked, vs a random "
                 "pick.", "The gap is the value of the model."),
                ("Prioritisation lift", "Capture ÷ random capture.", "2x means twice as many defaults found."),
                ("Cumulative gains chart", "Defaults captured as more loans are worked.",
                 "Closer to perfect foresight is better. Capture is not prevention."),
            ],
        },
        {
            "slug": "monitoring", "tab": "Model Monitoring", "path": "Model_Monitoring",
            "title": "Model monitoring",
            "summary": "Population stability of scores and features, with simulated recession and "
                       "bureau-deterioration scenarios.",
            "about": [
                "Checks whether today's applicants still look like the ones the model was built on, using the "
                "**Population Stability Index (PSI)**. Simulated scenarios show which alarms fire. They have no "
                "outcomes, so only data and score drift are shown.",
            ],
            "controls": [
                ("Current population", "Hold-out portfolio, a simulated scenario, or your own CSV (not stored).",
                 "Sets what is compared with the reference."),
                ("Scenario", "Income shock, bureau deterioration, thin-file growth, recession or custom.",
                 "Presets fill the sliders. Custom unlocks them."),
                ("Income shock", "Scales incomes (−50% to +50%).",
                 "Income PSI alerts, but the score barely moves (score PSI 0.001 on the real data)."),
                ("Bureau score shift", "Moves all bureau scores (−0.30 to +0.30).",
                 "Negative: PDs rise, grades shift to D and E, score PSI alerts (0.27 on the real data)."),
                ("Missing bureau scores", "Removes scores for a share of applicants (0–80%).",
                 "Missing-rate alerts fire even when PSI stays low."),
            ],
            "variables": [
                ("Score PSI", "Shift in the PD distribution.", "Below 0.10 stable, 0.10–0.25 monitor, above 0.25 act."),
                ("Mean PD", "Average PD now, vs the reference.", "Up means riskier applicants."),
                ("Features in alert and warning", "Inputs past the drift thresholds.", "Investigate these first."),
                ("Observed default rate", "Actual default rate (hold-out portfolio only).",
                 "Simulated data has no outcomes."),
                ("Score distribution", "PDs of the reference and current populations.",
                 "A shift right means riskier applicants."),
                ("Grade migration", "Share in each grade, reference vs current.", "A move towards D and E is a warning."),
                ("Feature stability", "PSI and missing rates per input.",
                 "Status is the worse of the PSI and missing-rate checks."),
            ],
        },
    ],
}
