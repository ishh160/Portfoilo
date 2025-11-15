import streamlit as st
import math

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Isha Patel | Data Science Portfolio",
    page_icon="📊",
    layout="wide"
)

# =========================
# CUSTOM STYLES
# =========================
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f7;
    }
    .hero-wrapper {
        margin-top: 0.5rem;
        margin-bottom: 2rem;
    }
    .hero {
        padding: 1.8rem 1.8rem 1.4rem 1.8rem;
        border-radius: 1.5rem;
        background: linear-gradient(110deg, #D1FAFF 0%, #DB7F8E 35%, #B497D6 85%);
        box-shadow: 0 18px 45px rgba(15, 23, 42, 0.12);
        color: #0f172a;
    }
    .hero-title {
        font-size: 2.6rem;
        font-weight: 700;
        margin-bottom: 0.25rem;
        color: #0f172a;
    }
    .hero-subtitle {
        font-size: 1.1rem;
        color: #111827;
        margin-bottom: 0.65rem;
    }
    .hero-text {
        font-size: 0.98rem;
        color: #1f2937;
        max-width: 520px;
    }
    .pill {
        display: inline-block;
        padding: 0.22rem 0.8rem;
        border-radius: 999px;
        font-size: 0.78rem;
        margin-right: 0.35rem;
        margin-top: 0.35rem;
        border: 1px solid rgba(15,23,42,0.12);
        background-color: rgba(255,255,255,0.85);
        color: #111827;
    }
    .hero-btn {
        display: inline-block;
        padding: 0.55rem 1.4rem;
        border-radius: 999px;
        font-size: 0.86rem;
        font-weight: 500;
        border: none;
        background-color: #0f172a;
        color: #f9fafb;
        text-decoration: none;
        margin-top: 0.6rem;
    }
    .hero-btn:hover {
        background-color: #111827;
    }
    .stats-card {
        border-radius: 1.2rem;
        background-color: #ffffff;
        padding: 1.1rem 1.4rem;
        box-shadow: 0 14px 35px rgba(15,23,42,0.12);
    }
    .stat-number {
        font-size: 1.5rem;
        font-weight: 600;
        color: #111827;
    }
    .stat-label {
        font-size: 0.8rem;
        color: #6b7280;
    }
    .tag-muted {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.18em;
        color: #6b7280;
    }
    .section-title {
        font-size: 1.45rem;
        font-weight: 600;
        margin: 0.2rem 0 0.9rem 0;
        color: #111827;
    }
    .section {
        margin-bottom: 2.3rem;
    }
    .what-item-title {
        font-weight: 600;
        font-size: 0.96rem;
        margin-bottom: 0.1rem;
        color: #111827;
    }
    .what-item-body {
        font-size: 0.86rem;
        color: #4b5563;
    }
    .project-card {
        border-radius: 1.1rem;
        padding: 0.95rem 1.05rem;
        background-color: #ffffff;
        border: 1px solid #e5e7eb;
        margin-bottom: 0.8rem;
        transition: transform 120ms ease, box-shadow 120ms ease;
    }
    .project-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 30px rgba(15,23,42,0.12);
    }
    .project-title {
        font-weight: 600;
        font-size: 0.98rem;
        margin-bottom: 0.15rem;
        color: #111827;
    }
    .project-meta {
        font-size: 0.78rem;
        color: #6b7280;
        margin-bottom: 0.2rem;
    }
    .project-body {
        font-size: 0.86rem;
        color: #374151;
        margin-bottom: 0.25rem;
    }
    .badge {
        display: inline-block;
        padding: 0.18rem 0.65rem;
        border-radius: 999px;
        font-size: 0.72rem;
        background-color: #f3f4f6;
        color: #4b5563;
        margin-right: 0.25rem;
        margin-top: 0.22rem;
    }
    .timeline-card {
        border-radius: 1.1rem;
        padding: 0.95rem 1.05rem;
        background-color: #ffffff;
        border: 1px solid #e5e7eb;
        margin-bottom: 0.7rem;
    }
    .timeline-role {
        font-weight: 600;
        font-size: 0.96rem;
        color: #111827;
    }
    .timeline-meta {
        font-size: 0.78rem;
        color: #6b7280;
        margin-bottom: 0.25rem;
    }
    .timeline-body {
        font-size: 0.86rem;
        color: #374151;
    }
    .chips {
        display: flex;
        flex-wrap: wrap;
        gap: 0.35rem;
    }
    .chip {
        padding: 0.18rem 0.7rem;
        border-radius: 999px;
        font-size: 0.78rem;
        background-color: #e5e7eb;
        color: #111827;
    }
    footer {
        font-size: 0.7rem;
        color: #9ca3af;
        padding-top: 0.8rem;
        margin-top: 1.6rem;
        border-top: 1px solid #e5e7eb;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# DATA STRUCTURES
# =========================

projects = [
    {
        "name": "FairLens AI – Fairness & Sustainability Audit for Food Products",
        "role": "Data Scientist & Project Lead",
        "summary": (
            "End-to-end ML pipeline using the Open Food Facts dataset to score food products "
            "on sustainability while checking fairness across product groups."
        ),
        "points": [
            "Engineered features from nutrition, packaging, eco-labels, and ingredients.",
            "Trained XGBoost models and evaluated with accuracy, F1, and ROC-AUC.",
            "Used SHAP and LIME to explain why a product receives a certain sustainability score.",
            "Audited fairness with AIF360 (Demographic Parity, Equal Opportunity).",
        ],
        "tech": ["Python", "Pandas", "Scikit-learn", "XGBoost", "SHAP", "LIME", "AIF360", "Streamlit"],
        "github": "https://github.com/your-username/fairlens-ai"
    },
    {
        "name": "MoMA Exhibition Helper – Predicting Artwork Selection",
        "role": "Data Scientist",
        "summary": (
            "Classification models on the MoMA artworks dataset to understand which pieces "
            "are more likely to be selected for exhibitions."
        ),
        "points": [
            "Cleaned and structured MoMA artwork metadata.",
            "Engineered features like medium, year, and artist activity period.",
            "Built models to predict exhibition selection and interpreted them with SHAP.",
        ],
        "tech": ["Python", "Pandas", "Scikit-learn", "Logistic Regression", "SHAP"],
        "github": "https://github.com/your-username/moma-exhibition-helper"
    },
    {
        "name": "Emotion Recognition from Audio – SVM Classifier",
        "role": "ML Engineer",
        "summary": (
            "Emotion classifier that uses speech recordings to predict labels like happy, "
            "sad, angry, and neutral."
        ),
        "points": [
            "Extracted MFCCs and other audio features with Librosa.",
            "Trained and tuned SVM models using cross-validation.",
            "Analysed confusion matrices to see which emotions are hardest to separate.",
        ],
        "tech": ["Python", "Librosa", "Scikit-learn", "SVM"],
        "github": "https://github.com/your-username/audio-emotion-recognition"
    },
]

skills_programming = ["Python", "Pandas", "NumPy", "Scikit-learn", "Librosa"]
skills_ml = ["Classification", "Clustering", "Anomaly detection", "SHAP", "LIME", "AIF360"]
skills_tools = ["Streamlit", "Git & GitHub", "Excel", "FastAPI (basic)", "Project & Change Management"]

# =========================
# HERO SECTION (CONCEPT A)
# =========================
with st.container():
    st.markdown('<div class="hero-wrapper">', unsafe_allow_html=True)
    col_left, col_right = st.columns([1.6, 1.1])

    with col_left:
        st.markdown('<div class="hero">', unsafe_allow_html=True)
        st.markdown('<div class="hero-title">Hey, I’m Isha.</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="hero-subtitle">I do Data Science & Machine Learning with a project manager mindset.</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="hero-text">'
            "I enjoy building end-to-end ML projects that stay honest about limitations, "
            "explain their decisions, and actually help people make choices."
            "</div>",
            unsafe_allow_html=True
        )

        # CTA button
        st.markdown(
            '<a class="hero-btn" href="#projects-section">View my work</a>',
            unsafe_allow_html=True
        )

        # Pills
        st.markdown(
            """
            <div>
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
        # Profile + stats card on the right
        st.markdown('<div class="stats-card">', unsafe_allow_html=True)
        st.image("assets/isha.jpeg", width=220)
        st.markdown("")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="stat-number">6+</div>', unsafe_allow_html=True)
            st.markdown('<div class="stat-label">ML / DS projects</div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="stat-number">3.8+</div>', unsafe_allow_html=True)
            st.markdown('<div class="stat-label">Graduate GPA</div>', unsafe_allow_html=True)

        st.markdown("")
        st.markdown('<div class="stat-number">1+ years</div>', unsafe_allow_html=True)
        st.markdown('<div class="stat-label">Professional experience (Senior daycare)</div>', unsafe_allow_html=True)
        st.caption("Pace University · Seidenberg School · New York")

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# SECTION: WHAT I DO
# =========================
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="tag-muted">Overview</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">What I focus on</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.write(
            """
            I like projects where I can own the data story from beginning to end:
            cleaning, modelling, evaluation, and figuring out how to present
            results so they actually help decisions.
            """
        )
    with col2:
        st.write(
            """
            My background mixes graduate-level data science with real operations work
            as a CACFP coordinator in a senior daycare. That keeps me grounded in
            how data flows in actual organisations.
            """
        )

    st.markdown("")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="what-item-title">ML Pipelines</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="what-item-body">End-to-end structure from data cleaning, '
            'feature engineering, and modelling to evaluation and reporting.</div>',
            unsafe_allow_html=True
        )
    with c2:
        st.markdown('<div class="what-item-title">Explainable & Fair AI</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="what-item-body">Using SHAP, LIME, and AIF360 to keep models '
            'transparent and to surface trade-offs instead of hiding them.</div>',
            unsafe_allow_html=True
        )
    with c3:
        st.markdown('<div class="what-item-title">Project / Stakeholder Communication</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="what-item-body">Turning technical work into slides, flows, and '
            'simple language for professors, teammates, or non-technical staff.</div>',
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# SECTION: PROJECTS
# =========================
with st.container():
    st.markdown('<div class="section" id="projects-section">', unsafe_allow_html=True)
    st.markdown('<div class="tag-muted">Projects</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Selected work</div>', unsafe_allow_html=True)

    for proj in projects:
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="project-title">{proj["name"]}</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="project-meta">{proj["role"]}</div>',
            unsafe_allow_html=True
        )
        st.markdown(f'<div class="project-body">{proj["summary"]}</div>', unsafe_allow_html=True)

        for p in proj["points"]:
            st.write(f"- {p}")

        if proj["github"]:
            st.markdown(
                f'<a href="{proj["github"]}" target="_blank">View on GitHub</a>',
                unsafe_allow_html=True
            )

        # Tech badges
        tech_html = "".join(
            f'<span class="badge">{t}</span>' for t in proj["tech"]
        )
        st.markdown(tech_html, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# SECTION: EXPERIENCE
# =========================
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="tag-muted">Experience</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Where I’ve applied this</div>', unsafe_allow_html=True)

    col_exp1, col_exp2 = st.columns(2)

    with col_exp1:
        st.markdown('<div class="timeline-card">', unsafe_allow_html=True)
        st.markdown('<div class="timeline-role">CACFP Coordinator – Senior Adult Daycare</div>', unsafe_allow_html=True)
        st.markdown('<div class="timeline-meta">New Jersey · Part-time</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="timeline-body">
            • Maintain CACFP food program records for state inspections.<br>
            • Clean and validate Excel data for meals, attendance, and timesheets.<br>
            • Coordinate with staff to resolve missing or inconsistent entries.<br>
            • Help translate program rules into simple checklists and flows.
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col_exp2:
        st.markdown('<div class="timeline-card">', unsafe_allow_html=True)
        st.markdown('<div class="timeline-role">Graduate Data Science Projects – Pace University</div>', unsafe_allow_html=True)
        st.markdown('<div class="timeline-meta">New York · Team-based coursework</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="timeline-body">
            • Led planning and modelling for projects like FairLens AI and CreditMate.<br>
            • Took ownership of evaluation, explainability, and presentation sections.<br>
            • Designed slides and storylines for technical and non-technical audiences.<br>
            • Answered questions on trade-offs, limitations, and future improvements.
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# SECTION: SKILLS
# =========================
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="tag-muted">Skills</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">What I work with</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("**Programming & Data**")
        st.markdown('<div class="chips">', unsafe_allow_html=True)
        for s in skills_programming:
            st.markdown(f'<span class="chip">{s}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown("**Machine Learning & AI**")
        st.markdown('<div class="chips">', unsafe_allow_html=True)
        for s in skills_ml:
            st.markdown(f'<span class="chip">{s}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with c3:
        st.markdown("**Tools & Practices**")
        st.markdown('<div class="chips">', unsafe_allow_html=True)
        for s in skills_tools:
            st.markdown(f'<span class="chip">{s}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# SECTION: CONTACT
# =========================
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="tag-muted">Contact</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Let’s connect</div>', unsafe_allow_html=True)

    st.write(
        "If you’re hiring for data science, ML, or analytics roles that need both "
        "technical depth and clear communication, I’d be happy to talk."
    )

    col_c1, col_c2 = st.columns([1.2, 1])

    with col_c1:
        st.write("📧 Email: your.email@example.com")
        st.write("🔗 LinkedIn: https://linkedin.com/in/your-profile")
        st.write("🐙 GitHub: https://github.com/your-username")

    with col_c2:
        name = st.text_input("Your name")
        email = st.text_input("Your email")
        message = st.text_area("Short message")

        if st.button("Send (demo only)"):
            st.success("Thank you for reaching out! In a real deployment this could send me an email.")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown(
    "<footer>© 2025 Isha Patel · Portfolio built with Python and Streamlit.</footer>",
    unsafe_allow_html=True
)
