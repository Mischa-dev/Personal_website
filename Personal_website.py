import streamlit as st

# Create tabs for different sections of your portfolio
tab1, tab2, tab3 = st.tabs(["Home", "Projects", "Google Cybersecurity Cert"])

# Home Page
with tab1:
    st.title("Mischa Nelson")
    
    # Updated introductory text
    st.write("""Mischa Nelson
I’m an 18-year-old high school student from Colorado, homeschooled with a mix of independent study and in-person programs. I’m passionate about creative problem-solving with a focus on cybersecurity, manufacturing automation, and electronics. I enjoy exploring how systems work and building smart, efficient solutions using both hardware and software.

Outside of tech and school, I enjoy playing bass, swimming, reading, and performing in musicals.""")

    st.markdown("---")  # Separator line

    # Completed Certifications Section (Moved Up)
    st.markdown("### Completed Certifications")
    col1, col2 = st.columns(2) # Changed to 2 columns

    with col1:
        st.markdown("**PMI Project Management Ready**")
        # Add description
        st.markdown("""
        *   Covers: project life cycle & phases; stakeholder analysis; scope, schedule & cost management; basic risk & quality management; project documentation
        """)
        try:
            with open("PMI Project Management Ready.pdf", "rb") as file:
                # Added unique key
                st.download_button("View Certification", file, file_name="PMI_Project_Management_Ready.pdf", key="pmi_cert_home")
        except FileNotFoundError:
            st.error("PMI Certification file not found.")

    with col2:
        st.markdown("**Autodesk Certified User: Fusion 360®**")
        # Add description
        st.markdown("""
        *   Covers: parametric modeling; sketching & constraints; assembly design; technical drawings; basic CAM toolpaths; rendering basics
        """)
        try:
            with open("Autodesk Certified User Fusion 360.pdf", "rb") as file:
                 # Added unique key
                st.download_button("View Certification", file, file_name="Autodesk_Certified_User_Fusion_360.pdf", key="autodesk_cert_home")
        except FileNotFoundError:
            st.error("Autodesk Certification file not found.")

    st.markdown("---")  # Separator line

    # In Progress Certifications Section (Moved Down)
    st.markdown("### In Progress Certifications")
    st.markdown("**Cisco Certified Support Technician (CCST): Networking**")
    st.markdown("""
    *   Covers: OSI & TCP/IP models; CLI navigation; LAN/WAN configuration; IPv4 & IPv6 subnetting; network security controls; risk assessment
    """)
    st.markdown("**Google Cybersecurity Professional Certificate**")
    st.markdown("""
    *   Covers: cybersecurity fundamentals; system administration basics; network defense & threat detection; identity & access management; incident response; compliance & governance
    *   *(See 'Google Cybersecurity Cert' tab for completed portfolio pieces)*
    """)

    st.markdown("---")  # Separator line

with tab2:
    st.title("Projects")
    st.write("Below are the projects that I have completed, are in progress, or are to-do:")

    # Completed Projects
    st.markdown("### Completed Projects")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Door Alarm"):
            st.link_button("Go to project", "https://github.com/gitgitgitgitgitgitgitgitgitgitgitgit/Micro-bit_door_alarm")
        st.write("A Python project utilizing two micro:bits and a computer to send a Telegram message when a door is opened or closed.")

    with col2:
        if st.button("Personal Website"):
            st.link_button("Go to project", "https://github.com/gitgitgitgitgitgitgitgitgitgitgitgit/Personal_website")
        st.write("This website, coded 100% In python to showcase my projects and provides information about me.")

    with col3:
        if st.button("Cyberdeck portable offensive cyber tool"):
            st.info("GitHub coming soon")
        st.write("A portable Kali Linux machine that can be used for pentesting and other cybersecurity tasks.")

    st.markdown("---")  # Separator line

    # In Progress Projects
    st.markdown("### In Progress Projects")
    col_in_progress1, col_in_progress2, col_in_progress3 = st.columns(3)

    with col_in_progress1:
        if st.button("Weather Alert Telegram Bot"):
            st.info("GitHub coming soon")
        st.write("A Telegram bot that sends weather alerts to a user based on their set location.")

    with col_in_progress2:
        if st.button("Cipherless Relay"):
            st.info("GitHub coming soon")
        st.write("A secure messaging system using a seed to map text locations instead of traditional encryption.")

    with col_in_progress3:
        if st.button("ESP8266 Desktop Info Hub"):
            st.info("GitHub coming soon")
        st.write("ESP8266 gadget with buttons/screen for time, weather, network speed, Pomodoro timer.")

    st.markdown("---")  # Separator line

    # To-Do Projects
    st.markdown("### To-Do Projects")
    st.write("*(No projects currently planned)*")

with tab3:
    st.title("Google Professional Cybersecurity Certification Portfolio")
    st.write("""
    This certification equips learners with in-demand skills needed for entry-level cybersecurity roles.
    The curriculum covers topics like security models, tools (SIEM, EDR), networks, threats, vulnerabilities,
    Python scripting for security tasks, SQL, and incident response frameworks like NIST.
    Below are the portfolio projects completed as part of this program.
    """)
    st.markdown("---")

    st.markdown("### Portfolio Pieces")

    portfolio_items = [
        {"title": "Professional Statement", "file": "1# Proffessional Statment..pdf", "desc": "My goals and interests in the cybersecurity field."},
        {"title": "NIST Framework Application", "file": "2# Use the NIST cybersecurity frameworks to respond..pdf", "desc": "Applying the NIST Cybersecurity Framework to respond to a security incident."},
        {"title": "Security Audit Report", "file": "3# Security audit..pdf", "desc": "Conducting a security audit and documenting findings."},
        {"title": "SQL Query Filtering", "file": "4# Apply filters to SQL queries.pdf", "desc": "Using SQL to filter and analyze security log data."},
        {"title": "Vulnerability Analysis", "file": "5# Analyze a vulnerable system for a small business .pdf", "desc": "Analyzing system vulnerabilities for a small business scenario."},
        {"title": "Python Algorithm for File Updates", "file": "6# Update a file with a python algorithm .pdf", "desc": "Using Python to automate the process of updating security-related files."},
        {"title": "Incident Handler's Journal", "file": "#7 Incident handler's journal .pdf", "desc": "Documenting the steps taken during a simulated security incident response."},
        {"title": "Resume", "file": "#8 Resume.pdf", "desc": "My professional resume detailing skills and experience."}
    ]

    cols = st.columns(2)
    col_index = 0

    for item in portfolio_items:
        with cols[col_index % 2]:
            st.markdown(f"**{item['title']}**")
            st.write(item['desc'])
            try:
                button_label = "View Resume" if item['title'] == "Resume" else "View Document"
                download_file_name = "Resume.pdf" if item['title'] == "Resume" else item['file'].replace("#", "").replace("..", ".").strip()
                button_key = f"download_{item['title'].replace(' ', '_').lower()}_tab3" if item['title'] == "Resume" else f"download_{item['title'].replace(' ', '_').lower()}_tab3"
                with open(item['file'], "rb") as file:
                    st.download_button(button_label, file, file_name=download_file_name, key=button_key)
            except FileNotFoundError:
                st.error(f"File not found: {item['file']}")
            st.markdown("---")
        col_index += 1

# Sidebar with buttons
st.sidebar.title("Connect with Me")
st.sidebar.link_button("LinkedIn", "https://www.linkedin.com/in/mischa-nelson-4a60842a7")
st.sidebar.link_button("GitHub", "https://github.com/gitgitgitgitgitgitgitgitgitgitgitgit")
st.sidebar.link_button("Email", "mailto:contact@mischanelson.dev")
st.sidebar.markdown("---") # Separator
st.sidebar.markdown("**Resume**")
try:
    with open("#8 Resume.pdf", "rb") as file:
        st.sidebar.download_button("View Resume", file, file_name="Resume.pdf", key="download_resume_sidebar")
except FileNotFoundError:
    st.sidebar.error("Resume file not found.")
