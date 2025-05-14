import streamlit as st

def project_card(title, description, status, key, on_click):
    """
    Creates a stylish card for projects
    
    Parameters:
    - title: Project title
    - description: Short project description
    - status: "completed", "in_progress", or "planned"
    - key: Unique key for the button
    - on_click: Function to call when clicked
    """
    
    # Status indicators and colors
    status_indicators = {
        "completed": {"emoji": "✅", "label": "Completed", "color": "#28a745"},
        "in_progress": {"emoji": "🚧", "label": "In Progress", "color": "#fd7e14"},
        "planned": {"emoji": "🔍", "label": "Planned", "color": "#6f42c1"}
    }
    
    indicator = status_indicators.get(status, status_indicators["planned"])
    
    st.markdown(f"""
    <div class="custom-card">
        <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
            <h3 style="margin: 0;">{title}</h3>
            <span style="background-color: {indicator['color']}1A; 
                        color: {indicator['color']}; 
                        padding: 3px 10px; 
                        border-radius: 12px; 
                        font-size: 0.8rem;
                        display: flex;
                        align-items: center;">
                {indicator['emoji']} {indicator['label']}
            </span>
        </div>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Simple button that calls the provided function
    if st.button("View Details", key=key):
        # Safety check to ensure on_click is callable
        if callable(on_click):
            on_click()
