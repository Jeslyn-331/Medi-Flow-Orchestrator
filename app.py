import streamlit as st
import base64
import os
import time

st.set_page_config(
    page_title="M-FLO | Secure Access Portal", 
    page_icon="⚕️", 
    layout="wide"
)

def get_base_base64(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

logo_b64 = get_base_base64("logo_medical.png")

st.markdown(f"""
    <style>
    .stApp {{ background-color: #FFFFFF !important; }}

    /* ELASTIC BOUNCE ANIMATION (Dribbble Style) */
    @keyframes elasticEntrance {{
        0% {{ opacity: 0; transform: scale(0.8) translateY(100px); }}
        70% {{ transform: scale(1.05) translateY(-10px); }}
        100% {{ opacity: 1; transform: scale(1) translateY(0); }}
    }}

    /* Sidebar Slide-in Bounce */
    @keyframes sidebarBounce {{
        0% {{ transform: translateX(-100%); }}
        100% {{ transform: translateX(0); }}
    }}

    /* Apply Staggered Bounces */
    .bounce-1 {{ animation: elasticEntrance 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55) forwards; opacity: 0; }}
    .bounce-2 {{ animation: elasticEntrance 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55) 0.1s forwards; opacity: 0; }}
    .bounce-3 {{ animation: elasticEntrance 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55) 0.2s forwards; opacity: 0; }}
    .bounce-4 {{ animation: elasticEntrance 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55) 0.3s forwards; opacity: 0; }}

    /* UI Styling */
    div[data-baseweb="input"], div[data-baseweb="textarea"] {{
        background-color: #FFFFFF !important;
        border: 2px solid #93C572 !important;
        border-radius: 16px !important;
        transition: all 0.3s ease;
    }}
    
    div[data-baseweb="input"]:focus-within {{
        transform: scale(1.02);
        border-color: #124D41 !important;
    }}

    .login-card {{
        border: 3px solid #93C572;
        border-radius: 40px;
        padding: 50px;
        background-color: #F9FFF9;
        text-align: center;
        max-width: 500px;
        margin: auto;
    }}

    .mflo-header {{ color: #124D41; font-size: 55px; font-weight: 900; margin: 0; }}

    div.stButton > button {{
        background: linear-gradient(90deg, #98FFD9, #7CFFCC) !important;
        color: #124D41 !important;
        border: none !important;
        font-weight: 800 !important;
        width: 100%;
        padding: 15px;
        border-radius: 14px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    
    div.stButton > button:hover {{ transform: scale(1.05); }}

    /* Sidebar Theme */
    section[data-testid="stSidebar"] {{
        background-color: #F0F4F2 !important;
        border-right: 1px solid #93C572;
        animation: sidebarBounce 0.7s cubic-bezier(0.165, 0.84, 0.44, 1);
    }}
    </style>
    """, unsafe_allow_html=True)

if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    logo_html = f'<div style="display: flex; justify-content: center;"><img src="data:image/png;base64,{logo_b64}" style="width:280px;"></div>' if logo_b64 else ""

    st.markdown(f"""
        <div class="login-card">
            {logo_html}
            <div style="color: #93C572; font-weight: 800; font-size: 28px; margin-top: 10px;">67+2 PODCAST</div>
            <div class="mflo-header">M-FLO</div>
            <hr style="border-top: 2px solid #93C572; opacity: 0.2; margin: 30px 0;">
        </div>
    """, unsafe_allow_html=True)

    _, col2, _ = st.columns([1, 1.8, 1])
    with col2:
        u = st.text_input("Physician ID", placeholder="Enter ID")
        p = st.text_input("Security Key", type="password")
        
        if st.button("AUTHENTICATE SYSTEM"):
            if u == "doctor1" and p == "mediflow2026":
                progress_bar = st.progress(0)
                for i in range(101):
                    time.sleep(0.005)
                    progress_bar.progress(i)
                st.session_state.auth = True
                st.rerun()
    
else:
    with st.sidebar:
        if logo_b64:
            st.markdown(f'<div style="text-align:center;"><img src="data:image/png;base64,{logo_b64}" width="120"></div>', unsafe_allow_html=True)
        st.title("M-FLO v2.1")
        if st.button("LOGOUT / LOCK"):
            st.session_state.auth = False
            st.rerun()

    # HEADER BOUNCE
    st.markdown('<div class="bounce-1">', unsafe_allow_html=True)
    st.subheader("⚕️ Patient Consultation Environment")
    st.markdown('</div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 2])
    
    with c1:
        st.markdown('<div class="bounce-2">', unsafe_allow_html=True)
        st.markdown("#### Patient Context")
        with st.container(border=True):
            st.markdown("### **J. Doe**")
            st.error("⚠️ ALLERGY: Penicillin")
            st.warning("⚠️ CONDITION: Hypertension")
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="bounce-3">', unsafe_allow_html=True)
        st.markdown("#### Clinical Interface")
        notes = st.text_area("Live Transcript", height=350)
        st.button("EXECUTE ANALYSIS")
        st.markdown('</div>', unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="bounce-4">', unsafe_allow_html=True)
        st.markdown("#### AI-Generated Orders")
        st.info("Awaiting analysis...")
        st.markdown('</div>', unsafe_allow_html=True)
