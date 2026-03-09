import streamlit as st
import base64
import os

# 1. PAGE SETUP
st.set_page_config(
    page_title="M-FLO | Cardiology Workspace", 
    page_icon="⚕️", 
    layout="wide"
)

# 2. GLOBAL DATA & VARIABLES
user_name = "Dr. John Doe"

COMMUNITY_POSTS = [
    {"user": "u/Cardio_Lead", "title": "Hypertension resistance protocols", "content": "Recent studies suggest..."},
    {"user": "u/Heart_Monitor", "title": "M-FLO v2.1 Beta Feedback", "content": "The new UI is much cleaner..."}
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
if "active_chat" not in st.session_state:
    st.session_state.active_chat = list(MESSAGES_DB.keys())[0]

# 4. FIXED THEME & NO-SCROLL CSS
st.markdown(f"""
    <style>
    /* LOCK SCROLLING ON LOGIN ONLY */
    html, body, [data-testid="stAppViewContainer"] {{
        overflow: {"hidden" if not st.session_state.auth else "auto"};
        height: 100vh;
    }}

    .stApp {{
        background: radial-gradient(circle at top right, #F9FFF9, #FDFDFD) !important;
    }}

    /* CENTERED LOGIN CONTAINER */
    .login-container {{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
        width: 100%;
        margin-top: -50px; /* Slight offset for visual balance */
    }}

    /* YOUR DESIGNED LOGO CARD */
    .login-card {{
        border: 6px solid #93C572; 
        border-radius: 60px; 
        padding: 40px 80px; 
        background-color: #FFFFFF; 
        text-align: center; 
        width: 100%;
        max-width: 750px;
        box-shadow: 0 20px 50px rgba(147, 197, 114, 0.1);
        margin-bottom: 30px;
    }}

    /* HEARTBEAT ANIMATION */
    @keyframes heartbeat {{
        0% {{ transform: scale(1); }}
        14% {{ transform: scale(1.05); }}
        28% {{ transform: scale(1); }}
        42% {{ transform: scale(1.08); }}
        70% {{ transform: scale(1); }}
    }}
    .heartbeat-logo {{ animation: heartbeat 1.5s infinite; display: inline-block; }}

    /* DASHBOARD ELEMENTS (PRESERVED) */
    .stButton > button {{
        height: 48px !important;
        border-radius: 10px !important;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        border: 1px solid #E0E0E0;
    }}
    
    .stTextInput > div > div {{
        height: 45px !important;
        border-radius: 8px !important;
        background-color: #f1f3f6 !important;
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
    # --- NO-SCROLL INTEGRATED LOGIN ---
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    
    # Logo Card Part
    logo_html = f'<div class="heartbeat-logo"><img src="data:image/png;base64,{logo_b64}" style="width:200px;"></div>' if logo_b64 else ""
    st.markdown(f"""
        <div class="login-card">
            {logo_html}
            <div style="color: #93C572; font-weight: 800; font-size: 24px; margin-top: 10px;">67+2 PODCAST</div>
            <div style="color: #124D41; font-size: 80px; font-weight: 900; margin: 0; letter-spacing: -5px;">M-FLO</div>
        </div>
    """, unsafe_allow_html=True)

    # Input Part (Aligned under card)
    _, col2, _ = st.columns([1, 1, 1])
    with col2:
        u = st.text_input("Physician ID")
        p = st.text_input("Security Key", type="password")
        if st.button("AUTHENTICATE SYSTEM", use_container_width=True):
            if u == "doctor1" and p == "mediflow2026":
                st.session_state.auth = True
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- DASHBOARD (PRESERVED FUNCTIONS) ---
    t1, t2, t3 = st.columns([1, 2, 1])
    with t2:
        sq = st.text_input("search", placeholder="Search functions...", label_visibility="collapsed", key="g_search")
        matches = run_global_search(sq)
        if matches:
            for m in matches[:3]:
                if st.button(f"🔍 {m['title']}", key=f"s_{m['title']}", use_container_width=True):
                    st.session_state.current_page = m['page']
                    st.rerun()

    with st.sidebar:
        if logo_b64: st.image(f"data:image/png;base64,{logo_b64}", use_container_width=True)
        st.divider()
        if st.button("🏠 Homepage", use_container_width=True): st.session_state.current_page = "Homepage"
        if st.button("👥 Patients", use_container_width=True): st.session_state.current_page = "Patients"
        if st.button("✉️ Messages", use_container_width=True): st.session_state.current_page = "Messages"
        if st.button("🤝 Community", use_container_width=True): st.session_state.current_page = "Community"
        st.divider()
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.auth = False
            st.rerun()

    # Dashboard logic for Messages/Homepage continues here...
    st.markdown(f"<h1>{st.session_state.current_page}</h1>", unsafe_allow_html=True)
    if st.session_state.current_page == "Homepage":
        st.line_chart({"bpm": [72, 75, 78, 74, 80]})
