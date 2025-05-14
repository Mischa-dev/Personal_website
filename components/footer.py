import streamlit as st

def render_footer():
    st.markdown("---")
    
    # Current year for copyright
    import datetime
    current_year = datetime.datetime.now().year
    
    # Footer with animated icons
    st.markdown(f"""
    <style>
    .footer {{
        text-align: center;
        padding: 30px 0;
        color: var(--light-text, #6c757d);
        margin-top: 40px;
    }}
    
    .social-icons {{
        display: flex;
        justify-content: center;
        gap: 25px;
        margin: 20px 0;
    }}
    
    .social-icon {{
        font-size: 24px;
        color: var(--secondary, #0096c7);
        transition: transform 0.3s ease, color 0.3s ease;
    }}
    
    .social-icon:hover {{
        transform: translateY(-5px);
        color: var(--primary, #2E3B4E);
    }}
    </style>
    
    <div class="footer">
        <div class="social-icons">
            <a href="https://github.com/gitgitgitgitgitgitgitgitgitgitgitgit" target="_blank" class="social-icon">
                <i class="fab fa-github"></i>
            </a>
            <a href="https://www.linkedin.com/in/mischa-nelson-4a60842a7" target="_blank" class="social-icon">
                <i class="fab fa-linkedin"></i>
            </a>
            <a href="mailto:contact@mischanelson.dev" class="social-icon">
                <i class="fas fa-envelope"></i>
            </a>
        </div>
        <p>© {current_year} Mischa Nelson. All rights reserved.</p>
        <p style="font-size: 0.9rem;">Built with Python and Streamlit</p>
    </div>
    
    <!-- Import Font Awesome for social icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """, unsafe_allow_html=True)
