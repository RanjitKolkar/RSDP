import streamlit as st

# ============ PAGE CONFIG ============
st.set_page_config(
    page_title="RSDP on AI in Cyber Security & Forensic Science",
    page_icon="🛡️",
    layout="wide"
)

# ============ CUSTOM CSS ============
st.markdown("""
    <style>
    /* Background */
    .stApp {
        background-color: #f0f7ff;
        padding: 10px;
    }
    /* Responsive container */
    .main-container {
        max-width: 1100px;
        margin: auto;
        padding: 15px;
    }
    /* Headings */
    h2, h3 {
        color: #003366 !important;
    }
    /* Subheaders */
    .stMarkdown h4 {
        color: #004080 !important;
    }
    /* Info/Highlight Box */
    .highlight-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #e6f0ff;
        border: 1px solid #99c2ff;
    }
    /* Footer */
    .footer {
        text-align: center;
        font-size: 14px;
        color: #666;
        margin-top: 30px;
    }
    /* Responsive Image */
    .logo-img {
        max-width: 100%;
        height: auto;
    }
    @media (max-width: 768px) {
        .stColumn {
            width: 100% !important;
            display: block;
        }
    }
    </style>
""", unsafe_allow_html=True)

# ============ HEADER WITH LOGO ============
with st.container():
    col1, col2 = st.columns([2,5])
    with col1:
        st.image("nfsu emblem logo.png", use_container_width=True)  # responsive logo
    with col2:
        st.markdown("""
        ## National Forensic Sciences University, Goa Campus  
        ### Research and Skills Development Programme (RSDP)  
        ## AI in Cyber Security and Forensic Science
        📅 *15-17 September, 2025* | ⏳ *3 Days* | 🌐 *Hybrid Mode*  
        """)

st.markdown("---")

# Wrap all sections in a centered container
with st.container():
    # ============ ABOUT SECTION ============
    st.subheader("📌 About the Programme")
    st.write("""
    The **Three-Day Research and Skills Development Programme (RSDP)** on  
    **"AI in Cyber Security and Forensic Science"** aims to equip faculty members, researchers,  
    and professionals with knowledge and insights into the transformative role of AI in  
    cybersecurity and forensic science.
    """)

    # ============ OBJECTIVES ============
    st.subheader("🎯 Programme Objectives")
    st.markdown("""
    1. Introduce participants to the fundamentals of AI and its applications in forensic science.  
    2. Explore practical case studies and tools used in AI-driven forensic investigations.  
    3. Discuss ethical considerations and challenges in integrating AI into forensic practices.  
    4. Facilitate networking and knowledge-sharing among faculty and professionals.  
    """)

    # ============ BENEFITS ============
    st.subheader("🌟 Key Benefits")
    st.markdown("""
    - 📜 RSDP Certificate from **National Forensic Sciences University**  
    - 🤝 Networking Opportunities  
    - 👨‍🏫 Learn from **Domain Experts**  
    - 🧪 **Lab Visits** at NFSU Goa to explore well-equipped tools in Cyber Security and Forensics  
    """)

    # ============ SCHEDULE ============
    st.subheader("📅 Tentative Schedule")
    tabs = st.tabs(["Day 1", "Day 2", "Day 3"])

    with tabs[0]:
        st.markdown("""
        **Day 1: Foundations of AI in Cybersecurity and Forensic Science**  
        - **10:30 AM – 11:30 AM** : *Inauguration & Keynote: The Role of AI in Cybersecurity and Forensic Science* — Dr. J. M. Vyas, Hon’ble Vice Chancellor, NFSU  
        - **11:30 AM – 12:00 PM** : *Tea Break*  
        - **12:00 PM – 1:30 PM** : *Session 1: Introduction to AI in Cyber Security and Forensic Science* — Dr. Ranjit Kolkar, Assistant Professor  
        - **01:30 PM – 02:30 PM** : Lunch Break  
        - **2:30 PM – 4:00 PM** : *Session 2: Introduction to AI – Hands-on* — Dr. Ranjit Kolkar, Assistant Professor  
        """)

    with tabs[1]:
        st.markdown("""
        **Day 2: AI Applications in Digital Forensics**  
        - **10:30 AM – 11:30 AM** : *Session 3: AI-based Crime and Investigations* — Prof. (Dr.) Naveen Kumar Chaudhary, Director, NFSU Goa  
        - **11:30 AM – 12:00 PM** : Tea Break  
        - **12:00 PM – 1:30 PM** : *Session 4: Applied Data Science in Cyber Security and Forensic Science* — Dr. Jovi D’Silva, Assistant Professor  
        - **01:30 PM – 02:30 PM** : Lunch Break  
        - **2:30 PM – 4:00 PM** : *Session 5: Applications of AI Tools in Cyber Crime Investigation and Deep Fake Detection* — Expert  
        """)

    with tabs[2]:
        st.markdown("""
        **Day 3: Emerging Trends and Practical Insights**  
        - **10:30 AM – 11:30 AM** : *Session 6: Deep Learning for Cybercrime Investigations* — Dr. Ranjit Kolkar, Assistant Professor  
        - **11:30 AM – 12:00 PM** : Tea Break  
        - **12:00 PM – 1:30 PM** : *Session 7: Ethics in AI for Criminal Justice System* — Prof. (Dr.) Naveen Kumar Chaudhary, Director, NFSU Goa  
        - **01:30 PM – 02:30 PM** : Lunch Break  
        - **2:30 PM – 4:00 PM** : *Panel Discussion: The Future of AI in Cybersecurity and Forensic Science* — Expert Panelists  
        """)

    # ============ OUTCOMES ============
    st.subheader("✅ Expected Outcomes")
    st.markdown("""
    - Understand the integration of AI in cybersecurity and forensics.  
    - Gain hands-on experience with AI tools and datasets.  
    - Encourage interdisciplinary research and curriculum development.  
    """)

     # --- Registration Fees ---
    st.markdown("## 💰 Registration Fees")
    st.markdown("""
    - **Academicians / Govt. Professionals** : INR 1000  
    - **Research Scholars** : INR 500  
    - **Online Participants** : INR 500  
    - **Industry Professionals** : INR 1500  
    - **International Participants** : USD 25  
    """)

    st.info("👉 Note: Registration fee does not include accommodation. It includes a Tea and Lunch only")

    # ============ REGISTRATION ============
    st.subheader("📝 Registration")
    st.markdown("""
    **Registration Fees**  
    - 🎓 Academic: INR 500  
    - 📚 Research Scholar: INR 250  
    - 💻 Online Participants: INR 250  
    - 🌍 International Participants: $25  
    """)
    st.info("👉 Please complete your registration using the link below:")

    st.markdown(
        """
        <a href="https://forms.gle/ajJs932f9EbnXm1W9" target="_blank">
            <button style="
                background-color:#1E90FF;
                color:white;
                border:none;
                padding:12px 24px;
                border-radius:8px;
                font-size:16px;
                cursor:pointer;">
                📌 Register Here
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )


    # ============ ORGANIZING COMMITTEE ============
    st.subheader("👥 Organizing Committee")
    st.markdown("""
    <div class="highlight-box">
    <b>Chief Patron:</b> Dr. J. M. Vyas, Hon'ble Vice-Chancellor, NFSU <br>
    <b>Chair:</b> Prof. (Dr.) Naveen Kumar Chaudhary, Director, NFSU Goa  <br>
    <b>Co-Chair:</b> Dr. Lokesh Chouhan, Dean Academics, NFSU Goa  <br>
    <b>Co-Ordinators:</b> Dr. Ranjit Kolkar and Dr. Inderbhan Singh, Assistant Professor, NFSU Goa  
    </div>
    """, unsafe_allow_html=True)

# ============ FOOTER ============
st.markdown("---")
st.markdown('<div class="footer">📍 Organized by <b>National Forensic Sciences University, Goa Campus</b></div>', unsafe_allow_html=True)
