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
    .stApp {{
        background: radial-gradient(circle at top right, #F0FFF4, #FFFFFF) !important;
    }}

    /* Spring Animation for Dribbble-style Pop */
    @keyframes dribbblePop {{
        0% {{ opacity: 0; transform: scale(0.8) translateY(40px); }}
        60% {{ opacity: 1; transform: scale(1.03) translateY(-10px); }}
        80% {{ transform: scale(0.98) translateY(2px); }}
        100% {{ opacity: 1; transform: scale(1) translateY(0); }}
    }}

    .pop-1 {{ animation: dribbblePop 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards; opacity: 0; }}
    .pop-2 {{ animation: dribbblePop 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) 0.1s forwards; opacity: 0; }}
    .pop-3 {{ animation: dribbblePop 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) 0.2s forwards; opacity: 0; }}

    /* Floating Glass Cards */
    div[data-testid="stVerticalBlockBorderWrapper"] {{
        background: rgba(255, 255, 255, 0.75) !important;
        backdrop-filter: blur(15px) !important;
        border: 1px solid rgba(147, 197, 114, 0.15) !important;
        border-radius: 28px !important;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.04) !important;
        padding: 25px !important;
        transition: all 0.4s ease;
    }}
    
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {{
        transform: translateY(-8px);
        border-color: #93C572 !important;
    }}

    /* Sidebar Refinement */
    section[data-testid="stSidebar"] {{
        background-color: #FFFFFF !important;
        border-right: 1px solid #EAEAEA;
    }}

    .nav-text {{ font-weight: 600; color: #124D41; }}
    .mflo-title {{ color: #124D41; font-size: 36px; font-weight: 900; letter-spacing: -1.5px; }}
    </style>
    """, unsafe_allow_html=True)

if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    # (Pistachio Login Logic remains here...)
    st.markdown('<div class="pop-1" style="text-align:center;"><h1>M-FLO Secure Access</h1></div>', unsafe_allow_html=True)
    if st.button("Simulate Login"):
        st.session_state.auth = True
        st.rerun()

else:
    # --- UPDATED SIDEBAR MENU ---
    with st.sidebar:
        if logo_b64:
            st.markdown(f'<div style="text-align:center;"><img src="data:image/png;base64,{logo_b64}" width="90"></div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Navigation Links
        st.button("🏠 Homepage", use_container_width=True)
        st.button("💬 Messages", use_container_width=True)
        st.button("👤 Patients", use_container_width=True)
        st.button("📅 Reservations", use_container_width=True)
        st.button("🤝 Community", use_container_width=True)
        
        st.divider()
        if st.button("Logout"):
            st.session_state.auth = False
            st.rerun()

    # --- CONTENT AREA ---
    st.markdown('<div class="pop-1"><p class="mflo-title">Clinical Intelligence Workspace</p></div>', unsafe_allow_html=True)
    
    col_l, col_r = st.columns([1.5, 1], gap="medium")

    with col_l:
        st.markdown('<div class="pop-2">', unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("### **🤝 Doctor Community**")
            st.caption("Trending Discussions in Cardiology & GPT-4 Med")
            
            # Reddit-style Feed
            with st.expander("u/Dr_Smith: Advice on chronic hypertension in 40yo male?", expanded=True):
                st.write("Has anyone seen resistance to Lisinopril 10mg lately? Thinking of switching to Losartan.")
                st.caption("💬 12 comments • 🔼 45 upvotes")
            
            with st.expander("u/Surgery_Lead: New robotic techniques for mitral valve"):
                st.write("Sharing my findings from last week's operation using the new v2.1 orchestrator.")
                st.caption("💬 4 comments • 🔼 18 upvotes")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_r:
        st.markdown('<div class="pop-3">', unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("### **📅 Upcoming Reservations**")
            st.write("Today's Schedule:")
            st.info("09:00 - Jane Doe (Consultation)")
            st.success("10:30 - John Wick (Follow-up)")
            st.warning("13:00 - Pending Approval")
            st.button("Manage Calendar", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Bottom Row Insights
    st.markdown('<div class="pop-3">', unsafe_allow_html=True)
    with st.container(border=True):
        st.write("### **💬 Recent Messages**")
        st.caption("From: Nurse Sarah - 'Patient in Room 4 is ready for review.'")
        st.button("Open Message Center", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
