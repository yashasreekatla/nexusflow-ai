import streamlit as st
import pandas as pd
import random

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="NexusFlow AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# SESSION STATE
# =========================================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

header {
    visibility: hidden;
}

[data-testid="stToolbar"] {
    display: none;
}

.block-container {
    padding-top: 1rem;
}

.stApp {
    background: linear-gradient(
        135deg,
        #f4f7fb 0%,
        #edf2f7 50%,
        #e6ecf5 100%
    );
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #dde7f3 0%,
        #edf2f7 100%
    );
    border-right: 1px solid #cbd5e1;
}

/* TITLES */

.main-title {
    font-size: 60px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 0;
}

.sub-title {
    font-size: 20px;
    color: #64748b;
    margin-top: -10px;
}

/* CARDS */

.card {
    background: rgba(255,255,255,0.82);
    border-radius: 24px;
    padding: 26px;
    margin-bottom: 22px;
    border: 1px solid rgba(255,255,255,0.5);
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    backdrop-filter: blur(10px);
}

.metric-card {
    background: white;
    border-radius: 20px;
    padding: 24px;
    text-align: center;
    box-shadow: 0 8px 22px rgba(0,0,0,0.05);
}

.metric-number {
    font-size: 40px;
    font-weight: 800;
    color: #2563eb;
}

.metric-text {
    color: #64748b;
    font-size: 15px;
}

/* CHAT */

.chat-user {
    background: linear-gradient(
        135deg,
        #2563eb,
        #4f46e5
    );
    color: white;
    padding: 18px;
    border-radius: 18px;
    margin-top: 12px;
}

.chat-ai {
    background: white;
    padding: 18px;
    border-radius: 18px;
    margin-top: 12px;
    border: 1px solid #dbeafe;
}

/* ALERT BOXES */

.success-box {
    background: #ecfdf5;
    border: 1px solid #bbf7d0;
    padding: 18px;
    border-radius: 18px;
}

.warning-box {
    background: #fef2f2;
    border: 1px solid #fecaca;
    padding: 18px;
    border-radius: 18px;
}

.info-box {
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    padding: 18px;
    border-radius: 18px;
}

/* BUTTON */

.stButton > button {
    width: 100%;
    border-radius: 14px;
    border: none;
    padding: 14px;
    background: linear-gradient(
        135deg,
        #4f46e5,
        #2563eb
    );
    color: white;
    font-weight: 700;
}

/* INPUTS */

textarea, input {
    border-radius: 14px !important;
}

.skill-pill {
    background: #dbeafe;
    color: #1d4ed8;
    padding: 8px 14px;
    border-radius: 18px;
    margin: 4px;
    display: inline-block;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("NexusFlow AI")

    role = st.selectbox(
        "Login Role",
        [
            "Admin",
            "HR Manager",
            "Finance Officer",
            "Operations Lead",
            "Sales Director"
        ]
    )

    st.success(f"Logged in as {role}")

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "HR Automation",
            "Finance Automation",
            "Operations Automation",
            "Sales Intelligence",
            "Analytics",
            "Audit Logs"
        ]
    )

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class='main-title'>
NexusFlow AI
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='sub-title'>
Enterprise Workflow Automation Platform
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# AI BUSINESS COPILOT
# =========================================================

st.markdown("""
<div class='card'>

<h2 style='color:#2563eb;'>
AI Business Copilot
</h2>

Ask questions related to:
• HR
• CRM
• Finance
• Operations
• Sales
• Productivity
• Business Automation

</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([5,1])

with col1:

    user_query = st.text_input(
        "Ask NexusFlow AI Anything",
        placeholder="How can I improve my sales and CRM?"
    )

with col2:

    st.markdown("<br>", unsafe_allow_html=True)

    ask_ai = st.button("Ask AI")

# =========================================================
# AI RESPONSE ENGINE
# =========================================================

if ask_ai and user_query:

    st.session_state.chat_history.append(
        ("user", user_query)
    )

    user_lower = user_query.lower()

    if "sales" in user_lower or "crm" in user_lower:

        ai_reply = """
Sales & CRM Optimization Strategy

1. AI Lead Scoring
Identify high-conversion leads automatically using predictive analytics.

2. CRM Workflow Automation
Automate follow-ups, reminders and engagement tracking.

3. Sales Funnel Analytics
Monitor conversion performance at each pipeline stage.

4. Customer Retention Intelligence
Detect customers likely to churn and trigger proactive engagement.

5. Personalized Outreach
AI-generated communication improves response rates.

Business Impact:
• Increased revenue
• Faster conversions
• Better customer retention
"""

    elif "finance" in user_lower:

        ai_reply = """
Financial Automation Insights

1. Expense Monitoring
Track unusual spending patterns automatically.

2. Predictive Budget Forecasting
Estimate future operational costs using AI.

3. Invoice Automation
Reduce manual finance processing workload.

4. Fraud Detection
Identify suspicious transactions instantly.

5. Financial KPI Analytics
Track ROI, revenue growth and operational efficiency.

Expected Benefits:
• Reduced costs
• Improved transparency
• Faster reporting
"""

    elif "operations" in user_lower:

        ai_reply = """
Operations Intelligence Report

1. Workflow Monitoring
AI identifies bottlenecks affecting delivery timelines.

2. Resource Optimization
Improve allocation of employees and infrastructure.

3. Productivity Analytics
Track operational performance in real-time.

4. Predictive Alerts
Prevent operational failures before they occur.

5. AI Automation Recommendations
Optimize repetitive enterprise tasks.

Operational Impact:
• Higher efficiency
• Reduced downtime
• Better scalability
"""

    elif "hr" in user_lower or "hiring" in user_lower:

        ai_reply = """
HR Automation Insights

1. Resume Screening
AI ranks candidates using skill relevance analysis.

2. Candidate Intelligence
Analyze certifications, projects and technical expertise.

3. Hiring Pipeline Optimization
Detect delays in recruitment workflows.

4. Workforce Analytics
Track employee engagement and productivity.

5. Interview Recommendation Engine
AI suggests top candidates for interviews.

Benefits:
• Faster hiring
• Better talent acquisition
• Reduced HR workload
"""

    else:

        ai_reply = f"""
Enterprise AI Business Analysis

Query:
"{user_query}"

Recommendations:

1. Automate repetitive workflows.

2. Centralize operational data into intelligent dashboards.

3. Use predictive analytics for business decisions.

4. Improve customer engagement through AI automation.

5. Optimize enterprise productivity with workflow intelligence.

Expected Impact:
• Higher efficiency
• Better scalability
• Reduced operational costs
"""

    st.session_state.chat_history.append(
        ("ai", ai_reply)
    )

# =========================================================
# CHAT DISPLAY
# =========================================================

for role_name, message in st.session_state.chat_history:

    if role_name == "user":

        st.markdown(f"""
        <div class='chat-user'>
        <b>You:</b><br><br>
        {message}
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div class='chat-ai'>
        <b style='color:#2563eb;'>
        NexusFlow AI Assistant
        </b>
        <br><br>
        {message}
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# DASHBOARD
# =========================================================

if page == "Dashboard":

    st.markdown("""
    <div class='card'>

    <h2 style='color:#2563eb;'>
    Executive Overview
    </h2>

    AI automated 142 enterprise workflows this week.

    Hiring efficiency improved by 72%.

    Financial monitoring identified budget optimization opportunities.

    Operations AI proactively detected workflow bottlenecks.

    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    metrics = [
        ("142", "AI Tasks"),
        ("72%", "Hiring Efficiency"),
        ("₹2.4L", "Cost Savings"),
        ("18", "Active Workflows")
    ]

    for col, (value, label) in zip(
        [c1,c2,c3,c4],
        metrics
    ):

        with col:

            st.markdown(f"""
            <div class='metric-card'>
            <div class='metric-number'>
            {value}
            </div>

            <div class='metric-text'>
            {label}
            </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    chart_data = pd.DataFrame({
        "Month": [
            "Jan","Feb","Mar",
            "Apr","May","Jun"
        ],
        "Efficiency": [
            42,51,59,66,73,81
        ]
    })

    st.subheader("Business Automation Growth")

    st.line_chart(
        chart_data,
        x="Month",
        y="Efficiency"
    )

# =========================================================
# HR AUTOMATION
# =========================================================

elif page == "HR Automation":

    st.subheader("AI Resume Screening")

    jd = st.text_area(
        "Job Description",
        height=180,
        value="""
Hiring Senior Backend Developer

Required Skills:
Python, FastAPI, Docker, Kubernetes, AWS and PostgreSQL.
"""
    )

    resume = st.text_area(
        "Candidate Resume",
        height=250,
        value="""
Senior Backend Developer

Skills:
Python, FastAPI, Docker, Kubernetes, AWS, PostgreSQL
"""
    )

    if st.button("Analyze Candidate"):

        score = 92

        st.markdown(f"""
        <div class='success-box'>

        <h2>
        🥇 Candidate Match Score
        </h2>

        <h1>
        {score}/100
        </h1>

        Strong technical alignment detected.

        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Skill Match")

        skills = [
            "Python",
            "FastAPI",
            "Docker",
            "AWS",
            "PostgreSQL"
        ]

        pills = ""

        for skill in skills:

            pills += f"""
            <span class='skill-pill'>
            ✓ {skill}
            </span>
            """

        st.markdown(pills, unsafe_allow_html=True)

# =========================================================
# FINANCE
# =========================================================

elif page == "Finance Automation":

    st.subheader("AI Financial Analyzer")

    finance_text = st.text_area(
        "Financial Report",
        height=220,
        value="""
• Cloud infrastructure expenses increased
• Operational costs optimized
• Predicted revenue growth: 14%
"""
    )

    if st.button("Analyze Finance"):

        st.markdown("""
        <div class='warning-box'>

        <h2>
        Financial Optimization Required
        </h2>

        AI detected increasing cloud operational expenses.

        Recommended:
        Optimize inactive resources and automate reporting.

        </div>
        """, unsafe_allow_html=True)

        finance_chart = pd.DataFrame({
            "Month": [
                "Jan","Feb","Mar",
                "Apr","May","Jun"
            ],
            "Expenses": [
                2.1,2.5,3.0,
                3.7,4.3,5.0
            ]
        })

        st.area_chart(
            finance_chart,
            x="Month",
            y="Expenses"
        )

# =========================================================
# OPERATIONS
# =========================================================

elif page == "Operations Automation":

    st.subheader("Operations Intelligence")

    ops = st.text_area(
        "Operations Report",
        height=220,
        value="""
• Backend deployment delayed
• QA resources overloaded
• Infrastructure utilization at 87%
"""
    )

    if st.button("Analyze Operations"):

        st.markdown("""
        <div class='info-box'>

        <h2>
        Operational Alert
        </h2>

        Workflow bottlenecks detected.

        Recommended:
        Increase QA resources and optimize deployments.

        </div>
        """, unsafe_allow_html=True)

# =========================================================
# SALES
# =========================================================

elif page == "Sales Intelligence":

    st.subheader("AI Lead Scoring")

    lead = st.text_area(
        "Lead Details",
        height=220,
        value="""
Company: MediCore Healthcare

Requirements:
• CRM automation
• Analytics dashboards
• AI support systems
"""
    )

    if st.button("Analyze Lead"):

        st.markdown("""
        <div class='card'>

        <h2 style='color:#2563eb;'>
        Lead Score: 94/100
        </h2>

        High conversion probability detected.

        Recommended:
        Immediate executive sales follow-up.

        </div>
        """, unsafe_allow_html=True)

# =========================================================
# ANALYTICS
# =========================================================

elif page == "Analytics":

    st.subheader("Enterprise Analytics Dashboard")

    chart1 = pd.DataFrame({
        "Month": [
            "Jan","Feb","Mar",
            "Apr","May"
        ],
        "Hiring": [
            45,53,61,70,79
        ]
    })

    st.line_chart(
        chart1,
        x="Month",
        y="Hiring"
    )

    chart2 = pd.DataFrame({
        "Month": [
            "Jan","Feb","Mar",
            "Apr","May"
        ],
        "Savings": [
            12,18,25,33,46
        ]
    })

    st.area_chart(
        chart2,
        x="Month",
        y="Savings"
    )

# =========================================================
# AUDIT LOGS
# =========================================================

elif page == "Audit Logs":

    st.subheader("Audit Logs")

    logs = pd.DataFrame({

        "Time": [
            "10:22 AM",
            "10:31 AM",
            "10:44 AM",
            "11:02 AM"
        ],

        "User": [
            "HR Manager",
            "Finance Officer",
            "Admin",
            "Operations Lead"
        ],

        "Action": [
            "Resume Screened",
            "Risk Analysis Completed",
            "AI Report Generated",
            "Workflow Alert Triggered"
        ]
    })

    st.dataframe(
        logs,
        use_container_width=True
    )

# =========================================================
# FOOTER
# =========================================================

st.markdown("<br><hr>", unsafe_allow_html=True)

st.markdown("""
<center>

<p style='color:#64748b;'>

NexusFlow AI © 2026
Enterprise Workflow Automation Platform

</p>

</center>
""", unsafe_allow_html=True)
