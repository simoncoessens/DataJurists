import streamlit as st
from PIL import Image
import utils

# Function to read the base64 string from a file
def read_base64_from_file(file_path):
    with open(file_path, "r") as file:
        encoded_string = file.read()
    return encoded_string

# Set the page configuration with a custom icon
im = Image.open('annalogo.png')
st.set_page_config(page_title="ANNA", layout="wide", initial_sidebar_state="collapsed", page_icon=im)

# Add background to the current page
utils.add_bg_from_base64("encoded_background.txt")

# Read the base64-encoded fonts from the text files
font_base64_1 = read_base64_from_file('encoded_moncheri.txt')  # Replace with the path to your base64 .txt for the first font
font_base64_2 = read_base64_from_file('encoded_tt_commons.txt')  # Replace with the path to your base64 .txt for the second font

# Define CSS for both fonts using the base64 data read from the text files
font_css = f"""
<style>
@font-face {{
  font-family: 'MyCustomFont';
  src: url(data:font/truetype;charset=utf-8;base64,{font_base64_1}) format('truetype');
}}
@font-face {{
  font-family: 'SecondaryFont';
  src: url(data:font/opentype;charset=utf-8;base64,{font_base64_2}) format('opentype');
}}
h1 {{
  font-family: 'MyCustomFont';
  font-size: 60px;
  color: #000;  /* Darker text */
  font-weight: bold;
  text-align: center;  /* Center the heading */
}}
p {{
  font-family: 'SecondaryFont';
  font-size: 20px;
  color: #000;
  font-weight: normal;
  text-align: center;  /* Center the smaller text */
  line-height: 1.5;  /* Adjust line height for readability */
}}
[data-testid="collapsedControl"] {{
    display: none;
}}
</style>
"""

# Inject the CSS into the Streamlit app
st.markdown(font_css, unsafe_allow_html=True)

# Function to display the landing page
def show_landing_page():
    st.markdown("<h1 style='margin-top: 20%;'>A.N.N.A</h1>", unsafe_allow_html=True)
    st.markdown("<p>AIA<br>Norms<br>Navigation<br>Assistant</p>", unsafe_allow_html=True)  # Smaller text with custom font below the main heading
    
    # Add a next question button at the bottom-right of the page
    if st.button("Start", type="primary"):
        st.switch_page("pages/1.intro.py")
    
# Check if the user is on the landing page and render the content
if 'page' not in st.session_state:
    st.session_state.page = 'landing'
    
if st.session_state.page == 'landing':
    show_landing_page()

# Apply custom CSS for layout and buttons
st.markdown(
"""
<style>
    /* Hide the Streamlit default hamburger menu (sidebar expander) */
    [data-testid="collapsedControl"] {
        display: none;
    }
    /* Style for the next question button */
    button[kind="primary"] {
        background-color: white;
        color: white !important;
        width: 200px;
        height: 50px;
        position: fixed;
        bottom: 30px;
        right: 30px;
        border-radius: 5px;
        font-family: sans-serif !important;  /* Use the system default font */
        font-size: 18px;
    }
    button[kind="primary"]:hover {
        background-color: #333 !important;
    }
    .spacer {
        margin-top: 200px;
    }
    .big-input {
        font-size: 18px !important;
        height: 100px !important;
        width: 100% !important;
    }
    /* Adjust the main container to have full width */
    .main .block-container {
        max-width: 90%;
        padding-left: 5%;
        padding-right: 5%;
    }
    .prompt-box {
        background-color: #f0f0f0;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
</style>
""",
    unsafe_allow_html=True
)
