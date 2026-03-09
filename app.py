import streamlit as st
import base64
import os
import time

st.set_page_config(
    page_title="M-FLO | Secure Access Portal", 
    page_icon="⚕️", 
    layout="wide"
)

def get_base64_image(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

logo_b64 = get_base64_image("logo_medical.png")

st.markdown(f"""
    <style>
    /* 1. Global Backgrounds */
    .stApp {{ background-color: #FFFFFF !important; }}

    /* 2. Dribbble-Style Elastic Bounce Keyframes */
    @keyframes elasticEntrance {{
        0% {{ opacity: 0; transform: scale(0.8) translateY(80px); }}
        70% {{ transform: scale(1.05) translateY(-10px); }}
        100% {{ opacity: 1; transform: scale(1) translateY(0); }}
    }}

    /* Animation Staggering */
    .stagger-1 {{ animation: elasticEntrance 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55) forwards; opacity: 0; }}
    .stagger-2 {{ animation: elasticEntrance 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55) 0.1s forwards; opacity: 0; }}
    .stagger-3 {{ animation: elasticEntrance 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55) 0.2s forwards; opacity: 0; }}

    /* 3. Login Page Styling (Pistachio Frame) */
    .login-card {{
        border: 3px solid #93C572;
        border-radius: 40px;
        padding: 50px;
        background-color: #F9FFF9;
        text-align: center;
        max-width: 500px;
        margin: auto;
        box-shadow: 0 20px 40px rgba(0,0,0,0.05);
    }}

    /* 4. Dashboard Floating Glass Cards */
    div[data-testid="stVerticalBlockBorderWrapper"] {{
        background: rgba(255, 255, 255, 0.8) !important;
        backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(147, 197, 114, 0.2) !important;
        border-radius: 28px !important;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.04) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}

    div[data-testid="stVerticalBlockBorderWrapper"]:hover {{
        transform: translateY(-8px) scale(1.01);
        border-color: #93C572 !important;
    }}

    /* 5. Typography and Inputs */
    .mflo-title {{ color: #124D41; font-size: 32px; font-weight: 850; letter-spacing: -1px; }}
    
    div[data-baseweb="input"], div[data-baseweb="textarea"] {{
        background-color: #FFFFFF !important;
        border: 2px solid #93C572 !important;
        border-radius: 12px !important;
    }}

    div.stButton > button {{
        background: linear-gradient(90deg, #98FFD9, #7CFFCC) !important;
        color: #124D41 !important;
        border: none !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        width: 100%;
        padding: 15px;
        border-radius: 14px;
        transition: all 0.3s ease;
    }}
    </style>
    """, unsafe_allow_html=True)

if "auth" not in st.session_state:
    st.session_state.auth = False

# --- LOGIC GATING ---
if not st.session_state.auth:
    # --- PISTACHIO LOGIN PAGE ---
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    logo_html = f'<div style="display: flex; justify-content: center;"><img src="data:image/png;base64,{logo_b64}" style="width:280px;"></div>' if logo_b64 else ""

    st.markdown(f"""
        <div class="login-card">
            {logo_html}
            <div style="color: #93C572; font-weight: 800; font-size: 28px; letter-spacing: 1px; margin-top: 10px;">67+2 PODCAST</div>
            <div style="color: #124D41; font-size: 55px; font-weight: 900; margin: 0; letter-spacing: -2px;">M-FLO</div>
            <p style="color: #124D41; font-size: 16px; font-weight: 500; opacity: 0.8;">Medi-Flow Orchestrator v2.1 | Secure Portal</p>
            <hr style="border-top: 2px solid #93C572; opacity: 0.2; margin: 30px 0;">
        </div>
    """, unsafe_allow_html=True)

    _, col2, _ = st.columns([1, 1.8, 1])
    with col2:
        u = st.text_input("Physician ID", placeholder="Enter ID")
        p = st.text_input("Security Key", type="password", placeholder="••••••••")
        
        if st.button("AUTHENTICATE SYSTEM"):
            if u == "doctor1" and p == "mediflow2026":
                pb = st.progress(0)
                for i in range(101):
                    time.sleep(0.005)
                    pb.progress(i)
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Access Denied.")

else:
    # --- BOUNCY DASHBOARD PAGE ---
    with st.sidebar:
        if logo_b64:
            st.markdown(f'<div style="text-align:center;"><img src="data:image/png;base64,{logo_b64}" width="100"></div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.write("Logged in: **Dr. John Doe**")
        st.divider()
        if st.button("Logout"):
            st.session_state.auth = False
            st.rerun()

    # Title with Bouncy Entrance
    st.markdown('<div class="stagger-1"><p class="mflo-title">Clinical Intelligence Workspace</p></div>', unsafe_allow_html=True)
    
    col_a, col_b = st.columns([1, 2.5], gap="large")

    with col_a:
        st.markdown('<div class="stagger-2">', unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("### **Active Patient**")
            st.caption("Jane Doe • ID #9921")
            st.divider()
            st.error("💊 **Allergy:** Penicillin")
            st.info("📊 **Condition:** Hypertension")
            st.markdown("<br>", unsafe_allow_html=True)
            st.button("View Full Profile", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_b:
        st.markdown('<div class="stagger-3">', unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("### **Clinical Orders**")
            st.write("Select verified orders to finalize:")
            st.checkbox("Lisinopril 10mg - 1x Daily", value=True)
            st.checkbox("Blood Work - CBC", value=True)
            st.checkbox("Chest X-ray - STAT", value=False)
            st.divider()
            st.button("✨ Approve and Sync Orders", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Bottom Summary Bouncy Card
    st.markdown('<div class="stagger-3">', unsafe_allow_html=True)
    with st.container(border=True):
        st.write("### **System Intelligence Summary**")
        st.success("All clinical databases are operational. No pending alerts for current physician shift.")
    st.markdown('</div>', unsafe_allow_html=True)
