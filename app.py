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
# PREMIUM CSS
# =========================================================

st.markdown("""
<style>

/* =========================================================
GLOBAL
========================================================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="collapsedControl"] {
    display: flex !important;
}

.block-container {
    padding-top: 1.2rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* =========================================================
BACKGROUND
========================================================= */

.stApp {
    background: linear-gradient(
        135deg,
        #eef2f7 0%,
        #e9eef5 50%,
        #e4ebf4 100%
    );
}

/* =========================================================
SIDEBAR
========================================================= */

section[data-testid="stSidebar"] {

    background: linear-gradient(
        180deg,
        #152434 0%,
        #1c3147 100%
    );

    border-right: 1px solid #2f4257;
}

/* SIDEBAR TEXT WHITE */

section[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

/* =========================================================
LOGIN ROLE SELECTED TEXT ONLY BLACK
========================================================= */

div[data-baseweb="select"] span {
    color: black !important;
}

/* Keep dropdown options readable */

ul[role="listbox"] li {
    color: black !important;
}

/* =========================================================
TITLES
========================================================= */

.main-title {

    font-size: 58px;
    font-weight: 800;
    letter-spacing: -1px;

    color: #0f172a;

    margin-bottom: 0;
}

.sub-title {

    font-size: 20px;
    font-weight: 500;

    color: #64748b;

    margin-top: -10px;
}

/* =========================================================
CARDS
========================================================= */

.card {

    background: rgba(248,250,252,0.82);

    border-radius: 26px;

    padding: 28px;

    margin-bottom: 24px;

    border: 1px solid #dbe4ee;

    box-shadow:
        0 8px 30px rgba(15,23,42,0.06);

    backdrop-filter: blur(12px);
}

/* =========================================================
METRICS
========================================================= */

.metric-card {

    background: rgba(255,255,255,0.88);

    border-radius: 24px;

    padding: 26px;

    text-align: center;

    border: 1px solid #dbe4ee;

    box-shadow:
        0 8px 24px rgba(15,23,42,0.05);
}

.metric-number {

    font-size: 42px;

    font-weight: 800;

    color: #23364d;
}

.metric-text {

    color: #64748b;

    font-size: 15px;

    margin-top: 4px;
}

/* =========================================================
BUTTONS
========================================================= */

.stButton > button {

    width: 100%;

    border-radius: 16px;

    border: none;

    padding: 14px;

    background: linear-gradient(
        135deg,
        #23364d,
        #304861
    );

    color: white;

    font-weight: 700;

    font-size: 15px;

    transition: 0.3s ease;
}

.stButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 10px 20px rgba(35,54,77,0.2);
}

/* =========================================================
INPUTS
========================================================= */

textarea,
input {

    border-radius: 16px !important;

    border: 1px solid #dbe4ee !important;

    background: rgba(255,255,255,0.9) !important;
}

/* =========================================================
CHAT
========================================================= */

.chat-user {

    background: linear-gradient(
        135deg,
        #23364d,
        #304861
    );

    color: white;

    padding: 18px;

    border-radius: 18px;

    margin-top: 12px;

    box-shadow:
        0 6px 20px rgba(35,54,77,0.18);
}

.chat-ai {

    background: #f8fafc;

    border: 1px solid #dbe4ee;

    padding: 18px;

    border-radius: 18px;

    margin-top: 12px;

    color: #0f172a;
}

/* =========================================================
ALERTS
========================================================= */

.success-box {

    background: #edfdf3;

    border: 1px solid #bbf7d0;

    padding: 18px;

    border-radius: 18px;
}

.warning-box {

    background: #fff8ed;

    border: 1px solid #fed7aa;

    padding: 18px;

    border-radius: 18px;
}

.info-box {

    background: #eef4ff;

    border: 1px solid #c7d7f8;

    padding: 18px;

    border-radius: 18px;
}

/* =========================================================
SKILL PILLS
========================================================= */

.skill-pill {

    background: #dbe7f5;

    color: #304861;

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
# AI COPILOT
# =========================================================

st.markdown("""
<div class='card'>

<h2 style='color:#23364d;'>
AI Business Copilot
</h2>

Ask anything related to:
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
# AI RESPONSE
# =========================================================

if ask_ai and user_query:

    st.session_state.chat_history.append(
        ("user", user_query)
    )

    responses = [

        """
Sales & CRM Optimization Strategy

1. AI Lead Scoring
Use predictive analytics to identify high-conversion prospects.

2. CRM Workflow Automation
Automate follow-ups and customer engagement tracking.

3. Funnel Analytics
Track conversion performance at each stage.

4. Customer Retention Intelligence
Identify churn risks proactively.

5. Personalized Outreach
Improve response rates with AI-generated messaging.
""",

        """
Finance Intelligence Report

1. Budget Forecasting
Predict operational costs using AI.

2. Expense Monitoring
Detect abnormal financial patterns.

3. KPI Analytics
Track ROI and enterprise growth.

4. Invoice Automation
Reduce manual finance tasks.

5. Fraud Detection
Identify suspicious transactions quickly.
""",

        """
Operations Intelligence Report

1. Workflow Monitoring
Detect delivery bottlenecks.

2. Resource Optimization
Improve infrastructure utilization.

3. Predictive Alerts
Prevent operational failures.

4. Productivity Analytics
Track enterprise efficiency.

5. Automation
Reduce repetitive operational tasks.
"""
    ]

    ai_reply = random.choice(responses)

    st.session_state.chat_history.append(
        ("ai", ai_reply)
    )

# =========================================================
# CLEAR CHAT
# =========================================================

colx, coly = st.columns([6,1])

with coly:

    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

# =========================================================
# CHAT DISPLAY
# =========================================================

# =========================================================
# CHAT DISPLAY
# =========================================================

for role_name, message in st.session_state.chat_history:

    safe_message = message.replace("<", "&lt;").replace(">", "&gt;")

    if role_name == "user":

        st.markdown(f"""
<div class='chat-user'>
<b>You:</b><br><br>
{safe_message}
</div>
""", unsafe_allow_html=True)

    else:

        formatted_message = safe_message.replace("\n", "<br>")

        st.markdown(f"""
<div class='chat-ai'>
<b style='color:#23364d;'>
NexusFlow AI Assistant
</b>
<br><br>
{formatted_message}
</div>
""", unsafe_allow_html=True)

# =========================================================
# DASHBOARD
# =========================================================

if page == "Dashboard":

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

    if st.button("Analyze Candidate"):

        st.markdown("""
        <div class='success-box'>

        <h2>
        Candidate Match Score: 92/100
        </h2>

        Strong technical alignment detected.

        </div>
        """, unsafe_allow_html=True)

# =========================================================
# FINANCE
# =========================================================

elif page == "Finance Automation":

    st.subheader("Finance Intelligence")

    if st.button("Analyze Finance"):

        st.markdown("""
        <div class='warning-box'>

        AI detected increasing operational expenses.

        Recommended:
        Optimize inactive cloud resources.

        </div>
        """, unsafe_allow_html=True)

# =========================================================
# OPERATIONS
# =========================================================

elif page == "Operations Automation":

    st.subheader("Operations Intelligence")

    if st.button("Analyze Operations"):

        st.markdown("""
        <div class='info-box'>

        Workflow bottlenecks detected.

        Recommended:
        Increase QA resources.

        </div>
        """, unsafe_allow_html=True)

# =========================================================
# SALES
# =========================================================

elif page == "Sales Intelligence":

    st.subheader("AI Lead Scoring")

    if st.button("Analyze Lead"):

        st.markdown("""
        <div class='card'>

        <h2 style='color:#23364d;'>
        Lead Score: 94/100
        </h2>

        High conversion probability detected.

        </div>
        """, unsafe_allow_html=True)

# =========================================================
# ANALYTICS
# =========================================================

elif page == "Analytics":

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

# =========================================================
# AUDIT LOGS
# =========================================================

elif page == "Audit Logs":

    logs = pd.DataFrame({

        "Time": [
            "10:22 AM",
            "10:31 AM",
            "10:44 AM"
        ],

        "User": [
            "HR Manager",
            "Finance Officer",
            "Admin"
        ],

        "Action": [
            "Resume Screened",
            "Risk Analysis Completed",
            "AI Report Generated"
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
