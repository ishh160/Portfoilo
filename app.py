import streamlit as st
import math
# =========================
# BASIC PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Isha Patel | Data Science Portfolio",
    page_icon="📊",
    layout="wide"
)

# =========================
# CUSTOM STYLING (YOUR PALETTE)
# =========================
# Using your preferred colors:
# Light Cyan (#D1FAFF), Teal Green (#114B5F),
# Coral Pink (#DB7F8E), Deep Wine Red (#832161), Lavender (#B497D6)

st.markdown(
    """
    <style>
    .main {
        background-color: #f8fafc;
    }
    .hero {
        padding: 1.5rem 1.5rem 1rem 1.5rem;
        border-radius: 1.5rem;
        background: linear-gradient(135deg, #D1FAFF 0%, #B497D6 40%, #FFFFFF 100%);
        box-shadow: 0 18px 45px rgba(15, 23, 42, 0.08);
    }
    .hero-title {
        font-size: 2.4rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
        color: #114B5F;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        color: #1f2933;
        margin-bottom: 0.6rem;
    }
    .pill {
        display: inline-block;
        padding: 0.2rem 0.8rem;
        border-radius: 999px;
        font-size: 0.78rem;
        margin-right: 0.35rem;
        margin-bottom: 0.35rem;
        border: 1px solid rgba(17,75,95,0.14);
        background-color: rgba(255,255,255,0.65);
    }
    .section-title {
        font-size: 1.45rem;
        font-weight: 600;
        margin: 0.2rem 0 0.8rem 0;
        color: #111827;
    }
    .tag-muted {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.18em;
        color: #6b7280;
    }
    .project-card {
        border-radius: 1.2rem;
        padding: 0.9rem 1rem;
        background-color: #ffffff;
        border: 1px solid #e5e7eb;
        margin-bottom: 0.7rem;
    }
    .project-title {
        font-weight: 600;
        font-size: 0.98rem;
        margin-bottom: 0.25rem;
        color: #111827;
    }
    .project-meta {
        font-size: 0.78rem;
        color: #6b7280;
        margin-bottom: 0.25rem;
    }
    .project-body {
        font-size: 0.86rem;
        color: #374151;
    }
    .badge {
        display: inline-block;
        padding: 0.15rem 0.55rem;
        border-radius: 999px;
        font-size: 0.72rem;
        background-color: #f3f4f6;
        color: #4b5563;
        margin-right: 0.2rem;
        margin-top: 0.2rem;
    }
    .timeline-role {
        font-weight: 600;
        font-size: 0.95rem;
        color: #111827;
    }
    .timeline-meta {
        font-size: 0.78rem;
        color: #6b7280;
        margin-bottom: 0.2rem;
    }
    .timeline-body {
        font-size: 0.86rem;
        color: #374151;
    }
    footer {
        font-size: 0.7rem;
        color: #9ca3af;
        padding-top: 0.8rem;
        margin-top: 1.2rem;
        border-top: 1px solid #e5e7eb;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# SIDEBAR – QUICK NAV
# =========================
st.sidebar.title("Navigate")
page = st.sidebar.radio(
    "Go to",
    ["Overview", "Projects", "Experience", "Skills", "Snapshot"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Open to:**")
st.sidebar.markdown("- Data Scientist / ML roles")
st.sidebar.markdown("- Data Science Project Coordinator")
st.sidebar.markdown("- Analytics-focused internships")

st.sidebar.markdown("---")
st.sidebar.markdown("**Location:** New York, USA")
st.sidebar.markdown("**Degree:** M.S. in Data Science (in progress)")
st.sidebar.markdown("**GPA:** 3.8+ (current)")

# =========================
# HERO (ALWAYS ON TOP)
# =========================
with st.container():
    col_left, col_right = st.columns([1.7, 1.1])

    with col_left:
        st.markdown('<div class="hero">', unsafe_allow_html=True)
        st.markdown('<div class="hero-title">Isha Patel</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="hero-subtitle">'
            'Data Science • Machine Learning • Project & Change Management'
            '</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            """
            I am a Master’s in Data Science student who likes to build projects that do not
            stay stuck in notebooks. I care about how models behave in the real world:
            how fair they are, how interpretable they feel, and how non-technical people
            will use them in their daily work.
            """.strip()
        )

        st.markdown(
            """
            <div style="margin-top: 0.75rem;">
                <span class="pill">Machine Learning</span>
                <span class="pill">Explainable AI (SHAP / LIME)</span>
                <span class="pill">Fairness (AIF360)</span>
                <span class="pill">Python & Streamlit</span>
                <span class="pill">Project & Change Management</span>
                <span class="pill">CACFP Operations</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col_right:
        st.metric("ML / DS Projects", "6+")
        st.metric("Graduate GPA", "3.8+")
        st.metric("Professional Experience", "1+ years")
        st.caption("Pace University · Seidenberg School · New York")

        st.markdown("")
        st.write("Resume link (add real URL):")
        st.markdown("[Download my resume](https://your-resume-link-here)", unsafe_allow_html=True)

# Small spacer
st.markdown("")

# =========================
# PROJECT DICTIONARY FOR INTERACTIVE VIEW
# =========================

PROJECTS = {
    "FairLens AI – Fairness & Sustainability Audit for Food Products": {
        "role": "Data Scientist & Project Lead",
        "tech": "Python, Pandas, Scikit-learn, XGBoost, SHAP, LIME, AIF360, Neo4j, Streamlit, FastAPI",
        "summary": (
            "An end-to-end system that scores food products for sustainability while checking "
            "fairness across different product groups and labels using Open Food Facts data."
        ),
        "bullets": [
            "Engineered features from nutrition, packaging, eco labels, and ingredients.",
            "Trained XGBoost models and evaluated with accuracy, F1 score, and ROC-AUC.",
            "Used SHAP and LIME to show which nutrients or attributes drive each prediction.",
            "Audited fairness with IBM AIF360 (Demographic Parity, Equal Opportunity) to keep gaps under a defined threshold.",
            "Designed a simple interface concept so non-technical users can scan or search products and understand the score."
        ],
        "learning": (
            "I learned how to connect model performance with fairness metrics and how to explain "
            "complex model behaviour in a way that is grounded and honest for end users."
        ),
        "github": "https://github.com/your-username/fairlens-ai"
    },
    "MoMA Exhibition Helper – Predicting Artwork Selection and Interest": {
        "role": "Data Scientist",
        "tech": "Python, Pandas, Scikit-learn, Logistic Regression, SHAP",
        "summary": (
            "A project built on the MoMA artworks dataset to explore which artworks are more "
            "likely to be selected and how medium, artist, and time periods influence visibility."
        ),
        "bullets": [
            "Cleaned and structured MoMA data with a focus on artwork metadata.",
            "Engineered features such as medium, year range, and artist activity period.",
            "Trained classification models to predict exhibition selection.",
            "Used SHAP values to highlight which factors drive the probability of being featured.",
            "Prepared visual and verbal explanations suitable for non-technical stakeholders like museum staff."
        ],
        "learning": (
            "I learned to handle imbalanced data and to turn technical outputs into stories that "
            "make sense in a cultural and business context."
        ),
        "github": "https://github.com/your-username/moma-exhibition-helper"
    },
    "Emotion Recognition from Audio – SVM Classifier": {
        "role": "ML Engineer",
        "tech": "Python, Librosa, Scikit-learn, SVM",
        "summary": (
            "An emotion recognition pipeline that uses speech recordings to classify emotions "
            "such as happy, sad, angry, and neutral."
        ),
        "bullets": [
            "Extracted audio features including MFCCs, chroma, and zero crossing rate.",
            "Built an SVM classifier and tuned hyperparameters for better generalisation.",
            "Used train–test splits and cross validation to evaluate robustness.",
            "Analysed confusion matrices to understand which emotions are hardest to separate.",
        ],
        "learning": (
            "I learned how much careful feature engineering matters for audio data and how to "
            "debug misclassifications using both numbers and listening tests."
        ),
        "github": "https://github.com/your-username/audio-emotion-recognition"
    },
    "CreditMate – Smart Credit Risk Assistant": {
        "role": "Data Science Project Lead",
        "tech": "Python, Pandas, Scikit-learn, Streamlit, Project & Change Management concepts",
        "summary": (
            "A credit risk and explainability concept that combines simple rules and models so "
            "non-technical users can understand why an applicant is considered low or high risk."
        ),
        "bullets": [
            "Defined problem, stakeholders, and scope as part of an IS Project and Change Management course.",
            "Designed a pipeline that can combine scorecards, rules, and ML in a single view.",
            "Mapped out phases, risks, and communication plans for introducing such a tool to an organisation."
        ],
        "learning": (
            "I learned how to think beyond code and consider change management, resistance, and "
            "communication when introducing data-driven tools."
        ),
        "github": "https://github.com/your-username/creditmate"
    }
}

# =========================
# OVERVIEW PAGE
# =========================
if page == "Overview":
    st.markdown('<div class="tag-muted">Overview</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">What I focus on</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.write(
            """
            I like projects where I can own the data story from beginning to end:
            problem statement, cleaning, modelling, evaluation, and how to present
            the results so people can act on them.
            
            I am especially interested in:
            - Making model decisions explainable and honest.
            - Checking that models are not unfair to certain groups or patterns.
            - Turning technical work into clean slides, flows, and documentation.
            """
        )

    with col2:
        st.write(
            """
            My background is a mix of:
            - Graduate-level data science at Pace University.
            - Real operations work as a CACFP food program coordinator in a senior daycare.
            - Team projects where I handle both modelling and presentation.
            
            This combination means I pay attention to details in the dataset, but I also
            keep an eye on who is going to use the tool and what they actually need.
            """
        )

    st.markdown("")
    st.markdown('<div class="section-title">Recent focus areas</div>', unsafe_allow_html=True)
    col_a, col_b, col_c = st.columns(3)

    with col_a:
        st.markdown("**ML pipelines**")
        st.caption("End-to-end structure from data cleaning to evaluation and reporting.")

    with col_b:
        st.markdown("**Explainable AI**")
        st.caption("SHAP and LIME for local and global explanations.")

    with col_c:
        st.markdown("**Responsible AI**")
        st.caption("Fairness checks with AIF360 and transparent assumptions.")

# =========================
# PROJECTS PAGE
# =========================
elif page == "Projects":
    st.markdown('<div class="tag-muted">Projects</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Selected work</div>', unsafe_allow_html=True)

    # Quick cards list
    for name, data in PROJECTS.items():
        with st.container():
            st.markdown('<div class="project-card">', unsafe_allow_html=True)
            st.markdown(f'<div class="project-title">{name}</div>', unsafe_allow_html=True)
            st.markdown(
                f'<div class="project-meta">{data["role"]} · {data["tech"]}</div>',
                unsafe_allow_html=True
            )
            if name.startswith("FairLens AI"):
                st.image("assets/fairlens.png", caption="FairLens AI – sample dashboard", use_container_width=True)
            elif name.startswith("MoMA Exhibition Helper"):
                st.image("assets/moma.png", caption="MoMA exhibition analysis visuals", use_container_width=True)
            elif name.startswith("Emotion Recognition"):
                st.image("assets/emotion.png", caption="Emotion recognition confusion matrix", use_container_width=True)

            st.markdown(
                f'<div class="project-body">{data["summary"]}</div>',
                unsafe_allow_html=True
            )
            if data.get("github"):
                st.markdown(
                    f'<a href="{data["github"]}" target="_blank">View on GitHub</a>',
                    unsafe_allow_html=True
                )
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("")
    st.markdown("#### Project spotlight")

    project_names = list(PROJECTS.keys())
    selected_project = st.selectbox(
        "Choose a project to see more detail",
        project_names
    )

    proj = PROJECTS[selected_project]
    st.write(f"**Role:** {proj['role']}")
    st.write(f"**Tech:** {proj['tech']}")
    st.write("**What I did:**")
    for b in proj["bullets"]:
        st.write(f"- {b}")
    st.write("")
    st.write("**What I learned:**")
    st.write(proj["learning"])

# =========================
# EXPERIENCE PAGE
# =========================
elif page == "Experience":
    st.markdown('<div class="tag-muted">Experience</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Where I have worked and contributed</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="timeline-role">CACFP Coordinator – Senior Adult Daycare Center (New Jersey)</div>', unsafe_allow_html=True)
        st.markdown('<div class="timeline-meta">Part-time · Food program coordination and compliance</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="timeline-body">
            - Maintain CACFP food program records for state inspections, including meals, attendance, and timesheets.<br>
            - Clean and validate data in Excel before audits and visits.<br>
            - Coordinate with staff to fix missing or inconsistent entries.<br>
            - Help translate program rules into simple checklists for day-to-day use.
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("")
    with st.container():
        st.markdown('<div class="timeline-role">Graduate Data Science Projects – Pace University</div>', unsafe_allow_html=True)
        st.markdown('<div class="timeline-meta">Team-based coursework · New York</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="timeline-body">
            - Led project planning and communication for FairLens AI and CreditMate.<br>
            - Took responsibility for modelling, evaluation, and explanation sections.<br>
            - Designed slides and flows to present to professors and classmates.<br>
            - Practiced answering questions about design choices, limitations, and future work.
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================
# SKILLS PAGE
# =========================
elif page == "Skills":
    st.markdown('<div class="tag-muted">Skills</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">What I work with</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**Programming and Data**")
        st.write(
            """
            - Python (Pandas, NumPy, Scikit-learn)<br>
            - Data cleaning and feature engineering<br>
            - Exploratory data analysis<br>
            - Working with APIs and CSV/Excel data
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown("**Machine Learning and AI**")
        st.write(
            """
            - Classification, clustering, anomaly detection<br>
            - SHAP and LIME for explainability<br>
            - AIF360 for fairness auditing<br>
            - Model evaluation: accuracy, F1, ROC-AUC
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown("**Tools and Practices**")
        st.write(
            """
            - Streamlit for fast prototypes<br>
            - Basic FastAPI for simple APIs<br>
            - Git and GitHub for version control<br>
            - Excel for reporting and CACFP documentation<br>
            - Project and change management concepts
            """,
            unsafe_allow_html=True
        )

    st.markdown("")
    st.markdown("#### Certifications and learning")
    st.write(
        """
        - CCNA (networking fundamentals and infrastructure basics).  
        - Graduate-level courses in Machine Learning, Data Mining, and Project & Change Management.  
        - Self-study in responsible AI, fairness, and explainability.
        """
    )

# =========================
# SNAPSHOT PAGE (SHORT SUMMARY + CONTACT)
# =========================
elif page == "Snapshot":
    st.markdown('<div class="tag-muted">Snapshot</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Quick profile and contact</div>', unsafe_allow_html=True)

    col_a, col_b = st.columns([1.4, 1])

    with col_a:
        st.write(
            """
            I am building a career that sits between data science and project management.
            I enjoy the technical work of modelling, but I also like planning, structuring
            deliverables, and making sure people actually understand the results.
            """
        )

        st.write(
            """
            I am open to:
            - Data Scientist or Machine Learning internships and early-career roles.
            - Data Analyst roles with strong ownership of projects.
            - Positions where I can help connect technical teams with operations.
            """
        )
        with st.expander("💡 Beyond data"):
            st.write(
                """
                - I love designing clean, easy-to-read dashboards and slides.  
                - I’m naturally curious about how small process changes can save time in real work.  
                - Outside coursework, I enjoy mixing creativity (design, travel) with analytical thinking.
                """
            )

    with col_b:
        st.markdown("**Contact**")
        st.write("Email: your.email@example.com")
        st.write("LinkedIn: https://linkedin.com/in/your-profile")
        st.write("GitHub: https://github.com/your-username")

        name = st.text_input("Your name")
        email = st.text_input("Your email")
        message = st.text_area("Message")

        if st.button("Send (demo only)"):
            st.success("Thank you for reaching out. In a real deployment this would send me an email.")

# =========================
# FOOTER
# =========================
st.markdown(
    "<footer>© "
    + str(st.session_state.get("year", 2025))
    + " Isha Patel · Portfolio built with Python and Streamlit.</footer>",
    unsafe_allow_html=True,
)
