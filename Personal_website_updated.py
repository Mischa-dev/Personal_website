import streamlit as st

# Initialize session state for navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'main'
if 'current_project' not in st.session_state:
    st.session_state.current_project = None

# Functions to handle navigation
def show_project(project_name):
    st.session_state.current_page = 'project_detail'
    st.session_state.current_project = project_name

def back_to_main():
    st.session_state.current_page = 'main'
    st.session_state.current_project = None

# Main Page Content
if st.session_state.current_page == 'main':
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
        # Use 2 columns for the first row
        col1, col2 = st.columns(2)

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

        # Use 2 columns for the second row
        col3, col4 = st.columns(2)

        with col3: # Moved Google Cert to the second row
            st.markdown("**Google Cybersecurity Professional Certificate**")
            # Add description
            st.markdown("""
            *   Covers: cybersecurity fundamentals; system administration basics; network defense & threat detection; identity & access management; incident response; compliance & governance
            """)
            try:
                # Use the correct, updated filename
                with open("GoogleCybersecurityProfessionalCertificateV2_Badge20250504-27-davnwp.pdf", "rb") as file:
                     # Added unique key and correct filename
                    st.download_button("View Certification", file, file_name="GoogleCybersecurityProfessionalCertificate.pdf", key="google_cert_home")
            except FileNotFoundError:
                st.error("Google Cybersecurity Certification file not found.")

        with col4: # Added column for SACA Cert
            st.markdown("**SACA Certified Industry 4.0 Associate - Basic Operations**") # Updated title
            # Update description for Basic Operations
            st.markdown("""
            *   Certifies skills for operators in an Industry 4.0 environment.
            *   Silver level: Awarded for successfully passing the written knowledge exam.
            """)
            try:
                # Use the correct source filename
                with open("SACA_Cert_MischaNelson_20250504.pdf", "rb") as file:
                     # Updated key and download filename
                    st.download_button("View Certification", file, file_name="SACA_Certified_I4.0_Associate_Basic_Operations.pdf", key="saca_basic_ops_cert_home")
            except FileNotFoundError:
                st.error("SACA Certification file not found.")

        st.markdown("---")  # Separator line

        # In Progress Certifications Section (Moved Down)
        st.markdown("### In Progress Certifications")
        st.markdown("**Cisco Certified Support Technician (CCST): Networking**")
        st.markdown("""
        *   Covers: OSI & TCP/IP models; CLI navigation; LAN/WAN configuration; IPv4 & IPv6 subnetting; network security controls; risk assessment
        """)

        st.markdown("---")  # Separator line

    with tab2:
        st.title("Projects")
        st.write("Below are the projects that I have completed, are in progress, or are to-do:")

        # Completed Projects
        st.markdown("### Completed Projects")
        # Using a 2x2 grid for 4 completed projects
        comp_row1_col1, comp_row1_col2 = st.columns(2)

        with comp_row1_col1:
            if st.button("Telegram Door Alert System", key="comp_tdas"): 
                show_project("Telegram Door Alert System")
            st.write("I created this Python project that uses two micro:bits and a computer to send a Telegram message when a door is opened or closed.")

        with comp_row1_col2:
            if st.button("Personal Website", key="comp_pers_site"):
                show_project("Personal Website")
            st.write("I coded this website 100% in Python using Streamlit to showcase my projects and provide information about me.")

        comp_row2_col1, comp_row2_col2 = st.columns(2)

        with comp_row2_col1:
            if st.button("Cyberdeck (Kali Linux on Raspberry Pi 4)", key="comp_cyberdeck"): 
                show_project("Cyberdeck (Kali Linux on Raspberry Pi 4)")
            st.write("I built this portable Kali Linux machine for pentesting and other cybersecurity tasks.")

        with comp_row2_col2:
            if st.button("ESP8266 Desk Gadget", key="comp_esp_gadget"): 
                show_project("ESP8266 Desk Gadget")
            st.write("I'm making this ESP8266 gadget with a screen and buttons to display time, weather, network speed, and a Pomodoro timer.")

        st.markdown("---")  # Separator line    # In Progress Projects
        st.markdown("### In Progress Projects")
        prog_row1_col1, prog_row1_col2, prog_row1_col3 = st.columns(3)
        
        with prog_row1_col1:
            if st.button("Seed-Based Secure Messaging System", key="prog_sbsms"): 
                show_project("Seed-Based Secure Messaging System")
            st.write("I'm developing this uncrackable messaging system that maps text to positions on a shared seed instead of using traditional encryption.")

        with prog_row1_col2:
            if st.button("TridentOS (Custom Debian Distro)", key="prog_tridentos"): 
                show_project("TridentOS (Custom Debian Distro)")
            st.write("I'm creating a custom Debian-based Linux distribution tailored to my specific needs.")

        with prog_row1_col3:
            if st.button("WSL Automation Toolkit", key="prog_wsl_auto"): 
                show_project("WSL Automation Toolkit")
            st.write("I'm building a collection of scripts and tools to automate tasks within Windows Subsystem for Linux.")

        prog_row2_col1, prog_row2_col2, prog_row2_col3 = st.columns(3)

        with prog_row2_col1:
            if st.button("ESP8266 Hacker Toolkit", key="prog_esp_hacker"): 
                show_project("ESP8266 Hacker Toolkit")
            st.write("I'm working on an ESP8266-based toolkit for various Wi-Fi and network-related experiments.")

        with prog_row2_col2:
            if st.button("Kali NetHunter Phone", key="prog_nethunter"): 
                show_project("Kali NetHunter Phone")
            st.write("I'm setting up Kali NetHunter on a compatible Android device for mobile penetration testing.")

        with prog_row2_col3:
            if st.button("Custom PCB Project", key="prog_pcb"): 
                show_project("Custom PCB Project")
            st.write("I'm designing and fabricating a custom Printed Circuit Board for one of my electronics projects.")

        st.markdown("---")  # Separator line

        # To-Do Projects
        st.markdown("### To-Do Projects")
        todo_col1, todo_col2, todo_col3 = st.columns(3)

        with todo_col1:
            if st.button("Telegram Weather Alert Bot", key="todo_weather_bot"): 
                show_project("Telegram Weather Alert Bot")
            st.write("I plan to create a Telegram bot that sends weather alerts to a user based on their set location.")

        with todo_col2:
            if st.button("Spotify Playback Switcher", key="todo_spotify_switch"): 
                show_project("Spotify Playback Switcher")
            st.write("I want to build a tool to easily switch Spotify playback between different devices.")

        with todo_col3:
            if st.button("Wazuh SIEM Server", key="todo_wazuh"): 
                show_project("Wazuh SIEM Server")
            st.write("I'm planning to set up and configure a Wazuh SIEM server for security monitoring.")

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

# Project Detail Page Content
elif st.session_state.current_page == 'project_detail':
    st.title(f"Project: {st.session_state.current_project}")
    st.button("Back to Main", on_click=back_to_main)

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
