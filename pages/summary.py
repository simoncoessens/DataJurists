import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

# Set the page configuration to wide layout and collapse the sidebar
st.set_page_config(page_title="AI Act Viewer", layout="wide", initial_sidebar_state="collapsed")

# Hide the sidebar expander button and style the buttons
st.markdown(
    """
    <style>
        [data-testid="collapsedControl"] {
            display: none;
        }
        button[kind="primary"] {
            background-color: black;
            color: white;
            width: 200px;
            height: 50px;
            display: block;
            margin: 10px auto; /* Center the button */
        }
        .centered-content {
            text-align: center;
        }
        .stMarkdown h1 {
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state for annotation scrolling and answers
if 'annotation_to_scroll' not in st.session_state:
    st.session_state['annotation_to_scroll'] = None
if 'answers' not in st.session_state:
    st.session_state['answers'] = {}

# Define annotations
annotations = [
    {"page": 11, "rect": [50, 700, 550, 720], "type": "highlight", "color": "yellow"},
    {"page": 19, "rect": [50, 600, 550, 620], "type": "highlight", "color": "yellow"},
    {"page": 24, "rect": [50, 500, 550, 520], "type": "highlight", "color": "yellow"},
]

# Map articles to annotation indices
article_to_annotation_index = {
    "Article 5": 1, 
    "Article 10": 2,
    "Article 15": 3,
}

# Create two columns for layout with improved centering
col1, col2 = st.columns([1, 1])  # Adjusted column widths for better balance

# Left column for summary of answers
with col1:
    st.markdown("<h1 class='centered-content'>Summary of Your Answers</h1>", unsafe_allow_html=True)
    
    # Display saved answers
    if 'answers' in st.session_state and st.session_state['answers']:
        for question_id, answer in st.session_state['answers'].items():
            st.write(f"**{question_id}:** {answer}")
    else:
        st.write("No answers submitted yet.")
    
    # Buttons for navigating to specific articles in the PDF
    st.markdown("<h1 class='centered-content'>AI Act Explanation</h1>", unsafe_allow_html=True)
    st.write("""
        The AI Act includes several important articles that apply to you:
        - **Prohibited AI Practices**: Refer to [Article 5](#) for details.
        - **Data Governance**: See [Article 10](#) for data requirements.
        - **Transparency Obligations**: Check [Article 15](#) for transparency rules.
    """, unsafe_allow_html=True)

    # Centered buttons for navigation
    if st.button("Go to Article 5", type="primary"):
        st.session_state['annotation_to_scroll'] = article_to_annotation_index["Article 5"]
    if st.button("Go to Article 10", type="primary"):
        st.session_state['annotation_to_scroll'] = article_to_annotation_index["Article 10"]
    if st.button("Go to Article 15", type="primary"):
        st.session_state['annotation_to_scroll'] = article_to_annotation_index["Article 15"]

# Right column for the AI Act PDF viewer
with col2:
    st.markdown("<h1 class='centered-content'>AI Act PDF Viewer</h1>", unsafe_allow_html=True)
    
    # Display the PDF viewer with annotations and navigation
    pdf_viewer(
        "AIA.pdf",  # Replace with the actual path or URL to your PDF
        annotations=annotations,
        scroll_to_annotation=st.session_state['annotation_to_scroll'],
        width=700,  # Adjust width for better centering
        height=1000  # Adjust height as needed
    )
