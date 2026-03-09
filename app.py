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
# Your reservation logic and database are right here
RESERVATIONS = [
    {"time": "09:00 AM", "patient": "Patient A", "status": "Confirmed"},
    {"time": "10:30 AM", "patient": "Patient B", "status": "Pending"}
]

MESSAGES_DB = {
    "Dr. Sarah Smith": ["Hello Doctor, regarding the lab results...", "I've updated the patient chart."],
    "Nurse Mike": ["Patient in Room 402 is ready for rounds.", "Vitals are stable."]
}

def get_base64(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

logo_b64 = get_base64("logo_medical.png")

# 3. SESSION STATE
if "auth" not in st.session_state:
    st.session_state.auth = False
if "current_page" not in st.session_state:
    st.session_state.current_page = "Homepage"

# 4. THE "CENTERED-FRAME" CSS
st.markdown(f"""
    <style>
    /* REMOVE TOP PADDING TO STOP THE 'SECOND PAGE' PUSH */
    [data-testid="stHeader"] {{ display: none; }}
    
    [data-testid="stAppViewContainer"] {{
        overflow: {"hidden" if not st.session_state.auth else "auto"};
        height: 100vh !important;
        background: radial-gradient(circle at top right, #F9FFF9, #FDFDFD) !important;
    }}

    /* FLEXBOX TO CENTER THE CARD IN THE MIDDLE OF THE PAGE */
    .main .block-container {{
        padding: 0 !important;
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
    }}

    /* THE LOGIN CARD (MATCHING YOUR SCREENSHOT) */
    .login-card {{
        border: 4px solid #93C572; 
        border-radius: 40px; 
        padding: 45px; 
        background-color: #FFFFFF; 
        text-align: center; 
        width: 480px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.05);
        display: flex;
        flex-direction: column;
        align-items: center;
    }}

    .mflo-text {{
        color: #124D41;
        font-size: 60px;
        font-weight: 900;
        margin: 0;
        letter-spacing: -3px;
        line-height: 1;
    }}
    .podcast-tag {{ color: #93C572; font-weight: 800; font-size: 20px; margin-bottom: 5px; }}

    /* INPUT STYLING */
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
        margin-top: 15px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# 5. SEARCH LOGIC (PRESERVED)
def run_global_search(query):
    if not query: return None
    results = []
    nav_items = ["Homepage", "Patients", "Reservation", "Messages", "Community"]
    for item in nav_items:
        if query.lower() in item.lower():
            results.append({"type": "Function", "title": f"Open {item}", "page": item})
    return results

# 6. APP FLOW
if not st.session_state.auth:
    # --- CENTERED LOGIN ---
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    
    if logo_b64:
        st.markdown(f'<img src="data:image/png;base64,{logo_b64}" style="width:120px; margin-bottom:15px;">', unsafe_allow_html=True)
    
    st.markdown('<p class="podcast-tag">67+2 PODCAST</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="mflo-text">M-FLO</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#888; font-size:11px; margin-bottom:25px;">Medi-Flow Orchestrator v2.1 | Secure Portal</p>', unsafe_allow_html=True)

    # Inputs are now locked inside the flexbox card
    u = st.text_input("Physician ID", placeholder="Enter ID", label_visibility="collapsed", key="u")
    p = st.text_input("Security Key", type="password", placeholder="Security Key", label_visibility="collapsed", key="p")

    if st.button("AUTHENTICATE SYSTEM"):
        if u == "doctor1" and p == "mediflow2026":
            st.session_state.auth = True
            st.rerun()
    
    st.markdown('<p style="color:#93C572; font-size:10px; margin-top:15px;">Auth: MD-Level Encrypted Access Only</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- DASHBOARD (RESERVATION FUNCTION IS HERE) ---
    with st.sidebar:
        if logo_b64: st.image(f"data:image/png;base64,{logo_b64}")
        st.divider()
        if st.button("🏠 Homepage"): st.session_state.current_page = "Homepage"
        if st.button("📅 Reservation"): st.session_state.current_page = "Reservation"
        if st.button("✉️ Messages"): st.session_state.current_page = "Messages"
        if st.button("🚪 Logout"):
            st.session_state.auth = False
            st.rerun()

    # Content Area
    st.title(st.session_state.current_page)
    
    if st.session_state.current_page == "Reservation":
        st.write("### Manage Appointments")
        st.table(RESERVATIONS)
        
    elif st.session_state.current_page == "Homepage":
        st.line_chart({"bpm": [72, 75, 78, 74, 80]})
