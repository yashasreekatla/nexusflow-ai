import streamlit as st
import pandas as pd
import google.generativeai as genai

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
# GEMINI CONFIG
# =========================================================

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

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

/* SIDEBAR LABELS */

section[data-testid="stSidebar"] label {
    color: white !important;
    font-weight: 700 !important;
}

/* LOGIN ROLE TEXT FIX */

section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div {
    color: black !important;
}

/* RADIO TEXT */

section[data-testid="stSidebar"] .stRadio label {
    color: white !important;
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

    background: rgba(248,250,252,0.88);

    border-radius: 26px;

    padding: 28px;

    margin-bottom: 24px;

    border: 1px solid #dbe4ee;

    box-shadow:
        0 8px 30px rgba(15,23,42,0.06);

    backdrop-filter: blur(12px);
}

/* =========================================================
METRIC CARDS
========================================================= */

.metric-card {

    background: rgba(255,255,255,0.95);

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

    background: rgba(255,255,255,0.95) !important;
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
ALERT BOXES
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
# AI BUSINESS COPILOT
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
# AI RESPONSE ENGINE
# =========================================================

if ask_ai and user_query:

    st.session_state.chat_history.append(
        ("user", user_query)
    )

    try:

        prompt = f"""
        You are NexusFlow AI,
        an advanced enterprise business assistant.

        Give professional, detailed,
        intelligent and helpful responses.

        User Question:
        {user_query}
        """

        response = model.generate_content(prompt)

        ai_reply = response.text

    except Exception as e:

        ai_reply = f"""
AI Error:
{e}
"""

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
        <b style='color:#23364d;'>
        NexusFlow AI Assistant
        </b>
        <br><br>
        {message}
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# DASHBOARD
# =========================================================

if page == "Dashboard":

    st.markdown("""
    <div class='card'>

    <h2 style='color:#23364d;'>
    Executive Overview
    </h2>

    AI automated 142 enterprise workflows this week.

    Hiring efficiency improved by 72%.

    Finance AI identified optimization opportunities.

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
        "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
        "Efficiency": [42,51,59,66,73,81]
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
        value="""
Hiring Senior Backend Developer

Required Skills:
Python, FastAPI, Docker, AWS, PostgreSQL
"""
    )

    resume = st.text_area(
        "Candidate Resume",
        value="""
Senior Backend Developer

Skills:
Python, FastAPI, Docker, AWS, PostgreSQL
"""
    )

    if st.button("Analyze Candidate"):

        st.markdown("""
        <div class='success-box'>

        <h2>Candidate Match Score: 92/100</h2>

        Strong technical alignment detected.

        </div>
        """, unsafe_allow_html=True)

# =========================================================
# FINANCE
# =========================================================

elif page == "Finance Automation":

    st.subheader("Finance Intelligence")

    report = st.text_area(
        "Financial Report",
        value="""
• Infrastructure expenses increased
• Revenue growth predicted at 14%
• Cloud utilization high
"""
    )

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

    ops = st.text_area(
        "Operations Report",
        value="""
• QA delays detected
• Infrastructure utilization at 87%
• Backend deployment delayed
"""
    )

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

    lead = st.text_area(
        "Lead Details",
        value="""
Company: MediCore Healthcare

Requirements:
CRM automation
Analytics dashboards
AI support systems
"""
    )

    if st.button("Analyze Lead"):

        st.markdown("""
        <div class='card'>

        <h2 style='color:#23364d;'>
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

    chart1 = pd.DataFrame({
        "Month": ["Jan","Feb","Mar","Apr","May"],
        "Hiring": [45,53,61,70,79]
    })

    st.line_chart(
        chart1,
        x="Month",
        y="Hiring"
    )

    chart2 = pd.DataFrame({
        "Month": ["Jan","Feb","Mar","Apr","May"],
        "Savings": [12,18,25,33,46]
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
