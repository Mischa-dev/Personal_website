import streamlit as st
import random

def render_skills():
    st.markdown("## My Skills")
    
    # Define skill categories with simple lists instead of levels
    skills = {
        "Programming Languages": [
            "Python",
            "SQL",
            "C++ (Arduino)",
            "Ladder Logic",
            "Rust",
            "Java"
        ],
        "Cybersecurity & Networking": [
            "NIST CSF",
            "CIA Triad",
            "Wireshark",
            "Linux/Windows Hardening",  # Updated name
            "Threat Modeling",
            "Incident Response"
        ],
        "CAD/CAM & Manufacturing": [
            "Fusion 360",
            "LightBurn",
            "CAM & CNC (5-axis mill, lathe, plasma)",
            "PCB Design"
        ],
        "Electronics & Hardware": [
            "PLC Automation",
            "Fanuc iRVision",
            "Robotics",
            "Hardware Troubleshooting"
        ]
    }
    
    # Updated CSS without level styling
    st.markdown("""
    <style>
    .skill-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
        padding: 8px 15px;
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
                    <div class="skill-name">{skill}</div>
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
