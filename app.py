import streamlit as st
import base64
import os
import time

# 1. Page Config MUST be the first Streamlit command
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

# 2. CSS Styling (Dribbble Bouncy Physics)
st.markdown(f"""
    <style>
    .stApp {{ background: radial-gradient(circle at top right, #F7FFF9, #FFFFFF) !important; }}

    @keyframes springBounce {{
        0% {{ opacity: 0; transform: scale(0.9) translateY(40px); }}
        60% {{ transform: scale(1.03) translateY(-10px); }}
        80% {{ transform: scale(0.98) translateY(2px); }}
        100% {{ opacity: 1; transform: scale(1) translateY(0); }}
    }}

    .stagger-1 {{ animation: springBounce 0.9s cubic-bezier(0.34, 1.56, 0.64, 1) forwards; opacity: 0; }}
    .stagger-2 {{ animation: springBounce 0.9s cubic-bezier(0.34, 1.56, 0.64, 1) 0.15s forwards; opacity: 0; }}
    .stagger-3 {{ animation: springBounce 0.9s cubic-bezier(0.34, 1.56, 0.64, 1) 0.3s forwards; opacity: 0; }}

    div[data-testid="stVerticalBlockBorderWrapper"] {{
        background: rgba(255, 255, 255, 0.9) !important;
        backdrop-filter: blur(8px);
        border: 1.5px solid rgba(147, 197, 114, 0.1) !important;
        border-radius: 30px !important;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.04) !important;
        padding: 25px !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {{
        transform: translateY(-10px) scale(1.02);
        border-color: #93C572 !important;
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

    div.stButton > button {{
        background: linear-gradient(90deg, #98FFD9, #7CFFCC) !important;
        color: #124D41 !important;
        border: none !important;
        font-weight: 800 !important;
        border-radius: 15px !important;
    }}

    section[data-testid="stSidebar"] {{
        background-color: #FFFFFF !important;
        border-right: 1px solid #F0F0F0;
    }}
    </style>
    """, unsafe_allow_html=True)

# 3. Initialize Session State
if "auth" not in st.session_state:
    st.session_state.auth = False

# 4. Logic Gating
if not st.session_state.auth:
    # --- LOGIN PAGE ---
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    logo_html = f'<div style="display: flex; justify-content: center;"><img src="data:image/png;base64,{logo_b64}" style="width:280px;"></div>' if logo_b64 else ""

    st.markdown(f"""
        <div class="login-card">
            {logo_html}
            <div style="color: #93C572; font-weight: 800; font-size: 28px; margin-top: 10px;">67+2 PODCAST</div>
            <div style="color: #124D41; font-size: 55px; font-weight: 900; margin: 0;">M-FLO</div>
            <hr style="border-top: 2px solid #93C572; opacity: 0.2; margin: 30px 0;">
        </div>
    """, unsafe_allow_html=True)

    _, col2, _ = st.columns([1, 1.8, 1])
    with col2:
        u = st.text_input("Physician ID", placeholder="Enter ID")
        p = st.text_input("Security Key", type="password")
        
        if st.button("AUTHENTICATE SYSTEM"):
            # Change these to your desired credentials
            if u == "doctor1" and p == "mediflow2026":
                st.session_state.auth = True
                st.rerun()  # Forces the page to refresh and show the dashboard
            else:
                st.error("Invalid Credentials")

else:
    # --- DASHBOARD PAGE (Triggers when auth is True) ---
    with st.sidebar:
        if logo_b64:
            st.markdown(f'<div style="text-align:center;"><img src="data:image/png;base64,{logo_b64}" width="100"></div>', unsafe_allow_html=True)
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.button("🏥 Dashboard", use_container_width=True)
        st.button("📁 Patient Files", use_container_width=True)
        st.button("⚙️ Settings", use_container_width=True)
        st.divider()
        if st.button("Logout"):
            st.session_state.auth = False
            st.rerun()

    # Main Dashboard Content
    st.markdown('<div class="stagger-1"><h1 style="color: #124D41; font-weight: 900;">Clinical Workspace</h1></div>', unsafe_allow_html=True)
    
    col_a, col_b = st.columns([1, 2], gap="large")

    with col_a:
        st.markdown('<div class="stagger-2">', unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("### **Active Patient**")
            st.caption("Jane Doe • ID #9921")
            st.error("💊 **Allergy:** Penicillin")
            st.button("Full History", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_b:
        st.markdown('<div class="stagger-3">', unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("### **Clinical Orders**")
            st.checkbox("Lisinopril 10mg", value=True)
            st.checkbox("Blood Analysis", value=True)
            st.button("✨ Sync Records", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
