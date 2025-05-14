import streamlit as st
import os
import sys
from datetime import datetime

# Add the components directory to the path so we can import from it
sys.path.append(os.path.dirname(__file__))

# Import custom components
try:
    from components.header import render_header
    from components.footer import render_footer
    from components.skills import render_skills
except ImportError:
    # Define fallback functions if imports fail
    def render_header(): 
        st.title("Mischa Nelson")
    def render_footer(): 
        st.markdown("---")
        st.write("© 2024 Mischa Nelson")
    def render_skills():
        st.write("Skills section")

# Define the set_project function before it's used
def set_project(name):
    """Helper function to set the current project and refresh"""
    st.session_state.current_project = name
    st.rerun()

# Update the get_image_path function to handle case-sensitivity
def get_image_path(filename):
    """Helper function to find images with flexible path handling for both local and deployed environments"""
    potential_paths = [
        f"Projects/{filename}",  # Local development path (uppercase)
        f"projects/{filename}",  # Deployment path (lowercase)
        f"./Projects/{filename}",  # Relative path (uppercase)
        f"./projects/{filename}",  # Relative path (lowercase)
        f"{os.path.dirname(__file__)}/Projects/{filename}",  # Absolute path (uppercase)
        f"{os.path.dirname(__file__)}/projects/{filename}",  # Absolute path (lowercase)
        f"../Projects/{filename}",  # One level up (uppercase)
        f"../projects/{filename}",  # One level up (lowercase)
    ]
    
    for path in potential_paths:
        if os.path.exists(path):
            return path
    
    # If image can't be found, return None so we can handle it gracefully
    return None

def load_image(filename, caption=None):
    """Load an image with proper error handling and fallbacks for deployment"""
    # Try to find the local image
    image_path = get_image_path(filename)
    if image_path:
        st.image(image_path, caption=caption)
        return True
    else:
        # For debugging, show directory information
        st.write(f"### Debugging Image Loading for: {filename}")
        st.write(f"Current working directory: {os.getcwd()}")
        st.write(f"Directory contents: {os.listdir('.')}")
        
        # Check both uppercase and lowercase "projects" directories
        projects_upper_exists = os.path.exists('Projects')
        projects_lower_exists = os.path.exists('projects')
        
        st.write(f"Projects directory exists (uppercase): {projects_upper_exists}")
        st.write(f"projects directory exists (lowercase): {projects_lower_exists}")
        
        # List contents of whichever projects directory exists
        if projects_upper_exists:
            st.write(f"Projects directory contents: {os.listdir('Projects')}")
        elif projects_lower_exists:
            st.write(f"projects directory contents: {os.listdir('projects')}")
            
            # Try loading from lowercase projects directory directly
            try:
                lowercase_path = f"projects/{filename}"
                st.image(lowercase_path, caption=caption)
                return True
            except:
                pass
        
        st.error(f"Image '{filename}' not available")
        return False

# Import the GitHub image loading function
try:
    from github_images import load_github_image
except ImportError:
    def load_github_image(filename, caption=None):
        return False

# Add global CSS with animations and smooth transitions - but let Streamlit handle the theming
st.markdown("""
<style>
    /* Animation for section entries */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Apply animations to sections */
    .stMarkdown, .stHeader, div[data-testid="stVerticalBlock"] > div {
        animation: fadeInUp 0.5s ease forwards;
    }
    
    /* Stagger animations */
    div[data-testid="stVerticalBlock"] > div:nth-child(2) {
        animation-delay: 0.1s;
    }
    div[data-testid="stVerticalBlock"] > div:nth-child(3) {
        animation-delay: 0.2s;
    }
    
    /* Project cards */
    .custom-card {
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 4px solid #3867d6;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .custom-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.12);
    }
    
    /* Featured project styling */
    .featured-project {
        border: none !important;
        border-radius: 12px !important;
        padding: 25px !important;
        background: linear-gradient(to right, rgba(56, 103, 214, 0.1), rgba(72, 219, 251, 0.05)) !important;
        margin-bottom: 30px !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08) !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .featured-project:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.15) !important;
    }
    
    .featured-badge {
        background: linear-gradient(45deg, #5c7aea, #3867d6) !important;
        color: white !important;
        padding: 6px 14px !important;
        border-radius: 20px !important;
        font-weight: 600 !important;
        font-size: 0.8em !important;
        margin-bottom: 15px !important;
        display: inline-block !important;
        box-shadow: 0 2px 10px rgba(0, 134, 227, 0.2) !important;
    }
    
    /* Time counter animation */
    .counter {
        font-size: 2.5rem;
        font-weight: 700;
        color: #3867d6;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for project navigation if it doesn't exist
if 'current_project' not in st.session_state:
    st.session_state.current_project = None

# Render the header at the top of the page
render_header()

# Create tabs for different sections of your portfolio
tab1, tab2, tab3, tab4 = st.tabs(["Home", "Projects", "Skills", "Google Cybersecurity Cert"])

# Home Page
with tab1:
    st.title("Mischa Nelson")
    
    st.write("""Mischa Nelson
I’m an 18-year-old high school student from Colorado, homeschooled with a mix of independent study and in-person programs. I’m passionate about creative problem-solving with a focus on cybersecurity, manufacturing automation, and electronics. I enjoy exploring how systems work and building smart, efficient solutions using both hardware and software.

Outside of tech and school, I enjoy playing bass, swimming, reading, and performing in musicals.""")

    st.markdown("---")  # Separator line

    st.markdown("### Certifications & Learning Journey")
    st.write("I've been fortunate to learn from some great resources. Here are some of the formal certifications I've earned so far:")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**PMI Project Management Ready**")
        st.markdown("""
        *   I learned about: project life cycles, stakeholder analysis, scope planning, and risk management basics
        """)
        try:
            with open("Ect-files/PMI Project Management Ready.pdf", "rb") as file:
                st.download_button("View Certificate", file, file_name="PMI_Project_Management_Ready.pdf", key="pmi_cert_home")
        except FileNotFoundError:
            st.error("PMI Certification file not found.")

    with col2:
        st.markdown("**Autodesk Certified User: Fusion 360®**")
        st.markdown("""
        *   Helped me understand: parametric modeling concepts, CAD sketching, assembly design, and technical drawing fundamentals
        """)
        try:
            with open("Ect-files/Autodesk Certified User Fusion 360.pdf", "rb") as file:
                st.download_button("View Certificate", file, file_name="Autodesk_Certified_User_Fusion_360.pdf", key="autodesk_cert_home")
        except FileNotFoundError:
            st.error("Autodesk Certification file not found.")

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("**Google Cybersecurity Professional Certificate**")
        st.markdown("""
        *   Introduced me to: security concepts, basic system administration, network security, and incident response procedures
        """)
        try:
            with open("Ect-files/GoogleCybersecurityProfessionalCertificateV2_Badge20250504-27-davnwp.pdf", "rb") as file:
                st.download_button("View Certificate", file, file_name="GoogleCybersecurityProfessionalCertificate.pdf", key="google_cert_home")
        except FileNotFoundError:
            st.error("Google Cybersecurity Certification file not found.")

    with col4:
        st.markdown("**SACA Certified Industry 4.0 Associate - Basic Operations**")
        st.markdown("""
        *   Gave me insights into: basic operations in Industry 4.0 environments
        *   Silver level: Received after completing the written knowledge exam
        """)
        try:
            with open("Ect-files/SACA_Cert_MischaNelson_20250504.pdf", "rb") as file:
                st.download_button("View Certificate", file, file_name="SACA_Certified_I4.0_Associate_Basic_Operations.pdf", key="saca_basic_ops_cert_home")
        except FileNotFoundError:
            st.error("SACA Certification file not found.")

    st.markdown("---")

    st.markdown("### Currently Learning")
    st.markdown("**Cisco Certified Support Technician (CCST): Networking**")
    st.markdown("""
    *   Working on understanding: OSI & TCP/IP models, network configurations, subnetting, and network security fundamentals
    """)

    st.markdown("---")  # Separator line

# Projects tab content 
with tab2:
    # Function to display project details
    def show_project_details(project_name):
        # Enhanced back button - made more prominent with columns and styling
        col1, col2 = st.columns([1, 3])
        with col1:
            if st.button("← Back to Projects", key="back_button", use_container_width=True):
                st.session_state.current_project = None
                st.rerun()
        
        st.markdown("---")  # Add separator after back button
        
        # Project details based on project name
        if project_name == "Telegram Door Alert System":
            st.header("Telegram Door Alert System")
            st.markdown("### Overview")
            st.write("This project leverages two micro:bits, a magnet, and a computer to send Telegram alerts when a door is opened or closed.")
            
            st.markdown("### How It Works")
            st.write("1. The first micro:bit detects the strength of the electromagnetic field from a magnet placed on the door")
            st.write("2. When the door is opened or closed, the change in the magnetic field is sensed")
            st.write("3. A signal is sent to the second micro:bit connected to a computer")
            st.write("4. The second micro:bit communicates with the computer via serial connection")
            st.write("5. The computer uses Telegram's API to send a message alerting you of the door's status")
            
            st.markdown("### Technologies Used")
            st.write("- Python")
            st.write("- Telegram Bot API")
            st.write("- BBC micro:bit")
            st.write("- Serial communication")
            st.write("- Electromagnetic field sensing")
            
            st.markdown("### Setup Instructions")
            st.write("To set up the Telegram bot for this project:")
            st.write("1. Create a Telegram bot following the official guide: https://core.telegram.org/bots")
            st.write("2. Get your chat ID and Bot token")
            st.write("3. Update these values in the computer.py script")
            
            st.markdown("### GitHub Repository")
            st.markdown("[View Code on GitHub](https://github.com/gitgitgitgitgitgitgitgitgitgitgitgit/Micro-bit_door_alarm)")
            
            # Add project image
            load_image("telegram_door_alert.jpg", caption="Telegram Door Alert System")
            
        elif project_name == "Cyberdeck (Kali Linux on Raspberry Pi 4)":
            st.header("Cyberdeck (Kali Linux on Raspberry Pi 4)")
            st.markdown("### Overview")
            st.write("A portable Kali Linux machine built for pentesting and cybersecurity tasks, housed in a rugged carrying case.")
            
            st.markdown("### Hardware Used")
            st.write("- Raspberry Pi 4")
            st.write("- Official Raspberry Pi touchscreen")
            st.write("- Bluetooth keyboard")
            st.write("- Waterproof, shockproof carrying case")
            
            st.markdown("### Software Configuration")
            st.write("- Kali Linux ARM distribution")
            st.write("- Custom scripts for hardware optimization")
            st.write("- Pre-installed security tools")
            
            st.subheader("Photos")
            col1, col2 = st.columns(2)
            with col1:
                # Try local loading first, fall back to GitHub if needed
                if not load_image("kali closed.jpg", caption="Cyberdeck Closed"):
                    load_github_image("kali closed.jpg", caption="Cyberdeck Closed")
            with col2:
                if not load_image("kali open.jpg", caption="Cyberdeck Open"):
                    load_github_image("kali open.jpg", caption="Cyberdeck Open")
            if not load_image("kali on.jpg", caption="Cyberdeck Powered On"):
                load_github_image("kali on.jpg", caption="Cyberdeck Powered On")
        
        elif project_name == "Personal Website":
            st.header("Personal Website")
            st.markdown("### Overview")
            st.write("This portfolio website showcases my projects, certifications, and skills - the very site you're viewing now!")
            
            st.markdown("### Technologies Used")
            st.write("- Python")
            st.write("- Streamlit framework")
            st.write("- GitHub for version control")
            
            st.markdown("### Features")
            st.write("- Responsive design")
            st.write("- Project portfolio with detailed pages")
            st.write("- Certification showcase with downloadable PDFs")
            st.write("- Multiple tabs for organized content")
            
            st.markdown("### GitHub Repository")
            st.markdown("[View Code on GitHub](https://github.com/gitgitgitgitgitgitgitgitgitgitgitgit/Personal_website)")
            
            # Add project image
            load_image("personal_website.jpg", caption="Personal Website Screenshot")
            
        elif project_name == "ESP8266 Desk Gadget":
            st.header("ESP8266 Desk Gadget")
            st.markdown("### Overview")
            st.write("An ESP8266-based desktop gadget with a screen and buttons to display various information.")
            
            st.markdown("### Features")
            st.write("- Time and date display")
            st.write("- Weather information")
            st.write("- Network speed monitoring")
            st.write("- Pomodoro timer for productivity")
            
            st.markdown("### Technologies Used")
            st.write("- ESP8266 microcontroller")
            st.write("- OLED display")
            st.write("- Arduino programming")
            st.write("- Various APIs for data")
            
            # Add project image
            load_image("esp8266_desk_gadget.jpg", caption="ESP8266 Desk Gadget")
            
        elif project_name == "Cipherless_relay":
            st.header("Cipherless_relay")
            st.markdown("### Overview")
            st.write("A seed-driven \"book cipher\" that hides your message in a deterministic pseudo-random text stream. Instead of sending encrypted files, you share a short hex pointer plus an encrypted phrase.")
            
            st.markdown("### How It Works")
            st.write("1. You and your correspondent agree on a secret string (the seed)")
            st.write("2. The system generates text blocks where each block (default 1024 characters) is created by hashing seed + block_index")
            st.write("3. A pseudo-random generator uses that hash to produce the block on demand")
            st.write("4. The system maps your phrase to a location by hashing phrase + seed to pick a block index and offset")
            st.write("5. It computes a numeric location = block_index * block_size + offset")
            st.write("6. Creates an opaque pointer by XORing the location with a 64-bit key derived from the seed hash")
            st.write("7. The phrase is encrypted by XORing each byte with a repeating key from SHA-256(seed)")
            st.write("8. The recipient reverses the XOR on the location, regenerates the block, and extracts the message")
            
            st.markdown("### Security Features")
            st.write("- No traditional encryption algorithms used - resistant to quantum computing attacks")
            st.write("- Messages are represented as positions within shared seed-based text")
            st.write("- Even if intercepted, the transmitted data reveals nothing without the seed")
            st.write("- Requires only Python 3.7+ and uses only standard library modules")
            
            st.markdown("### GitHub Repository")
            st.markdown("[View Code on GitHub](https://github.com/gitgitgitgitgitgitgitgitgitgitgitgit/Cipherless_relay/tree/main)")
            
            # Add project image
            load_image("cipherless_relay.jpg", caption="Cipherless_relay Project")
            
        elif project_name == "TridentOS":
            st.header("TridentOS")
            st.markdown("### Overview")
            st.write("A custom Ubuntu-based Linux distribution tailored to my specific needs and preferences.")
            
            st.markdown("### Current Progress")
            st.write("- Base system configured")
            st.write("- Working on package selection")
            st.write("- Creating custom installation scripts")
            
            # Add project image
            load_image("trident_os.jpg", caption="TridentOS Linux Distribution")
            
        elif project_name == "WSL Automation Toolkit":
            st.header("WSL Automation Toolkit")
            st.markdown("### Overview")
            st.write("A collection of scripts and tools to automate tasks within Windows Subsystem for Linux.")
            
            st.markdown("### Tools Included")
            st.write("- Environment setup scripts")
            st.write("- Windows-Linux file synchronization")
            st.write("- Service management helpers")
            st.write("- Development environment automation")
            
            st.markdown("### Technologies")
            st.write("- Bash scripting")
            st.write("- PowerShell")
            st.write("- Python")
            
            # Add project image
            load_image("wsl_automation.jpg", caption="WSL Automation Toolkit")
            
        elif project_name == "Red Team Pen-testing":
            st.header("Red Team Pen-testing")
            st.markdown("### Overview")
            st.write("A comprehensive collection of devices for mobile penetration testing, digital forensics, and cybersecurity research.")
            
            # Section 1: Mobile Devices
            st.markdown("### Mobile Devices")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### Kali NetHunter Phone")
                st.write("- Rootless implementation")
                st.write("- Full Kali Linux toolset")
                st.write("- Wireless network testing")
                st.write("- Penetration testing utilities")
                st.write("- **Status:** Configured and operational")
            
            with col2:
                load_image("nethunter.jpg", caption="Kali NetHunter")
            
            st.markdown("---")
            
            # Section 2: Bootable USB Drives
            st.markdown("### Portable Operating Systems")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### Bootable USB Drives")
                st.write("- Kali Linux with persistence")
                st.write("- Parrot OS with persistence")
                st.write("- Tails OS for anonymous operations")
                st.write("- **Status:** Prepared and tested")
            
            with col2:
                load_image("linux usbs.jpg", caption="Bootable Linux USB Drives")
            
            st.markdown("---")
            
            # Section 3: Specialized Hardware
            st.markdown("### Specialized Hardware")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### Raspberry Pi Devices")
                st.write("- Raspberry Pi Pico Bad USB")
                st.write("  ([GitHub Repository](https://github.com/kacperbartocha/pico-badusb))")
                st.write("  Turns a Pi Pico into a BadUSB device with DuckyScript-style syntax.")
                st.write("  Automates keystroke payloads similar to a Hak5 Rubber Ducky.")
                st.write("- Raspberry Pi Zero 2 W running Kali Linux")
                st.write("- Remote access via hotspot connection")
                st.write("- **Status:** Configured with SSH access")
            
            with col2:
                load_image("rasberrypizerow2.jpg", caption="Raspberry Pi Zero 2 W")
                load_image("badusb.jpg", caption="Pi Pico BadUSB")
            
            st.markdown("---")
            
            # Section 4: ESP8266 Tools Integration
            st.markdown("### ESP8266 Integration")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### ESP8266-Based Tools")
                st.write("- Wi-Fi Deauther & Beacon Flooder")
                st.write("  ([GitHub Repository](https://github.com/SpacehuhnTech/esp8266_deauther))")
                st.write("  Affordable Wi-Fi hacking firmware that scans networks, kicks clients")
                st.write("  off with deauth attacks, and floods beacon frames to clutter scanners.")
                st.write("  Great for testing 802.11 wireless security defenses.")
                
                st.write("- Rogue AP & Evil Twin")
                st.write("  ([GitHub Repository](https://github.com/Deborshibd/DevilTwin-ESP8266))")
                st.write("  Spins up a fake \"evil twin\" access point that clones a real SSID.")
                st.write("  When victims connect, their traffic can be sniffed or credentials harvested.")
                
                st.write("- Captive Portal")
                st.write("  ([GitHub Repository](https://github.com/beigeworm/ESP8266-Evil-Portal))")
                st.write("  Creates a captive portal on the ESP8266 that presents a fake Google")
                st.write("  login page. Perfect for social-engineering tests or security training.")
                
                st.write("- Network Reconnaissance")
                st.write("- **Status:** Hardware assembled, configuring firmware")
            
            with col2:
                load_image("esp8266.jpg", caption="ESP8266 NodeMCU")
            
        elif project_name == "Custom PCB Project":
            st.header("Custom PCB Project")
            st.markdown("### Overview")
            st.write("Designing and fabricating a custom Printed Circuit Board for one of my electronics projects.")
            
            st.markdown("### Project Scope")
            st.write("- Schematic design")
            st.write("- PCB layout")
            st.write("- Component selection")
            st.write("- Manufacturing and assembly")
            
            st.markdown("### Technologies Used")
            st.write("- KiCad for schematic and PCB design")
            st.write("- SMD components")
            st.write("- Professional PCB fabrication service")
            
            # Add project image
            load_image("custom_pcb.jpg", caption="Custom PCB Design")
            
        elif project_name == "Telegram Weather Alert Bot":
            st.header("Telegram Weather Alert Bot")
            st.markdown("### Overview")
            st.write("A planned Telegram bot that will send weather alerts to users based on their set location.")
            
            st.markdown("### Planned Features")
            st.write("- Location-based weather monitoring")
            st.write("- Customizable alert thresholds")
            st.write("- Daily forecasts")
            st.write("- Extreme weather warnings")
            
            st.markdown("### Technologies To Be Used")
            st.write("- Python")
            st.write("- Telegram Bot API")
            st.write("- Weather data API")
            st.write("- Database for user preferences")
            
            # Add project image
            load_image("telegram_weather_bot.jpg", caption="Telegram Weather Alert Bot Concept")
            
        elif project_name == "Spotify Playback Switcher":
            st.header("Spotify Playback Switcher")
            st.markdown("### Overview")
            st.write("A tool to easily switch Spotify playback between different devices with minimal interruption.")
            
            st.markdown("### Planned Features")
            st.write("- One-click device switching")
            st.write("- Maintain current song position")
            st.write("- Device presets for common scenarios")
            st.write("- Keyboard shortcuts")
            
            st.markdown("### Technologies To Be Used")
            st.write("- Python or JavaScript")
            st.write("- Spotify Web API")
            st.write("- Simple GUI interface")
            
            # Add project image
            load_image("spotify_switcher.jpg", caption="Spotify Playback Switcher Concept")
            
        elif project_name == "Wazuh SIEM Server":
            st.header("Wazuh SIEM Server")
            st.markdown("### Overview")
            st.write("Setting up and configuring a Wazuh SIEM (Security Information and Event Management) server for security monitoring.")
            
            st.markdown("### Planned Features")
            st.write("- Log collection from multiple sources")
            st.write("- Real-time alerts for security events")
            st.write("- Compliance monitoring")
            st.write("- Custom dashboards for security metrics")
            
            st.markdown("### Technologies To Be Used")
            st.write("- Wazuh")
            st.write("- Elasticsearch")
            st.write("- Kibana")
            st.write("- Linux server")
            
            # Add project image
            load_image("wazuh_siem.jpg", caption="Wazuh SIEM Server Dashboard")
    
    # Check if a project is selected
    if st.session_state.current_project:
        show_project_details(st.session_state.current_project)
    else:
        st.title("Projects")
        
        # Create legend for status indicators
        st.markdown("#### Project Status Legend:")
        col_legend1, col_legend2, col_legend3 = st.columns(3)
        with col_legend1:
            st.markdown("✅ **Completed**")
        with col_legend2:
            st.markdown("🚧 **In Progress**")
        with col_legend3:
            st.markdown("🔍 **Planned**")
        
        # Featured Project Section - Highlight Cipherless_relay as main project
        st.markdown("---")
        
        with st.container():
            # Create a visually distinct featured project box with custom CSS
            st.markdown("""
            <div class="featured-project">
                <span class="featured-badge">✨ FEATURED PROJECT</span>
                <h3>Cipherless_relay</h3>
                <p>A breakthrough encryption alternative: this seed-driven "book cipher" hides messages in deterministic pseudo-random text streams, making it quantum-computing resistant.</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Create two columns for project description and CTA button
            feat_col1, feat_col2 = st.columns([3, 1])
            
            with feat_col1:
                st.markdown("**Why it matters:** Unlike traditional encryption that will be vulnerable to quantum computers, this approach maps text to positions within shared seed-based text, leaving no encryption patterns to crack.")
            
            with feat_col2:
                if st.button("View Details", key="featured_project_button"):
                    set_project("Cipherless_relay")  # This will work now because set_project is defined
        
        st.markdown("---")  # Separator line

        # Cybersecurity Projects
        st.markdown("### Cybersecurity Projects")
        
        # Use a 2x2 grid for all cybersecurity projects for more consistent spacing
        cyber_row1_col1, cyber_row1_col2 = st.columns(2)
        cyber_row2_col1, cyber_row2_col2 = st.columns(2)
        
        with cyber_row1_col1:
            if st.button("✅ Cyberdeck (Kali Linux on Raspberry Pi 4)", key="cyber_deck"):
                set_project("Cyberdeck (Kali Linux on Raspberry Pi 4)")
            st.write("A portable Kali Linux machine built for pentesting and cybersecurity tasks.")
        
        with cyber_row1_col2:
            if st.button("🚧 Cipherless_relay", key="cyber_cipherless"):
                set_project("Cipherless_relay")
            st.write("A seed-driven \"book cipher\" system that maps text to positions on a shared seed.")
        
        with cyber_row2_col1:
            if st.button("✅ Red Team Pen-testing", key="cyber_nethunter"):
                set_project("Red Team Pen-testing")
            st.write("A comprehensive collection of mobile pentesting devices, including NetHunter, bootable drives, and specialized hardware.")
            
        with cyber_row2_col2:
            if st.button("🔍 Wazuh SIEM Server", key="cyber_wazuh"):
                set_project("Wazuh SIEM Server")
            st.write("Setting up and configuring a SIEM server for security monitoring and incident response.")

        st.markdown("---")  # Separator line

        # IoT & Hardware Projects
        st.markdown("### IoT & Hardware Projects")
        iot_col1, iot_col2 = st.columns(2)
        
        with iot_col1:
            if st.button("✅ Telegram Door Alert System", key="iot_door_alert"):
                set_project("Telegram Door Alert System")
            st.write("A Python project using micro:bits and a magnet to detect door status and send alerts.")
            
            if st.button("🚧 Custom PCB Project", key="iot_pcb"):
                set_project("Custom PCB Project")
            st.write("Designing and fabricating a custom Printed Circuit Board for an electronics project.")
        
        with iot_col2:
            if st.button("✅ ESP8266 Desk Gadget", key="iot_desk_gadget"):
                set_project("ESP8266 Desk Gadget")
            st.write("An ESP8266-based desktop gadget displaying time, weather, and network information.")
            
            if st.button("🔍 Telegram Weather Alert Bot", key="iot_weather_bot"):
                set_project("Telegram Weather Alert Bot")
            st.write("A Telegram bot that sends weather alerts based on user location and preferences.")

        st.markdown("---")  # Separator line

        # System & Automation Projects
        st.markdown("### System & Automation Projects")
        sys_col1, sys_col2, sys_col3 = st.columns(3)
        
        with sys_col1:
            if st.button("🚧 TridentOS", key="sys_tridentos"):
                set_project("TridentOS")
            st.write("A custom Ubuntu-based operating system tailored to my specific needs.")
        
        with sys_col2:
            if st.button("🚧 WSL Automation Toolkit", key="sys_wsl_auto"):
                set_project("WSL Automation Toolkit")
            st.write("A collection of scripts and tools to automate tasks within Windows Subsystem for Linux.")
        
        with sys_col3:
            if st.button("🔍 Spotify Playback Switcher", key="sys_spotify"):
                set_project("Spotify Playback Switcher")
            st.write("A tool to easily switch Spotify playback between different devices with minimal interruption.")

        st.markdown("---")  # Separator line

        # Web & Software Development
        st.markdown("### Web & Software Development")
        web_col1, web_col2 = st.columns(2)
        
        with web_col1:
            if st.button("✅ Personal Website", key="web_personal_site"):
                set_project("Personal Website")
            st.write("This portfolio website, coded in Python using Streamlit to showcase my projects and skills.")

# NEW Skills Tab
with tab3:
    render_skills()

# Google Cybersecurity Certification Portfolio
with tab4:
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
        {"title": "Professional Statement", "file": "Ect-files/1# Proffessional Statment..pdf", "desc": "My goals and interests in the cybersecurity field."},
        {"title": "NIST Framework Application", "file": "Ect-files/2# Use the NIST cybersecurity frameworks to respond..pdf", "desc": "Applying the NIST Cybersecurity Framework to respond to a security incident."},
        {"title": "Security Audit Report", "file": "Ect-files/3# Security audit..pdf", "desc": "Conducting a security audit and documenting findings."},
        {"title": "SQL Query Filtering", "file": "Ect-files/4# Apply filters to SQL queries.pdf", "desc": "Using SQL to filter and analyze security log data."},
        {"title": "Vulnerability Analysis", "file": "Ect-files/5# Analyze a vulnerable system for a small business .pdf", "desc": "Analyzing system vulnerabilities for a small business scenario."},
        {"title": "Python Algorithm for File Updates", "file": "Ect-files/6# Update a file with a python algorithm .pdf", "desc": "Using Python to automate the process of updating security-related files."},
        {"title": "Incident Handler's Journal", "file": "Ect-files/#7 Incident handler's journal .pdf", "desc": "Documenting the steps taken during a simulated security incident response."},
        {"title": "Resume", "file": "Ect-files/#8 Resume.pdf", "desc": "My professional resume detailing skills and experience."}
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

# Render footer
render_footer()
