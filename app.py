import streamlit as st

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
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* MAIN APP */

.stApp {
    background: #f3f5f9;
}

/* REMOVE DEFAULT PADDING */

.block-container {
    padding: 0rem !important;
}

/* HIDE STREAMLIT MENU */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* FULL LOGIN CONTAINER */

.main-container {
    display: flex;
    height: 100vh;
    width: 100%;
}

/* LEFT PANEL */

.left-panel {
    background: linear-gradient(
        180deg,
        #112132 0%,
        #16283b 100%
    );
    color: white;
    padding: 60px;
    border-top-right-radius: 22px;
    border-bottom-right-radius: 22px;
    height: 100vh;
}

.logo-box {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 34px;
    font-weight: 700;
    margin-bottom: 220px;
}

.logo-icon {
    background: #2ea7ff;
    width: 42px;
    height: 42px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.hero-title {
    font-size: 58px;
    font-weight: 700;
    line-height: 1.1;
    margin-bottom: 26px;
}

.hero-sub {
    color: #d0d9e5;
    font-size: 22px;
    line-height: 1.7;
    max-width: 600px;
}

/* RIGHT PANEL */

.right-panel {
    padding: 90px 100px;
}

/* AUTH BOX */

.auth-title {
    font-size: 52px;
    font-weight: 700;
    color: #0f172a;
}

.auth-sub {
    color: #64748b;
    margin-bottom: 35px;
    font-size: 18px;
}

/* TABS */

.tab-box {
    background: #e8edf5;
    border-radius: 14px;
    padding: 5px;
    display: flex;
    margin-bottom: 30px;
}

.tab-active {
    background: white;
    padding: 12px;
    border-radius: 10px;
    width: 50%;
    text-align: center;
    font-weight: 600;
}

.tab-inactive {
    padding: 12px;
    width: 50%;
    text-align: center;
    color: #475569;
    font-weight: 600;
}

/* INPUT LABELS */

.input-label {
    font-size: 16px;
    font-weight: 600;
    color: #0f172a;
    margin-bottom: 8px;
    margin-top: 18px;
}

/* INPUTS */

.stTextInput input {
    border-radius: 14px !important;
    border: 1px solid #dbe2ea !important;
    height: 52px !important;
    font-size: 16px !important;
    background: white !important;
}

/* BUTTON */

.stButton > button {
    width: 100%;
    height: 54px;
    border-radius: 14px;
    border: none;
    background: #24364d;
    color: white;
    font-size: 18px;
    font-weight: 700;
    margin-top: 25px;
}

/* DIVIDER */

.divider {
    text-align: center;
    color: #64748b;
    margin: 28px 0;
    position: relative;
}

.divider::before {
    content: "";
    position: absolute;
    left: 0;
    top: 50%;
    width: 42%;
    height: 1px;
    background: #d6dde8;
}

.divider::after {
    content: "";
    position: absolute;
    right: 0;
    top: 50%;
    width: 42%;
    height: 1px;
    background: #d6dde8;
}

/* GOOGLE BUTTON */

.google-btn {
    border: 1px solid #dbe2ea;
    border-radius: 14px;
    padding: 16px;
    text-align: center;
    font-weight: 600;
    background: white;
    cursor: pointer;
}

/* FOOTER */

.footer-text {
    position: absolute;
    bottom: 40px;
    color: #9fb0c4;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LAYOUT
# =========================================================

left, right = st.columns([1.25, 1])

# =========================================================
# LEFT SIDE
# =========================================================

with left:

    st.markdown("""
    <div class="left-panel">

        <div class="logo-box">
            <div class="logo-icon">⚙️</div>
            <div>Atlas</div>
        </div>

        <div class="hero-title">
            One agent for every business workflow.
        </div>

        <div class="hero-sub">
            Sales pipeline, hiring, project execution,
            finance automation and customer support —
            orchestrated by AI, with role-based access
            and enterprise-grade audit trails.
        </div>

        <div class="footer-text">
            © Atlas Operations
        </div>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# RIGHT SIDE
# =========================================================

with right:

    st.markdown("<div class='right-panel'>", unsafe_allow_html=True)

    st.markdown("""
    <div class="auth-title">
        Sign in to Atlas
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="auth-sub">
        Continue with email or Google.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tab-box">
        <div class="tab-active">Sign in</div>
        <div class="tab-inactive">Create account</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-label">
        Email
    </div>
    """, unsafe_allow_html=True)

    email = st.text_input(
        "",
        placeholder="Enter your email"
    )

    st.markdown("""
    <div class="input-label">
        Password
    </div>
    """, unsafe_allow_html=True)

    password = st.text_input(
        "",
        type="password",
        placeholder="Enter your password"
    )

    login = st.button("Sign in")

    if login:

        if email and password:

            st.success("Login successful!")

            st.switch_page("pages/dashboard.py")

        else:

            st.error("Enter email and password")

    st.markdown("""
    <div class="divider">
        OR
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="google-btn">
        Continue with Google
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
