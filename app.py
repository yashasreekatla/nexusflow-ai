import streamlit as st
import pandas as pd
import random

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="NexusFlow AI",
    page_icon="🧠",
    layout="wide"
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

[data-testid="stDecoration"] {
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

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #dde7f3 0%,
        #edf2f7 100%
    );
}

.main-title {
    font-size: 54px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 0;
}

.sub-title {
    font-size: 18px;
    color: #64748b;
    margin-top: -8px;
}

.card {
    background: rgba(255,255,255,0.78);
    border-radius: 24px;
    padding: 24px;
    margin-bottom: 22px;
    border: 1px solid rgba(255,255,255,0.45);
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

.chat-user {
    background: #2563eb;
    color: white;
    padding: 16px;
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

textarea, input {
    border-radius: 14px !important;
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

if ask_ai and user_query:

    st.session_state.chat_history.append(
        ("user", user_query)
    )

    user_lower = user_query.lower()

    if "sales" in user_lower or "crm" in user_lower:

        ai_reply = """
NexusFlow AI Sales & CRM Recommendations

1. Implement AI Lead Scoring
Use machine learning models to identify high-conversion prospects based on customer behavior, engagement history and demographic patterns.

2. Automate Customer Follow-Ups
Businesses lose many leads due to delayed responses. Automated email sequences and AI-driven reminders improve engagement rates significantly.

3. Centralize CRM Data
Integrating all customer interactions into one CRM dashboard helps sales teams track communication history, pending deals and customer preferences efficiently.

4. Predict Customer Behavior
AI analytics can identify customers likely to purchase, churn or upgrade services. This allows proactive sales strategies.

5. Improve Sales Funnel Visibility
Tracking conversion rates at every stage helps identify weak points in the pipeline and optimize performance.

Expected Impact:
• Increased lead conversion
• Faster response times
• Better customer retention
• Improved sales forecasting
"""

    elif "finance" in user_lower:

        ai_reply = """
NexusFlow AI Financial Optimization Report

1. Expense Pattern Monitoring
AI systems can continuously analyze spending trends and identify abnormal financial behavior before it becomes risky.

2. Predictive Budget Forecasting
Machine learning models can estimate future operational costs based on historical financial data.

3. Invoice Automation
Automating invoice processing reduces manual workload, improves accuracy and speeds up approvals.

4. Fraud Detection
AI can identify suspicious transactions, duplicate payments and unusual spending behavior in real-time.

5. Cost Optimization
The platform recommends reducing inactive cloud resources, unused subscriptions and inefficient spending patterns.

Business Benefits:
• Reduced operational costs
• Better financial transparency
• Faster reporting
• Improved budgeting accuracy
"""

    elif "operations" in user_lower:

        ai_reply = """
NexusFlow AI Operations Intelligence

1. Workflow Bottleneck Detection
AI continuously monitors project activities and identifies delays affecting delivery timelines.

2. Resource Allocation Optimization
The platform recommends reallocating employees and infrastructure to improve productivity.

3. Predictive Maintenance
Operational AI can identify systems likely to fail before breakdowns occur.

4. Productivity Analytics
Managers can track task completion efficiency and identify underperforming workflows.

5. Real-Time Operational Alerts
The system proactively generates alerts for risks, delays and dependency conflicts.

Operational Impact:
• Faster project delivery
• Reduced downtime
• Better resource utilization
• Improved team productivity
"""

    elif "hr" in user_lower or "hiring" in user_lower:

        ai_reply = """
NexusFlow AI HR Automation Insights

1. AI Resume Screening
The system automatically matches resumes against job descriptions and ranks candidates based on skill relevance.

2. Candidate Skill Analysis
Technical skills, certifications and experience levels are analyzed automatically.

3. Hiring Pipeline Optimization
AI helps HR teams identify bottlenecks in recruitment workflows.

4. Employee Performance Tracking
The platform can monitor productivity metrics and engagement trends.

5. Predictive Hiring Analytics
AI predicts candidate success probability using historical recruitment data.

Benefits:
• Faster hiring cycles
• Better talent acquisition
• Reduced recruiter workload
• Improved hiring accuracy
"""

    else:

        ai_reply = f"""
NexusFlow AI Business Analysis

Your Query:
"{user_query}"

Strategic Recommendations:

1. Implement workflow automation to reduce repetitive manual tasks.

2. Use analytics dashboards for data-driven decision making.

3. Centralize business operations into integrated management systems.

4. Deploy AI-driven monitoring tools for predictive insights.

5. Improve organizational efficiency through automation and process optimization.

Enterprise Impact:
• Higher productivity
• Reduced operational costs
• Improved scalability
• Faster business decisions
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
        NexusFlow AI
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

Experience:
Minimum 4 years building scalable cloud-native enterprise applications.
"""
    )

    resume = st.text_area(
        "Candidate Resume",
        height=250,
        value="""
Senior Backend Developer

Skills:
Python, FastAPI, Docker, Kubernetes, AWS, PostgreSQL

Experience:
5 years building scalable enterprise APIs and cloud infrastructure.

Projects:
• AI-powered HR analytics platform
• Cloud-native CRM backend system
• Real-time operations dashboard

Certifications:
AWS Certified Developer
Docker Professional Certification
"""
    )

    if st.button("Analyze Candidate"):

        matched = [
            "Python",
            "FastAPI",
            "Docker",
            "AWS",
            "PostgreSQL"
        ]

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

        Recommended for technical interview round.

        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Skill Match")

        pills = ""

        for skill in matched:

            pills += f"""
            <span style='
            background:#dbeafe;
            color:#1d4ed8;
            padding:8px 14px;
            border-radius:18px;
            margin:4px;
            display:inline-block;
            font-weight:600;
            '>
            ✓ {skill}
            </span>
            """

        st.markdown(pills, unsafe_allow_html=True)

# =========================================================
# FINANCE AUTOMATION
# =========================================================

elif page == "Finance Automation":

    st.subheader("AI Financial Risk Analyzer")

    finance_text = st.text_area(
        "Financial Summary",
        height=220,
        value="""
Quarterly Financial Summary

• Cloud infrastructure expenses increased by 38%
• Marketing spend increased by 22%
• Operational efficiency improved by 17%
• AI automation reduced manual processing costs
• Predicted Q4 revenue growth: 14%
"""
    )

    if st.button("Analyze Financial Risk"):

        risk = 84

        st.markdown(f"""
        <div class='warning-box'>

        <h2>
        Financial Risk Detected
        </h2>

        <h1>
        {risk}%
        </h1>

        AI recommends reducing inactive cloud resources and optimizing operational spending.

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
# OPERATIONS AUTOMATION
# =========================================================

elif page == "Operations Automation":

    st.subheader("AI Operations Monitoring")

    ops_text = st.text_area(
        "Operations Report",
        height=240,
        value="""
Operations Status Report

• Backend API deployment delayed by 5 days
• QA testing resources overloaded
• DevOps infrastructure utilization at 87%
• Two critical workflow bottlenecks detected
• Customer ticket resolution time increased by 18%
"""
    )

    if st.button("Analyze Operations"):

        st.markdown("""
        <div class='info-box'>

        <h2>
        Operational Risk Alert
        </h2>

        AI detected workflow bottlenecks affecting delivery timelines.

        Recommended Action:
        Increase QA testing resources and optimize deployment pipeline.

        </div>
        """, unsafe_allow_html=True)

# =========================================================
# SALES INTELLIGENCE
# =========================================================

elif page == "Sales Intelligence":

    st.subheader("AI Lead Scoring")

    lead_text = st.text_area(
        "Lead Details",
        height=240,
        value="""
Lead Analysis Report

Company:
MediCore Healthcare Solutions

Requirements:
• CRM automation
• AI-powered analytics
• Customer support automation

Estimated Deal Size:
₹24 Lakhs

Engagement Level:
High

Decision Stage:
Final vendor evaluation
"""
    )

    if st.button("Analyze Lead"):

        lead_score = 94

        st.markdown(f"""
        <div class='card'>

        <h2 style='color:#2563eb;'>
        Lead Score
        </h2>

        <h1>
        {lead_score}/100
        </h1>

        High conversion probability detected.

        Recommended Action:
        Immediate executive sales follow-up.

        </div>
        """, unsafe_allow_html=True)

# =========================================================
# ANALYTICS
# =========================================================

elif page == "Analytics":

    st.subheader("Enterprise Analytics Dashboard")

    col1, col2 = st.columns(2)

    with col1:

        hire_chart = pd.DataFrame({
            "Month": [
                "Jan","Feb","Mar",
                "Apr","May"
            ],
            "Hiring": [
                45,53,61,70,79
            ]
        })

        st.line_chart(
            hire_chart,
            x="Month",
            y="Hiring"
        )

    with col2:

        finance_chart = pd.DataFrame({
            "Month": [
                "Jan","Feb","Mar",
                "Apr","May"
            ],
            "Savings": [
                12,18,25,33,46
            ]
        })

        st.area_chart(
            finance_chart,
            x="Month",
            y="Savings"
        )

# =========================================================
# AUDIT LOGS
# =========================================================

elif page == "Audit Logs":

    st.subheader("Enterprise Audit Logs")

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