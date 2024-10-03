import streamlit as st

# Set page configuration to start with sidebar collapsed
st.set_page_config(page_title="Questionnaire App", layout="wide", initial_sidebar_state="collapsed")

# Hide the sidebar expander button and style buttons
st.markdown(
    """
    <style>
        [data-testid="collapsedControl"] {
            display: none;
        }
        button[kind="primary"] {
            background-color: black;
            color: white;
            width: 200px; /* Adjust the width as needed */
            height: 50px; /* Adjust the height as needed */
            display: block;
            margin: 0 auto; /* Center the button */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to display the landing page
def show_landing_page():
    st.markdown("<h1 style='text-align: center; margin-top: 20%;'>Navigating the AI Act</h1>", unsafe_allow_html=True)

    # Centered "Get Started" button
    if st.button("Get Started", type="primary"):
        st.switch_page("pages/question1.py")

# Check if the user is on the landing page and render the content
if 'page' not in st.session_state:
    st.session_state.page = 'landing'
    
if st.session_state.page == 'landing':
    show_landing_page()
