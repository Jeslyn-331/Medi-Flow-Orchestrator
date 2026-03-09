import streamlit as st
import base64
import os

# 1. PAGE SETUP
st.set_page_config(
    page_title="M-FLO | Cardiology Workspace", 
    page_icon="⚕️", 
    layout="wide"
)

# 2. GLOBAL DATA & VARIABLES (PRESERVED)
def get_base64(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

logo_b64 = get_base64("logo_medical.png")

MESSAGES_DB = {
    "Dr. Sarah Smith": ["Hello Doctor, regarding the lab results...", "I've updated the patient chart."],
    "Nurse Mike": ["Patient in Room 402 is ready for rounds.", "Vitals are stable."]
}

# 3. SESSION STATE
if "auth" not in st.session_state:
    st.session_state.auth = False
if "current_page" not in st.session_state:
    st.session_state.current_page = "Homepage"
if "active_chat" not in st.session_state:
    st.session_state.active_chat = list(MESSAGES_DB.keys())[0]

# 4. CSS: THE "FIT-TO-PAGE" LOCK
st.markdown(f"""
    <style>
    /* REMOVE ALL PADDING & PREVENT SCROLL */
    html, body, [data-testid="stAppViewContainer"] {{
        overflow: {"hidden" if not st.session_state.auth else "auto"};
        height: 100vh;
        background: radial-gradient(circle at top right, #F9FFF9, #FDFDFD) !important;
    }}

    .main .block-container {{
        padding: 0 !important;
        max-width: 100%;
    }}

    /* CENTERED COMPACT LOGIN CARD */
    .login-wrapper {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        width: 100vw;
    }}

    .login-card {{
        border: 4px solid #93C572; 
        border-radius: 40px; 
        padding: 40px 60px; 
        background-color: #FFFFFF; 
        text-align: left; 
        width: 500px;
        box-shadow: 0 15px 35px rgba(147, 197, 114, 0.1);
    }}

    /* LOGO & TEXT */
    .heartbeat-logo {{ 
        display: block;
        margin-bottom: 10px;
    }}
    
    .title-area {{ text-align: left; margin-bottom: 25px; }}
    .podcast-text {{ color: #93C572; font-weight: 800; font-size: 22px; margin: 0; }}
    .mflo-text {{ color: #124D41; font-size: 60px; font-weight: 900; line-height: 1; margin: 0; letter-spacing: -3px; }}
    .sub-text {{ color: #666; font-size: 11px; margin-top: 5px; }}

    /* INPUT STYLING TO MATCH SCREENSHOT */
    .stTextInput > label {{ font-size: 14px !important; color: #124D41 !important; font-weight: 600 !important; }}
    .stTextInput > div > div {{
        background-color: #f8f9fa !important;
        border: 1.5px solid #93C572 !important;
        border-radius: 10px !important;
    }}
    
    .stButton > button {{
        background: linear-gradient(90deg, #93C572, #A8E6CF) !important;
        color: #124D41 !important;
        font-weight: 700 !important;
        border: none !important;
        width: 100% !important;
        height: 48px !important;
        margin-top: 10px;
    }}

    .footer-text {{ color: #93C572; font-size: 10px; margin-top: 20px; font-weight: 500; }}
    </style>
    """, unsafe_allow_html=True)

# 5. APP FLOW
if not st.session_state.auth:
    # --- INTEGRATED COMPACT LOGIN ---
    st.markdown('<div class="login-wrapper">', unsafe_allow_html=True)
    
    # We use a single container to wrap EVERYTHING inside the green border
    with st.container():
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        
        # Logo and Title section
        if logo_b64:
            st.markdown(f'<div class="heartbeat-logo"><img src="data:image/png;base64,{logo_b64}" style="width:100px;"></div>', unsafe_allow_html=True)
        
        st.markdown('''
            <div class="title-area">
                <p class="podcast-text">67+2 PODCAST</p>
                <h1 class="mflo-text">M-FLO</h1>
                <p class="sub-text">Medi-Flow Orchestrator v2.1 | Secure Portal</p>
            </div>
        ''', unsafe_allow_html=True)
        
        # Login fields (Streamlit components stay inside the div via the container)
        u = st.text_input("Physician ID", placeholder="Enter ID", key="user_id")
        p = st.text_input("Security Key", type="password", placeholder="••••••••", key="pass_id")
        
        if st.button("AUTHENTICATE SYSTEM"):
            if u == "doctor1" and p == "mediflow2026":
                st.session_state.auth = True
                st.rerun()
        
        st.markdown('<p class="footer-text">Auth: MD-Level Encrypted Access Only</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- DASHBOARD (ALL FUNCTIONS PRESERVED) ---
    with st.sidebar:
        if logo_b64: st.image(f"data:image/png;base64,{logo_b64}")
        st.divider()
        if st.button("🏠 Homepage"): st.session_state.current_page = "Homepage"
        if st.button("✉️ Messages"): st.session_state.current_page = "Messages"
        if st.button("🚪 Logout"):
            st.session_state.auth = False
            st.rerun()

    st.title(st.session_state.current_page)
    if st.session_state.current_page == "Homepage":
        st.line_chart({"bpm": [72, 75, 78, 74, 80]})
