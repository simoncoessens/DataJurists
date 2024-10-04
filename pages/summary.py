import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from agent_with_memory import AgentWithMemory

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
            margin: 10px auto;
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

# Initialize the agent with context
context = (
    "The European Union AI Act is a proposed regulation on artificial intelligence in the "
    "European Union. It aims to introduce a common regulatory and legal framework for artificial "
    "intelligence. The regulation classifies AI applications into risk categories and imposes "
    "different regulatory requirements depending on the category."
)
agent = AgentWithMemory(context=context, model="gpt-4o")

# Create two columns for layout with improved centering
col1, col2 = st.columns([1, 1])

# Left column for summary of answers and obligations
with col1:
    st.markdown("<h1 class='centered-content'>Summary of Your Answers</h1>", unsafe_allow_html=True)
    
    # Display saved answers
    user_answers = st.session_state.get('answers', {})
    if user_answers:
        for question_id, answer in user_answers.items():
            st.write(f"**{question_id}:** {answer}")
    else:
        st.write("No answers submitted yet.")
    
    # Format the answers into a prompt
    formatted_answers = "\n".join([f"{question_id}: {answer}" for question_id, answer in user_answers.items()])
    prompt = (
        "Based on the following answers provided by the user, generate a summary of the obligations "
        "that apply to them under the AI Act:\n\n" + formatted_answers
    )
    
    # Generate and display the summary of obligations
    if st.button("Generate Summary of Obligations"):
        with st.spinner("Generating summary..."):
            response = agent.run(prompt)
            summary = response['output']
            st.markdown("### Summary of Obligations")
            st.write(summary)
    

# Right column for the AI Act PDF viewer
with col2:
    st.markdown("<h1 class='centered-content'>AI Act PDF Viewer</h1>", unsafe_allow_html=True)
    
    # Display the PDF viewer with annotations and navigation
    pdf_viewer(
        "AIA.pdf",
        annotations=annotations,
        scroll_to_annotation=st.session_state['annotation_to_scroll'],
        width=700,
        height=1000
    )
