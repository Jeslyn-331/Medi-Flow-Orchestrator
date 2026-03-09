import streamlit as st
import time

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="M-FLO | Medi-Flow", page_icon="⚕️", layout="wide")

# --- 2. THE CODED LOGO & AGGRESSIVE CSS ---
# This SVG recreates your microphone + medical cross icon directly in the code.
logo_svg = """
<svg width="100" height="100" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="9" y="2" width="6" height="12" rx="3" fill="#93C572"/>
    <path d="M5 10V11C5 14.866 8.13401 18 12 18V18C15.866 18 19 14.866 19 11V10" stroke="#93C572" stroke-width="2" stroke-linecap="round"/>
    <line x1="12" y1="18" x2="12" y2="22" stroke="#93C572" stroke-width="2" stroke-linecap="round"/>
    <line x1="9" y1="22" x2="15" y2="22" stroke="#93C572" stroke-width="2" stroke-linecap="round"/>
    <path d="M12 7V11M10 9H14" stroke="white" stroke-width="1.5" stroke-linecap="round"/>
</svg>
"""

st.markdown(f"""
    <style>
    /* Force Light Mode */
    .stApp {{ background-color: #FFFFFF !important; color: #2F4F4F !important; }}
    
    /* THE BLACK BOX FIX: Forcing inputs to stay white */
    div[data-baseweb="input"], div[data-baseweb="textarea"], .stTextArea textarea {{
        background-color: #FFFFFF !important;
        border: 2px solid #93C572 !important;
        border-radius: 10px !important;
    }}
    
    input, textarea {{
        color: #124D41 !important;
        -webkit-text-fill-color: #124D41 !important;
    }}

    /* The Pistachio Frame */
    .login-card {{
        border: 2.5px solid #93C572;
        border-radius: 20px;
        padding: 30px;
        background-color: #F9FFF9;
        text-align: center;
        max-width: 450px;
        margin: auto;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    }}

    /* Coded Logo Text */
    .logo-text {{
        color: #124D41;
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        font-size: 28px;
        letter-spacing: -1px;
        margin-top: 5px;
    }}
    
    .mflo-header {{ color: #124D41; font-size: 45px; font-weight: 900; margin: 0; line-height: 1; }}

    /* Mint Authenticate Button */
    div.stButton > button {{
        background-color: #98FFD9 !important;
        color: #124D41 !important;
        border: 1.5px solid #93C572 !important;
        font-weight: 800 !important;
        width: 100%;
        border-radius: 10px;
        padding: 12px;
    }}

    label p {{ color: #124D41 !important; font-weight: bold !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGIC ---
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    # --- PAGE 1: LOGIN ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Everything coded into one HTML block
    st.markdown(f"""
        <div class="login-card">
            {logo_svg}
            <div class="logo-text">67+2 PODCAST</div>
            <div class="mflo-header">M-FLO</div>
            <p style="color: #124D41; opacity: 0.7; font-size: 14px;">
                Medi-Flow Orchestrator v2.1 | Secure Portal
            </p>
            <hr style="border-top: 1px solid #93C572; margin: 20px 0;">
        </div>
    """, unsafe_allow_html=True)

    # Input section aligned under the frame
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        u = st.text_input("Physician ID", placeholder="doctor1")
        p = st.text_input("Security Key", type="password", placeholder="••••••••")
        
        if st.button("AUTHENTICATE SYSTEM"):
            if u == "doctor1" and p == "mediflow2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Access Denied: Invalid Physician Credentials.")
        
        st.markdown("<p style='text-align:center; font-size:11px; color:gray;'>Auth: MD-Level Encrypted Access Only</p>", unsafe_allow_html=True)
        st.info("ℹ️ Demo: doctor1 / mediflow2026")

else:
    # --- PAGE 2: DASHBOARD ---
    with st.sidebar:
        st.markdown(logo_svg, unsafe_allow_html=True)
        st.title("M-FLO v2.1")
        st.write("User: **Dr. John Doe**")
        if st.button("LOGOUT"):
            st.session_state.auth = False
            st.rerun()

    st.subheader("⚕️ Clinical Intelligence Dashboard")
    c1, c2, c3 = st.columns([1, 2, 2])

    with c1:
        st.markdown("#### Patient Context")
        with st.container(border=True):
            st.write("**J. Doe** | ID: #8821")
            st.error("⚠️ Penicillin Allergy")

    with c2:
        st.markdown("#### Input Control")
        notes = st.text_area("Consultation Notes:", height=300)
        if st.button("ANALYZE"):
            st.toast("Coding intents...")

    with c3:
        st.markdown("#### Generated Orders")
        st.info("Awaiting analysis...")
