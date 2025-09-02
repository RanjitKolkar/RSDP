import streamlit as st

# Page config
st.set_page_config(
    page_title="RSDP - NFSU Goa",
    page_icon=":shield:",
    layout="wide"
)

# ================== MAINTENANCE NOTICE ==================
st.markdown(
    """
    <div style="
        background-color:#fff3cd;
        color:#856404;
        padding:15px;
        border-radius:8px;
        border:1px solid #ffeeba;
        font-size:16px;
        text-align:center;
        margin-bottom:20px;">
        ⚠️ This site is currently <b>under maintenance. We will get back to you shortly</b>.  
        
    </div>
    """,
    unsafe_allow_html=True
)





# ================== FOOTER ==================
st.markdown(
    """
    <hr>
    <div style="text-align:center; color:gray; font-size:14px;">
        © 2025 National Forensic Sciences University, Goa Campus
    </div>
    """,
    unsafe_allow_html=True
)
