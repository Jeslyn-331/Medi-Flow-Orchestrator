import streamlit as st
import base64
import os
import requests # Added to handle GitHub URLs

# 1. PAGE SETUP
st.set_page_config(
    page_title="M-FLO | Cardiology Workspace", 
    page_icon="⚕️", 
    layout="wide"
)

# 2. GLOBAL DATA & VARIABLES
user_name = "Dr. John Doe"

# --- PASTE YOUR GITHUB RAW URL HERE ---
GITHUB_RAW_URL = "https://raw.githubusercontent.com/username/repo/main/doctor_profile.png" 

DOCTOR_BIO = {
    "title": "Senior Consultant Cardiologist",
    "desc": "Specializing in interventional cardiology and structural heart disease with over 15 years of clinical excellence.",
    "certs": ["MD, Harvard Medical School", "Board Certified in Cardiovascular Disease", "FACC Fellowship"],
    "achievements": ["Best Clinician Award 2025", "50+ Published Research Papers", "Lead Researcher - Project HeartBeat"]
}

# 3. ADVANCED IMAGE LOADING (LOCAL + GITHUB SUPPORT)
def get_base64_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return base64.b64encode(response.content).decode()
    except:
        return ""
    return ""

def get_base64_local(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

# Try loading from GitHub first, then local, then logo
doctor_b64 = get_base64_from_url(GITHUB_RAW_URL)
if not doctor_b64:
    doctor_b64 = get_base64_local("doctor_profile.png")

logo_b64 = get_base64_local("logo_medical.png")

# 4. SESSION STATE (PRESERVED)
if "auth" not in st.session_state:
    st.session_state.auth = False
if "current_page" not in st.session_state:
    st.session_state.current_page = "Homepage"
if "todos" not in st.session_state:
    st.session_state.todos = ["Review Lab Results", "Surgery Consultation", "Department Meeting"]
if "completed_count" not in st.session_state:
    st.session_state.completed_count = 0

# 5. CSS (ALL BRANDING & MINT SIDEBAR PRESERVED)
st.markdown(f"""
    <style>
    @keyframes slideUp {{ from {{ opacity: 0; transform: translateY(20px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    [data-testid="stHeader"] {{ display: none; }}
    
    [data-testid="stAppViewContainer"] {{
        background: radial-gradient(circle at top right, #F9FFF9, #FDFDFD) !important;
        overflow: {"hidden" if not st.session_state.auth else "auto"};
    }}

    /* LOGIN BRANDING */
    .main .block-container {{
        padding: {"0" if not st.session_state.auth else "2rem"} !important;
        display: {"flex" if not st.session_state.auth else "block"};
        align-items: center; justify-content: center; height: 100vh;
    }}
    div[data-testid="stForm"] {{
        border: 4px solid #93C572 !important; border-radius: 40px !important; padding: 40px !important;
        background-color: #FFFFFF !important; width: 480px !important; text-align: center;
    }}
    .mflo-header {{ color: #124D41; font-size: 55px; font-weight: 900; margin: 0; letter-spacing: -3px; line-height: 1; }}
    .podcast-header {{ color: #93C572; font-weight: 800; font-size: 20px; margin-bottom: 5px; }}

    /* SIDEBAR & PROFILE */
    [data-testid="stSidebar"] {{ background-image: linear-gradient(180deg, #E8F5E9 0%, #C8E6C9 100%) !important; }}
    .profile-card {{ background: white; padding: 35px; border-radius: 30px; border: 1px solid #E0E0E0; box-shadow: 0 10px 40px rgba(0,0,0,0.04); }}
    .profile-img {{ width: 120px; height: 120px; border-radius: 25px; object-fit: cover; border: 3px solid #93C572; }}
    .todo-item {{ background:#F1F8E9; padding:12px; border-radius:12px; border-left:5px solid #93C572; margin-bottom:10px; }}
    </style>
    """, unsafe_allow_html=True)

# 6. APP FLOW
if not st.session_state.auth:
    with st.form("login_form", clear_on_submit=False):
        if logo_b64:
            st.markdown(f'<div style="text-align:center;"><img src="data:image/png;base64,{logo_b64}" style="width:110px; margin-bottom:15px;"></div>', unsafe_allow_html=True)
        st.markdown('<p class="podcast-header">67+2 PODCAST</p>', unsafe_allow_html=True)
        st.markdown('<h1 class="mflo-header">M-FLO</h1>', unsafe_allow_html=True)
        u = st.text_input("ID", placeholder="Enter ID", label_visibility="collapsed")
        p = st.text_input("Key", type="password", placeholder="Security Key", label_visibility="collapsed")
        if st.form_submit_button("AUTHENTICATE SYSTEM"):
            if u == "doctor1" and p == "mediflow2026":
                st.session_state.auth = True; st.rerun()
else:
    # SIDEBAR
    with st.sidebar:
        if logo_b64: st.image(f"data:image/png;base64,{logo_b64}", use_container_width=True)
        st.divider()
        if st.button("🏠 Homepage", use_container_width=True): st.session_state.current_page = "Homepage"
        if st.button("👥 Patients", use_container_width=True): st.session_state.current_page = "Patients"
        if st.button("📅 Reservation", use_container_width=True): st.session_state.current_page = "Reservation"
        if st.button("✉️ Messages", use_container_width=True): st.session_state.current_page = "Messages"
        if st.button("🤝 Community", use_container_width=True): st.session_state.current_page = "Community"
        st.divider()
        if st.button("🚪 Logout", use_container_width=True): st.session_state.auth = False; st.rerun()

    # HOMEPAGE
    if st.session_state.current_page == "Homepage":
        col_main, col_plan = st.columns([2.2, 1], gap="large")
        with col_main:
            img_html = f'<img src="data:image/png;base64,{doctor_b64}" class="profile-img">' if doctor_b64 else '<div class="profile-img" style="background:#93C572; display:flex; align-items:center; justify-content:center; color:white; font-size:40px;">👨‍⚕️</div>'
            st.markdown(f'<div class="profile-card"><div style="display:flex; align-items:center; gap:25px;">{img_html}<div><h1 style="margin:0; color:#124D41;">{user_name}</h1><p style="color:#93C572; font-weight:700;">{DOCTOR_BIO["title"]}</p></div></div><hr style="border:0; border-top:1px solid #eee; margin:25px 0;"><p>{DOCTOR_BIO["desc"]}</p></div>', unsafe_allow_html=True)
        with col_plan:
            st.markdown("### 📅 Calendar")
            st.date_input("Schedule", label_visibility="collapsed")
            st.divider()
            st.markdown("### 📝 Planning")
            for i, task in enumerate(st.session_state.todos):
                c1, c2 = st.columns([5, 1])
                c1.markdown(f'<div class="todo-item">{task}</div>', unsafe_allow_html=True)
                if c2.button("✔️", key=f"d_{i}"):
                    st.session_state.todos.pop(i); st.session_state.completed_count += 1; st.rerun()
