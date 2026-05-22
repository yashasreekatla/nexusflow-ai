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

/* SIDEBAR */

section[data-testid="stSidebar"] {

    background: linear-gradient(
        180deg,
        #152434 0%,
        #1c3147 100%
    );

    border-right: 1px solid #2f4257;
}

/* KEEP SIDEBAR TEXT WHITE */

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* ONLY LOGIN ROLE SELECTED TEXT BLACK */

.stSelectbox [data-baseweb="select"] span {
    color: black !important;
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
