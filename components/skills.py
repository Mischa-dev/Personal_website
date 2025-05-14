import streamlit as st
import random

def render_skills():
    st.markdown("## My Skills")
    
    # Define skill categories and their items with text-based levels
    skills = {
        "Programming Languages": [
            {"name": "Python", "level": "Beginner"},
            {"name": "SQL", "level": "Beginner"},
            {"name": "C++ (Arduino)", "level": "Beginner"},
            {"name": "Ladder Logic", "level": "Beginner"},
            {"name": "Rust", "level": "Beginner"},
            {"name": "Java", "level": "Beginner"}
        ],
        "Cybersecurity & Networking": [
            {"name": "NIST CSF", "level": "Beginner"},
            {"name": "CIA Triad", "level": "Beginner"},
            {"name": "Wireshark", "level": "Beginner"},
            {"name": "Linux Hardening", "level": "Beginner"},
            {"name": "Threat Modeling", "level": "Beginner"},
            {"name": "Incident Response", "level": "Beginner"}
        ],
        "CAD/CAM & Manufacturing": [
            {"name": "Fusion 360", "level": "Intermediate"},
            {"name": "LightBurn", "level": "Beginner"},
            {"name": "CAM & CNC (5-axis mill, lathe, plasma)", "level": "Beginner"},
            {"name": "PCB Design", "level": "Beginner"}
        ],
        "Electronics & Hardware": [
            {"name": "PLC Automation", "level": "Intermediate"},
            {"name": "Fanuc iRVision", "level": "Beginner"},
            {"name": "Robotics", "level": "Beginner"},
            {"name": "Hardware Troubleshooting", "level": "Beginner"}
        ]
    }
    
    # CSS for skill items - updated to work with dark mode
    st.markdown("""
    <style>
    .skill-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
        padding: 8px 12px;
        background-color: #182C61; /* Dark blue background for dark mode */
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .skill-item:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.25);
        border-left: 3px solid #3867d6;
    }
    
    .skill-name {
        font-weight: 500;
        font-size: 1rem;
        color: #eaf0ff; /* Light text color for dark mode */
    }
    
    .skill-level {
        font-weight: 500;
        padding: 3px 12px;
        border-radius: 12px;
        font-size: 0.85rem;
        color: white;
    }
    
    .level-Advanced {
        background-color: #48dbfb;  /* Bright cyan blue */
    }
    
    .level-Intermediate {
        background-color: #3867d6;  /* Medium blue */
    }
    
    .level-Beginner {
        background-color: #5c7aea;  /* Lighter blue */
    }
    
    .container {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0,0,0,0.15);
        margin-bottom: 20px;
        background-color: #0a1931; /* Dark background for container */
        border-left: 3px solid #5c7aea;
    }

    .container h3 {
        color: #eaf0ff; /* Light text color for headings */
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Display skills by category in 2 columns
    col1, col2 = st.columns(2)
    
    # Distribute skill categories between columns
    categories = list(skills.keys())
    for i, category in enumerate(categories):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div class="container">
                <h3>{category}</h3>
            """, unsafe_allow_html=True)
            
            for skill in skills[category]:
                # Generate a unique animation delay for each skill
                delay = random.uniform(0.1, 0.5)
                
                st.markdown(f"""
                <div class="skill-item" style="animation: fadeIn 0.5s forwards; animation-delay: {delay}s; opacity: 0;">
                    <div class="skill-name">{skill['name']}</div>
                    <div class="skill-level level-{skill['level']}">{skill['level']}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    # Add animation for fade-in effect
    st.markdown("""
    <style>
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)
