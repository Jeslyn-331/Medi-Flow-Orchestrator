import streamlit as st
import base64
import os
import time

st.set_page_config(
    page_title="M-FLO | Workflow", 
    page_icon="⚕️", 
    layout="wide"
)

def get_base64(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

logo_b64 = get_base64("logo_medical.png")

st.markdown(f"""
    <style>
    /* 1. Global Background: Soft Mint Gradient */
    .stApp {{
        background: radial-gradient(circle at top right, #F0FFF4, #FFFFFF) !important;
    }}

    /* 2. Fluid Spring Animations */
    @keyframes dribbbleBounce {{
        0% {{ opacity: 0; transform: scale(0.8) translateY(40px); }}
        70% {{ transform: scale(1.02) translateY(-5px); }}
        100% {{ opacity: 1; transform: scale(1) translateY(0); }}
    }}

    .stagger-1 {{ animation: dribbbleBounce 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards; opacity: 0; }}
    .stagger-2 {{ animation: dribbbleBounce 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) 0.1s forwards; opacity: 0; }}
    .stagger-3 {{ animation: dribbbleBounce 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) 0.2s forwards; opacity: 0; }}

    /* 3. Floating Glass Cards */
    div[data-testid="stVerticalBlockBorderWrapper"] {{
        background: rgba(255, 255, 255, 0.7) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(147, 197, 114, 0.2) !important;
        border-radius: 24px !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.03) !important;
        padding: 20px !important;
        transition: transform 0.3s ease;
    }}
    
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {{
        transform: translateY(-5px);
        border-color: #93C572 !important;
    }}

    /* 4. Minimalist Sidebar */
    section[data-testid="stSidebar"] {{
        background-color: #FFFFFF !important;
        border-right: 1px solid #EAEAEA;
    }}

    /* 5. Inputs and Typography */
    .mflo-title {{
        color: #124D41;
        font-size: 32px;
        font-weight: 800;
        letter-spacing: -1px;
    }}

    div[data-baseweb="textarea"] textarea {{
        border-radius: 16px !important;
        border: 1px solid #E0E0E0 !important;
        background: #F9F9F9 !important;
    }}
    </style>
    """, unsafe_allow_html=True)

if "auth" not in st.session_state:
    st.session_state.auth = False

# --- LOGIC GATING ---
if not st.session_state.auth:
    # (Assuming the login code from previous steps remains here)
    st.title("Please Login")
    if st.button("Simulate Login"):
        st.session_state.auth = True
        st.rerun()

else:
    # --- DASHBOARD LAYOUT ---
    with st.sidebar:
        if logo_b64:
            st.markdown(f'<div style="text-align:center;"><img src="data:image/png;base64,{logo_b64}" width="100"></div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("Dashboard")
        st.button("Patient Files")
        st.button("Settings")
        st.divider()
        if st.button("Logout"):
            st.session_state.auth = False
            st.rerun()

    # Header section
    st.markdown('<div class="stagger-1"><p class="mflo-title">Clinical Intelligence Workspace</p></div>', unsafe_allow_html=True)
    
    col_a, col_b = st.columns([1, 2.5], gap="large")

    with col_a:
        st.markdown('<div class="stagger-2">', unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("### **Active Patient**")
            st.caption("Jane Doe • ID #9921")
            st.divider()
            st.error("💊 **Allergy:** Penicillin")
            st.info("📊 **Last Visit:** 2 days ago")
            st.markdown("<br>", unsafe_allow_html=True)
            st.button("View Full Profile", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_b:
        st.markdown('<div class="stagger-3">', unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("### **Live Consultation**")
            transcript = st.text_area("Listening to audio...", height=300, placeholder="Transcribed text will appear here...")
            
            # Action Row
            btn_left, btn_right = st.columns(2)
            with btn_left:
                st.button("🎙️ Pause Recording", use_container_width=True)
            with btn_right:
                st.button("✨ Run AI Analysis", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Bottom Row: Generated Insights
    st.markdown('<div class="stagger-3">', unsafe_allow_html=True)
    with st.container(border=True):
        st.write("### **AI-Generated Clinical Orders**")
        st.info("System standby. Start recording to generate orders.")
    st.markdown('</div>', unsafe_allow_html=True)
