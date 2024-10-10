import os
import streamlit as st
from risk_evaluator import assess_risk  # Import the assess_risk function from your script
from PIL import Image  # Import PIL to handle images

# Set the page layout to wide
st.set_page_config(page_title="ANNA", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for layout and button styling
st.markdown(
    """
    <style>
        /* Hide the Streamlit default hamburger menu (sidebar expander) */
        [data-testid="collapsedControl"] {
            display: none;
        }
        /* Style for the next question button */
        button[kind="primary"] {
            background-color: black;
            color: white;
            width: 200px;
            height: 50px;
            position: fixed;
            bottom: 30px;
            right: 30px;
            border-radius: 5px;
        }
        button[kind="primary"]:hover {
            background-color: #333;
        }
        .spacer {
            margin-top: 200px;
        }
        /* Adjust the main container to have full width */
        .main .block-container{
            max-width: 90%;
            padding-left: 5%;
            padding-right: 5%;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to render the next question button
def render_next_question_button(next_page):
    # Add a next question button at the bottom-right of the page
    if st.button("Next Question", type="primary"):
        st.switch_page(next_page)

# Get the user's previous answers from session state
user_answers = st.session_state.get('answers', {})

# Check if there are any answers to use for the risk assessment
if not user_answers:
    st.write("No answers provided yet. Please answer the previous questions to perform the risk assessment.")
else:
    # Format the answers into a context string to use for the risk assessment
    formatted_answers = "\n".join([f"{question_id}: {answer}" for question_id, answer in user_answers.items()])

    # Detailed context for the risk assessment
    context = f"""
    High risk AI systems include:
    ... [Your existing context here] ...
    """

    # Automatically perform risk assessment when the page loads
    if 'risk_assessment' not in st.session_state:
        with st.spinner("Assessing risk..."):
            result = assess_risk(context, formatted_answers)
            
            # Store the results in session state for later use
            st.session_state['risk_assessment'] = result
    
    # Display the risk assessment results
    risk_assessment = st.session_state['risk_assessment']
    st.markdown("### Risk Assessment Result")
    st.write(f"**Risk Category**: {risk_assessment.risk_category}")
    st.write(f"**Explanation**: {risk_assessment.explanation}")

# **Add this code to include the centered image at the bottom**

# Load the image
image_path = os.path.join('risk_pyramid.png')
image = Image.open(image_path)

# Add a spacer to push the content to the top (optional)
st.write("")  # You can add more st.write("") if needed to adjust spacing

# Create a placeholder at the bottom
placeholder = st.empty()

# Create three columns with the middle one wider inside the placeholder
with placeholder.container():
    empty_col1, image_col, empty_col2 = st.columns([1, 2, 1])

    # Display the image in the middle column
    with image_col:
        st.image(image, use_column_width=True)

# Render the Next Page button
render_next_question_button("pages/summary.py")
