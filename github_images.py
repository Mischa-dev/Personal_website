"""
Helper module to load images from GitHub raw content URLs
This is a workaround for deployment environments where local files aren't accessible
"""
import streamlit as st
from urllib.parse import quote

# Dictionary mapping filenames to GitHub raw URLs
# Replace this URL with your actual GitHub repository URL
GITHUB_IMAGE_BASE_URL = "https://raw.githubusercontent.com/gitgitgitgitgitgitgitgitgitgitgitgit/Personal_website/main/projects/"

def get_github_image_url(filename: str) -> str:
    """Return the GitHub raw URL for an image filename."""
    # Properly encode the filename for use in a URL
    encoded_filename = quote(filename)
    return f"{GITHUB_IMAGE_BASE_URL}{encoded_filename}"

def load_github_image(filename, caption=None):
    """Load an image directly from GitHub raw content"""
    try:
        url = get_github_image_url(filename)
        st.image(url, caption=caption)
        return True
    except Exception as e:
        st.error(f"Failed to load image from GitHub: {str(e)}")
        return False
