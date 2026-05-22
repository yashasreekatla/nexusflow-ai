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
    initial_sidebar_state="collapsed"
)

# =========================================================
# SESSION STATE
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

/* =========================================================
GLOBAL
========================================================= */

#MainMenu {display:none;}
footer {display:none;}
header {display:none;}

.block-container{
    padding:0 !important;
}

.stApp{
    background:#f4f7fb;
    font-family:Inter,sans-serif;
}

/* =========================================================
LOGIN PAGE
========================================================= */

.wrapper{
    display:flex;
    height:100vh;
    width:100vw;
    overflow:hidden;
}

.left{
    width:55%;
    background:linear-gradient(
        180deg,
        #0d1b2a 0%,
        #13263c 100%
    );

    color:white;
    padding:60px;
    position:relative;
}

.logo{
    display:flex;
    align-items:center;
    gap:14px;
    font-size:34px;
    font-weight:700;
}

.logo-icon{
    width:46px;
    height:46px;
    border-radius:14px;
    background:#36a9ff;

    display:flex;
    align-items:center;
    justify-content:center;

    font-size:24px;
}

.hero{
    margin-top:220px;
}

.hero-title{
    font-size:68px;
    line-height:1.05;
    font-weight:700;
    max-width:650px;
}

.hero-sub{
    margin-top:32px;
    font-size:24px;
    line-height:1.7;
    color:#cbd5e1;
    max-width:700px;
}

.footer{
    position:absolute;
    bottom:40px;
    color:#94a3b8;
    font-size:18px;
}

.right{
    width:45%;
    background:#f4f7fb;
    display:flex;
    align-items:center;
    justify-content:center;
}

.card{
    width:520px;
}

.auth-title{
    font-size:64px;
    font-weight:700;
    color:#0f172a;
}

.auth-sub{
    margin-top:10px;
    color:#64748b;
    font-size:22px;
    margin-bottom:40px;
}

.tabs{
    display:flex;
    background:#e7edf5;
    padding:6px;
    border-radius:18px;
    margin-bottom:40px;
}

.active{
    width:50%;
    background:white;
    padding:16px;
    border-radius:14px;
    text-align:center;
    font-weight:700;
    font-size:20px;
}

.inactive{
    width:50%;
    padding:16px;
    text-align:center;
    color:#475569;
    font-size:20px;
}

.label{
    font-size:18px;
    font-weight:600;
    margin-bottom:10px;
    margin-top:18px;
    color:#0f172a;
}

.stTextInput input{
    height:62px !important;
    border-radius:18px !important;
    border:1px solid #d9e2ec !important;
    padding-left:18px !important;
    font-size:18px !important;
}

.stButton button{
    width:100%;
    height:62px;
    border:none;
    border-radius:18px;
    background:#23364d;
    color:white;
    font-size:20px;
    font-weight:700;
    margin-top:30px;
}

/* =========================================================
DASHBOARD
========================================================= */

.dashboard{
    padding:40px;
}

.topbar{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:30px;
}

.dashboard-title{
    font-size:52px;
    font-weight:800;
    color:#0f172a;
}

.dashboard-sub{
    color:#64748b;
    font-size:20px;
}

.card-ui{
    background:white;
    padding:28px;
    border-radius:24px;
    box-shadow:0 8px 30px rgba(0,0,0,0.04);
    margin-bottom:24px;
}

.metric{
    text-align:center;
}

.metric-number{
    font-size:42px;
    font-weight:800;
    color:#2563eb;
}

.metric-label{
    color:#64748b;
    font-size:16px;
}

.section-title{
    font-size:32px;
    font-weight:700;
    margin-bottom:18px;
    color:#0f172a;
}

.chat-box{
    background:#eef4ff;
    padding:18px;
    border-radius:18px;
    margin-top:12px;
}

.user-box{
    background:#1e293b;
    color:white;
    padding:18px;
    border-radius:18px;
    margin-top:12px;
}

.sidebar-box{
    background:white;
    padding:18px;
    border-radius:18px;
    margin-bottom:20px;
}

.alert-success{
    background:#ecfdf5;
    border:1px solid #bbf7d0;
    padding:16px;
    border-radius:16px;
    margin-top:12px;
}

.alert-warning{
    background:#fff7ed;
    border:1px solid #fed7aa;
    padding:16px;
    border-radius:16px;
    margin-top:12px;
}

.alert-danger{
    background:#fef2f2;
    border:1px solid #fecaca;
    padding:16px;
    border-radius:16px;
    margin-top:12px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOGIN PAGE
# =========================================================

if not st.session_state.logged_in:

    left,right = st.columns([1.2,1])

    with left:

        st.markdown("""
        <div class="left">

            <div class="logo">
                <div class="logo-icon">⚙️</div>
                <div>Atlas</div>
            </div>

            <div class="hero">

                <div class="hero-title">
                    One agent for every business workflow.
                </div>

                <div class="hero-sub">
                    Sales pipeline, hiring, project execution,
                    finance automation and customer support —
                    orchestrated by AI, with role-based access
                    and enterprise-grade audit trails.
                </div>

            </div>

            <div class="footer">
                © Atlas Operations
            </div>

        </div>
        """, unsafe_allow_html=True)

    with right:

        st.markdown("""
        <div style="padding:120px 80px;">

        <div class="auth-title">
            Sign in to Atlas
        </div>

        <div class="auth-sub">
            Continue with email or Google.
        </div>

        <div class="tabs">
            <div class="active">Sign in</div>
            <div class="inactive">Create account</div>
        </div>
        """, unsafe_allow_html=True)

        email = st.text_input(
            "Email",
            placeholder="Enter your email"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password"
        )

        if st.button("Sign in"):

            if email and password:

                st.session_state.logged_in = True
                st.rerun()

            else:
                st.error("Enter email and password")

        st.markdown("""
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# MAIN DASHBOARD
# =========================================================

else:

    # =====================================================
    # SIDEBAR
    # =====================================================

    with st.sidebar:

        st.markdown("## Atlas AI")

        st.markdown("""
        <div class="sidebar-box">
        <b>Role:</b> Enterprise Admin
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="sidebar-box">
        ✅ HR Automation<br><br>
        ✅ CRM Intelligence<br><br>
        ✅ Finance AI<br><br>
        ✅ Operations Monitoring<br><br>
        ✅ AI Assistant
        </div>
        """, unsafe_allow_html=True)

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

    # =====================================================
    # DASHBOARD
    # =====================================================

    st.markdown("""
    <div class="dashboard">

    <div class="topbar">

        <div>
            <div class="dashboard-title">
                Atlas AI
            </div>

            <div class="dashboard-sub">
                Enterprise Workflow Automation Platform
            </div>
        </div>

    </div>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # METRICS
    # =====================================================

    col1,col2,col3,col4 = st.columns(4)

    metrics = [
        ("142", "Workflows Automated"),
        ("89%", "Sales Conversion"),
        ("72%", "Hiring Efficiency"),
        ("34", "Operational Alerts")
    ]

    for col,metric in zip([col1,col2,col3,col4],metrics):

        with col:

            st.markdown(f"""
            <div class="card-ui metric">
                <div class="metric-number">{metric[0]}</div>
                <div class="metric-label">{metric[1]}</div>
            </div>
            """, unsafe_allow_html=True)

    # =====================================================
    # MAIN CONTENT
    # =====================================================

    left,right = st.columns([1.5,1])

    # =====================================================
    # LEFT SIDE
    # =====================================================

    with left:

        # AI CHAT

        st.markdown("""
        <div class="card-ui">
            <div class="section-title">
                AI Business Copilot
            </div>
        """, unsafe_allow_html=True)

        prompt = st.text_area(
            "",
            placeholder="Ask anything about HR, CRM, Finance, Operations, Sales or Business Strategy...",
            height=120
        )

        if st.button("Ask Atlas AI"):

            if prompt:

                st.markdown(f"""
                <div class="user-box">
                {prompt}
                </div>
                """, unsafe_allow_html=True)

                with st.spinner("Atlas AI is analyzing..."):

                    time.sleep(2)

                responses = [
                    f"""
                    Based on your request about "{prompt}", Atlas AI recommends:
                    
                    • Automating repetitive workflows using AI triggers
                    • Improving customer retention through predictive CRM analytics
                    • Monitoring finance KPIs weekly
                    • Using AI-driven operational forecasting
                    • Implementing role-based reporting dashboards
                    """,

                    f"""
                    Strategic insights for "{prompt}":
                    
                    • Revenue optimization opportunity detected
                    • Workflow inefficiencies identified
                    • AI automation can reduce manual effort by 43%
                    • Consider implementing smart escalation systems
                    • Predictive analytics can improve forecasting accuracy
                    """,

                    f"""
                    Atlas AI business recommendations:
                    
                    • Strengthen sales pipeline automation
                    • Deploy AI-powered customer segmentation
                    • Integrate finance approval workflows
                    • Improve operational visibility with live dashboards
                    • Enable automated reporting systems
                    """
                ]

                ai_response = random.choice(responses)

                st.markdown(f"""
                <div class="chat-box">
                {ai_response}
                </div>
                """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # HR SECTION

        st.markdown("""
        <div class="card-ui">
            <div class="section-title">
                HR Automation
            </div>

            <div class="alert-success">
            AI screened 142 resumes this week.
            </div>

            <div class="alert-warning">
            8 high-potential candidates detected.
            </div>

            <div class="alert-danger">
            Interview scheduling delays detected in Engineering.
            </div>

        </div>
        """, unsafe_allow_html=True)

        # CRM SECTION

        st.markdown("""
        <div class="card-ui">
            <div class="section-title">
                CRM Intelligence
            </div>

            <ul>
                <li>Lead scoring automation active</li>
                <li>Sales pipeline conversion improved by 18%</li>
                <li>AI follow-up reminders generated</li>
                <li>Customer churn prediction enabled</li>
            </ul>

        </div>
        """, unsafe_allow_html=True)

    # =====================================================
    # RIGHT SIDE
    # =====================================================

    with right:

        # FINANCE

        st.markdown("""
        <div class="card-ui">

            <div class="section-title">
                Finance Automation
            </div>

            <div class="alert-success">
            Budget optimization opportunities identified.
            </div>

            <div class="alert-warning">
            Vendor payment cycle approaching.
            </div>

            <div class="alert-danger">
            Unusual expense pattern detected.
            </div>

        </div>
        """, unsafe_allow_html=True)

        # OPERATIONS

        st.markdown("""
        <div class="card-ui">

            <div class="section-title">
                Operations Monitoring
            </div>

            <ul>
                <li>Warehouse efficiency increased by 24%</li>
                <li>AI detected supply bottlenecks</li>
                <li>Delivery timelines optimized</li>
                <li>Operational forecasting enabled</li>
            </ul>

        </div>
        """, unsafe_allow_html=True)

        # PROJECT MANAGEMENT

        st.markdown("""
        <div class="card-ui">

            <div class="section-title">
                Project Intelligence
            </div>

            <ul>
                <li>4 project deadlines approaching</li>
                <li>AI resource allocation active</li>
                <li>Risk prediction monitoring enabled</li>
                <li>Cross-team collaboration improved</li>
            </ul>

        </div>
        """, unsafe_allow_html=True)

        # ANALYTICS

        chart_data = pd.DataFrame({
            "Month":["Jan","Feb","Mar","Apr","May","Jun"],
            "Revenue":[20,35,40,50,68,82]
        })

        st.markdown("""
        <div class="card-ui">
            <div class="section-title">
                Revenue Analytics
            </div>
        """, unsafe_allow_html=True)

        st.line_chart(
            chart_data,
            x="Month",
            y="Revenue"
        )

        st.markdown("</div>", unsafe_allow_html=True)
