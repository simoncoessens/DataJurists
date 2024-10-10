import os
import streamlit as st
from risk_evaluator import assess_risk
from PIL import Image
from pinecone import Pinecone

# Get Pinecone API key from secrets
pinecone_api_key = st.secrets["pinecone"]["api_key"]

# Initialize Pinecone
pc = Pinecone(api_key=pinecone_api_key)
index = pc.Index("aiact")

# Set Streamlit page configuration
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

# Define the mapping of risk categories to image filenames
risk_category_images = {
    "Prohibited Risk": "img/prohibited_risk.png",
    "High Risk": "img/high_risk.png",
    "Transparency Risk": "img/transparency_risk.png",
    "Minimal Risk": "img/minimal_risk.png"
}

def fetch_articles(article_ids):
    all_fetched_texts = []

    for article_id in article_ids:
        # Try to fetch the article normally
        result = index.fetch(ids=[article_id])

        if article_id in result['vectors']:
            # Article found
            all_fetched_texts.append(f"{article_id}:\n{result['vectors'][article_id]['metadata']['text']}")
        else:
            # Article not found, try to fetch subsections
            subsection_ids = [f"{article_id}.{i:03d}" for i in range(1, 100)]  # Generates 001, 002, ..., 099
            result = index.fetch(ids=subsection_ids)

            # Keep track of whether any subsections were found
            subsections_found = False

            # Process fetched subsections
            for subsection_id in subsection_ids:
                if subsection_id in result['vectors']:
                    subsections_found = True
                    all_fetched_texts.append(f"{subsection_id}:\n{result['vectors'][subsection_id]['metadata']['text']}")

            if not subsections_found:
                # No subsections found, print a message to the terminal
                print(f"No article found for ID: {article_id}")

    return "\n\n".join(all_fetched_texts)

# Check if there are any answers to use for the risk assessment
if not user_answers:
    st.write("No answers provided yet. Please answer the previous questions to perform the risk assessment.")
else:
    # Format the answers into a context string to use for the risk assessment
    formatted_answers = "\n".join([f"{question_id}: {answer}" for question_id, answer in user_answers.items()])

    # Detailed context for the risk assessment
    context = fetch_articles(["article_005", "article_006", "article_050", "article_095"])

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
    st.write(f"**Obligations or Recommendations:**")
    for obligation in risk_assessment.obligations_or_recommendations:
        st.write(f"- {obligation}")

    # Get the corresponding image filename based on the risk category
    risk_category = risk_assessment.risk_category.strip()
    image_filename = risk_category_images.get(risk_category, 'default_image.png')  # Use a default image if not found

    # Load the image based on the risk category
    image_path = os.path.join(image_filename)
    if os.path.exists(image_path):
        image = Image.open(image_path)
    else:
        st.write(f"Image not found for risk category: {risk_category}")
        image = None

    # Add a spacer to push the content to the top (optional)
    st.write("")

    # Create a placeholder at the bottom
    placeholder = st.empty()

    # Create three columns with the middle one wider inside the placeholder
    with placeholder.container():
        empty_col1, image_col, empty_col2 = st.columns([1, 2, 1])

        # Display the image in the middle column
        with image_col:
            if image:
                st.image(image, use_column_width=True)
            else:
                st.write("No image to display.")

# Render the Next Page button
render_next_question_button("pages/summary.py")
