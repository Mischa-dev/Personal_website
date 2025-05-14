"""
Helper module to load images from GitHub raw content URLs
This is a workaround for deployment environments where local files aren't accessible
"""

# Dictionary mapping filenames to GitHub raw URLs
# You'll need to update these URLs with your actual GitHub repository
GITHUB_IMAGES = {
    # Cyberdeck images
    "kali closed.jpg": "https://raw.githubusercontent.com/gitgitgitgitgitgitgitgitgitgitgitgit/Personal_website/main/Projects/kali%20closed.jpg",
    "kali open.jpg": "https://raw.githubusercontent.com/gitgitgitgitgitgitgitgitgitgitgitgit/Personal_website/main/Projects/kali%20open.jpg",
    "kali on.jpg": "https://raw.githubusercontent.com/gitgitgitgitgitgitgitgitgitgitgitgit/Personal_website/main/Projects/kali%20on.jpg",
    
    # Red Team images
    "nethunter.jpg": "https://raw.githubusercontent.com/gitgitgitgitgitgitgitgitgitgitgitgit/Personal_website/main/Projects/nethunter.jpg", 
    "linux usbs.jpg": "https://raw.githubusercontent.com/gitgitgitgitgitgitgitgitgitgitgitgit/Personal_website/main/Projects/linux%20usbs.jpg",
    "rasberrypizerow2.jpg": "https://raw.githubusercontent.com/gitgitgitgitgitgitgitgitgitgitgitgit/Personal_website/main/Projects/rasberrypizerow2.jpg",
    "badusb.jpg": "https://raw.githubusercontent.com/gitgitgitgitgitgitgitgitgitgitgitgit/Personal_website/main/Projects/badusb.jpg", 
    "esp8266.jpg": "https://raw.githubusercontent.com/gitgitgitgitgitgitgitgitgitgitgitgit/Personal_website/main/Projects/esp8266.jpg"
    
    # Add more image mappings as needed
}

def get_github_image_url(filename):
    """Return the GitHub raw URL for an image filename"""
    if filename in GITHUB_IMAGES:
        return GITHUB_IMAGES[filename]
    return None
