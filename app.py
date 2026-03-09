import streamlit as st
import base64
import os

# 1. PAGE SETUP
st.set_page_config(
    page_title="M-FLO | Cardiology Workspace", 
    page_icon="⚕️", 
    layout="wide"
)

# 2. GLOBAL DATA & VARIABLES (ALL PRESERVED)
user_name = "Dr. John Doe"

COMMUNITY_POSTS = [
    {"user": "u/Cardio_Lead", "title": "Hypertension resistance protocols", "content": "Recent studies suggest..."},
    {"user": "u/Heart_Monitor", "title": "M-FLO v2.1 Beta Feedback", "content": "The new UI is much cleaner..."}
]

RESERVATIONS_DB = [
    {"Time": "09:00 AM", "Patient": "Alice Tan", "Status": "Confirmed"},
    {"Time": "11:30 AM", "Patient": "Bob Smith", "Status": "Pending"},
    {"Time": "02:00 PM", "Patient": "Charlie Dean", "Status": "Confirmed"}
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

# 4. ENHANCED MOTION & DESIGN CSS
st.markdown(f"""
    <style>
    /* KEYFRAME ANIMATIONS */
    @keyframes slideUp {{
        from {{ opacity: 0; transform: translateY(30px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    
    @keyframes softFade {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}

    /* GLOBAL STYLING */
    [data-testid="stHeader"] {{ display: none; }}
    
    [data-testid="stAppViewContainer"] {{
        background: radial-gradient(circle at top right, #F9FFF9, #FDFDFD) !important;
        overflow: {"hidden" if not st.session_state.auth else "auto"};
    }}

    /* CENTERED LOGIN ALIGNMENT */
    .main .block-container {{
        padding: {"0" if not st.session_state.auth else "2rem"} !important;
        height: 100vh;
        display: {"flex" if not st.session_state.auth else "block"};
        align-items: center;
        justify-content: center;
        animation: slideUp 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);
    }}

    /* ANIMATED LOGIN CARD */
    div[data-testid="stForm"] {{
        border: 4px solid #93C572 !important; 
        border-radius: 40px !important; 
        padding: 40px !important; 
        background-color: #FFFFFF !important; 
        width: 480px !important;
        box-shadow: 0 20px 60px rgba(0,0,0,0.07) !important;
        text-align: center;
        transition: transform 0.3s ease;
    }}
    div[data-testid="stForm"]:hover {{
        transform: translateY(-5px);
    }}

    .mflo-header {{ color: #124D41; font-size: 55px; font-weight: 900; margin: 0; letter-spacing: -3px; line-height: 1; }}
    .podcast-header {{ color: #93C572; font-weight: 800; font-size: 20px; margin-bottom: 5px; }}
    .user-greeting {{ color: #124D41; font-size: 20px; font-weight: 700; padding-top: 10px; }}

    /* INPUTS & BUTTONS MOTION */
    .stTextInput > div > div {{
        background-color: #f8f9fa !important;
        border: 1.5px solid #93C572 !important;
        border-radius: 12px !important;
        transition: all 0.3s ease;
    }}
    
    .stButton > button {{
        background: linear-gradient(90deg, #93C572, #A8E6CF) !important;
        color: #124D41 !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 12px !important;
        height: 48px !important;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    }}
    .stButton > button:hover {{
        transform: scale(1.03) !important;
        box-shadow: 0 8px 20px rgba(147, 197, 114, 0.3) !important;
    }}

    /* SIDEBAR HOVER EFFECT */
    [data-testid="stSidebar"] button {{
        transition: 0.3s !important;
    }}
    [data-testid="stSidebar"] button:hover {{
        padding-left: 20px !important;
        background-color: #F0F9F0 !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# 5. GLOBAL SEARCH LOGIC (PRESERVED)
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
    # --- ANIMATED LOGIN PAGE (PRESERVED) ---
    with st.form("login_form", clear_on_submit=False):
        if logo_b64:
            st.markdown(f'<div style="text-align:center;"><img src="data:image/png;base64,{logo_b64}" style="width:110px; margin-bottom:15px; animation: softFade 2s;"></div>', unsafe_allow_html=True)
        st.markdown('<p class="podcast-header">67+2 PODCAST</p>', unsafe_allow_html=True)
        st.markdown('<h1 class="mflo-header">M-FLO</h1>', unsafe_allow_html=True)
        st.markdown('<p style="color:#888; font-size:11px; margin-bottom:20px;">Medi-Flow Orchestrator v2.1 | Secure Portal</p>', unsafe_allow_html=True)

        u = st.text_input("Physician ID", placeholder="Enter ID", label_visibility="collapsed")
        p = st.text_input("Security Key", type="password", placeholder="Security Key", label_visibility="collapsed")

        if st.form_submit_button("AUTHENTICATE SYSTEM"):
            if u == "doctor1" and p == "mediflow2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Access Denied")
        st.markdown('<p style="color:#93C572; font-size:10px; margin-top:10px;">Auth: MD-Level Encrypted Access Only</p>', unsafe_allow_html=True)

else:
    # --- DASHBOARD VIEW ---
    top_l, top_c, top_r = st.columns([1, 2, 1])
    with top_l:
        st.markdown(f'<p class="user-greeting">Hello, {user_name} 👋</p>', unsafe_allow_html=True)
    
    with top_c:
        sq = st.text_input("search", placeholder="Search functions...", key="g_search", label_visibility="collapsed")
        matches = run_global_search(sq)
        if matches:
            for m in matches[:3]:
                if st.button(f"🔍 {m['title']}", key=f"s_{m['title']}", use_container_width=True):
                    st.session_state.current_page = m['page']
                    st.rerun()

    # SIDEBAR
    with st.sidebar:
        if logo_b64: st.image(f"data:image/png;base64,{logo_b64}", use_container_width=True)
        st.divider()
        if st.button("🏠 Homepage", use_container_width=True): st.session_state.current_page = "Homepage"
        if st.button("👥 Patients", use_container_width=True): st.session_state.current_page = "Patients"
        if st.button("📅 Reservation", use_container_width=True): st.session_state.current_page = "Reservation"
        if st.button("✉️ Messages", use_container_width=True): st.session_state.current_page = "Messages"
        st.divider()
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.auth = False
            st.rerun()

    # CONTENT AREA
    st.markdown(f"<div style='animation: slideUp 0.6s ease-out;'><h1>{st.session_state.current_page}</h1></div>", unsafe_allow_html=True)
    
    if st.session_state.current_page == "Homepage":
        st.line_chart({"bpm": [72, 75, 78, 74, 80]})
    elif st.session_state.current_page == "Reservation":
        st.table(RESERVATIONS_DB)
