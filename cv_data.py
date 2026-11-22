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
    # The phone number is hidden on the public site by default to limit spam.
    # Set SHOW_PHONE = True to display it.
    "phone": "+27 (0)79 210 2948",
    "linkedin": "",  # e.g. "https://www.linkedin.com/in/your-profile" (shown when filled in)
    "github": "",  # e.g. "https://github.com/your-username" (shown when filled in)
    "photo": "static/img/portrait.jpg",
    "cv_pdf": "static/cv/Reorapetse_Molefe_CV.pdf",
    "cv_updated": "November 2026",
}
SHOW_PHONE = False

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
        ("Member", "Actuarial Society of South Africa"),
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

AFFILIATIONS = ["Actuarial Society of South Africa (ASSA)"]

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
]
