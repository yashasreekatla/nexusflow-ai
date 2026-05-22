import streamlit as st
import pandas as pd
import random
import time

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Atlas AI",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

/* =========================================================
GLOBAL
========================================================= */

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}

.stApp {
    background: #eef2f7;
}

/* HEADER */

[data-testid="stHeader"] {
    background: transparent;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #0f1c2b 0%,
        #16283b 100%
    );
    border-right: 1px solid #23364d;
}

/* SIDEBAR TEXT */

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* SIDEBAR BUTTON */

[data-testid="collapsedControl"] {
    display: flex !important;
}

/* CONTAINER */

.block-container {
    padding-top: 2rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* TITLES */

.main-title {
    font-size: 54px;
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
    background: #f8fafc;
    border: 1px solid #d9e2ec;
    border-radius: 24px;
    padding: 28px;
    margin-bottom: 24px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.04);
}

/* METRIC CARDS */

.metric-card {
    background: #f8fafc;
    border: 1px solid #d9e2ec;
    border-radius: 24px;
    padding: 30px;
    text-align: center;
    box-shadow: 0 8px 30px rgba(0,0,0,0.04);
}

.metric-number {
    font-size: 42px;
    font-weight: 800;
    color: #304861;
}

.metric-label {
    color: #64748b;
    font-size: 16px;
}

/* SECTION TITLE */

.section-title {
    font-size: 30px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 18px;
}

/* BUTTONS */

.stButton > button {
    width: 100%;
    border: none;
    border-radius: 16px;
    padding: 14px;
    background: linear-gradient(
        135deg,
        #23364d,
        #304861
    );
    color: white;
    font-size: 17px;
    font-weight: 700;
}

/* INPUTS */

textarea, input {
    border-radius: 16px !important;
}

/* CHAT */

.chat-user {
    background: #23364d;
    color: white;
    padding: 18px;
    border-radius: 18px;
    margin-top: 12px;
}

.chat-ai {
    background: #eaf1f8;
    border: 1px solid #d8e2ee;
    padding: 18px;
    border-radius: 18px;
    margin-top: 12px;
}

/* ALERTS */

.success-box {
    background: #edfdf3;
    border: 1px solid #bbf7d0;
    padding: 18px;
    border-radius: 18px;
    margin-top: 14px;
}

.warning-box {
    background: #fff8ed;
    border: 1px solid #fed7aa;
    padding: 18px;
    border-radius: 18px;
    margin-top: 14px;
}

.danger-box {
    background: #fff1f2;
    border: 1px solid #fecdd3;
    padding: 18px;
    border-radius: 18px;
    margin-top: 14px;
}

/* TAGS */

.tag {
    display: inline-block;
    background: #dbe7f5;
    color: #304861;
    padding: 8px 14px;
    border-radius: 999px;
    margin: 4px;
    font-size: 14px;
    font-weight: 600;
}

.small-text {
    color: #64748b;
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## Atlas AI")

    st.markdown("---")

    st.markdown("""
    ✅ HR Automation  
    ✅ CRM Intelligence  
    ✅ Finance AI  
    ✅ Operations Monitoring  
    ✅ AI Assistant  
    ✅ Project Analytics  
    """)

    st.markdown("---")

    st.info("Enterprise Admin")

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="main-title">
Atlas AI
</div>

<div class="sub-title">
Enterprise Workflow Automation Platform
</div>
""", unsafe_allow_html=True)

st.write("")

# =========================================================
# METRICS
# =========================================================

col1, col2, col3, col4 = st.columns(4)

metrics = [
    ("142", "Automated Workflows"),
    ("89%", "Sales Conversion"),
    ("72%", "Hiring Efficiency"),
    ("34", "Operational Alerts")
]

for col, metric in zip([col1, col2, col3, col4], metrics):

    with col:

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{metric[0]}</div>
            <div class="metric-label">{metric[1]}</div>
        </div>
        """, unsafe_allow_html=True)

st.write("")

# =========================================================
# MAIN LAYOUT
# =========================================================

left, right = st.columns([1.5, 1])

# =========================================================
# LEFT SIDE
# =========================================================

with left:

    st.markdown("""
    <div class="card">
        <div class="section-title">
            AI Business Copilot
        </div>

        <div class="small-text">
            Ask anything about HR, CRM, Finance,
            Operations or Business Strategy.
        </div>
    """, unsafe_allow_html=True)

    prompt = st.text_area(
        "",
        placeholder="How can I improve my sales pipeline and customer retention?",
        height=130
    )

    if st.button("Ask Atlas AI"):

        if prompt:

            st.markdown(f"""
            <div class="chat-user">
            {prompt}
            </div>
            """, unsafe_allow_html=True)

            with st.spinner("Atlas AI is analyzing your workflows..."):
                time.sleep(2)

            responses = [

                f"""
                Based on your request regarding "{prompt}":

                • Improve customer segmentation using predictive analytics  
                • Automate follow-up workflows for inactive leads  
                • Implement AI-powered lead scoring  
                • Enable smart CRM reminders for sales teams  
                • Use analytics dashboards for retention tracking  
                """,

                f"""
                Atlas AI strategic insights:

                • Workflow inefficiencies detected  
                • Revenue optimization opportunities identified  
                • AI automation can reduce operational effort by 43%  
                • Predictive forecasting recommended  
                • Customer churn analysis advised  
                """,

                f"""
                Recommended enterprise actions:

                • Deploy automated reporting systems  
                • Integrate finance and CRM analytics  
                • Use AI-driven operational monitoring  
                • Improve HR workflow automation  
                • Enable project escalation alerts  
                """
            ]

            ai_response = random.choice(responses)

            st.markdown(f"""
            <div class="chat-ai">
            {ai_response}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # HR SECTION
    # =====================================================

    st.markdown("""
    <div class="card">

        <div class="section-title">
            HR Automation
        </div>

        <span class="tag">Resume Screening</span>
        <span class="tag">Candidate Ranking</span>
        <span class="tag">Interview Scheduling</span>
        <span class="tag">Skill Matching</span>

        <div class="success-box">
        AI screened 142 resumes this week.
        </div>

        <div class="warning-box">
        8 high-potential candidates identified.
        </div>

        <div class="danger-box">
        Engineering hiring pipeline needs attention.
        </div>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # CRM
    # =====================================================

    st.markdown("""
    <div class="card">

        <div class="section-title">
            CRM Intelligence
        </div>

        <ul>
            <li>Lead scoring automation enabled</li>
            <li>Customer churn prediction active</li>
            <li>AI-generated follow-up reminders</li>
            <li>Sales engagement tracking improved</li>
            <li>Customer segmentation analytics available</li>
        </ul>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# RIGHT SIDE
# =========================================================

with right:

    # =====================================================
    # FINANCE
    # =====================================================

    st.markdown("""
    <div class="card">

        <div class="section-title">
            Finance Automation
        </div>

        <div class="success-box">
        Budget optimization opportunities detected.
        </div>

        <div class="warning-box">
        Vendor payment approvals pending.
        </div>

        <div class="danger-box">
        Unusual expense spike detected.
        </div>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # OPERATIONS
    # =====================================================

    st.markdown("""
    <div class="card">

        <div class="section-title">
            Operations Monitoring
        </div>

        <ul>
            <li>Supply chain bottleneck detection active</li>
            <li>Warehouse efficiency improved by 24%</li>
            <li>Operational forecasting enabled</li>
            <li>Delivery optimization AI running</li>
        </ul>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # PROJECTS
    # =====================================================

    st.markdown("""
    <div class="card">

        <div class="section-title">
            Project Intelligence
        </div>

        <ul>
            <li>4 deadlines approaching this week</li>
            <li>AI task prioritization enabled</li>
            <li>Resource allocation optimized</li>
            <li>Cross-team collaboration improved</li>
        </ul>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # ANALYTICS
    # =====================================================

    st.markdown("""
    <div class="card">

        <div class="section-title">
            Revenue Analytics
        </div>
    """, unsafe_allow_html=True)

    chart_data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Revenue": [20, 35, 48, 60, 72, 91]
    })

    st.line_chart(
        chart_data,
        x="Month",
        y="Revenue"
    )

    st.markdown("</div>", unsafe_allow_html=True)
