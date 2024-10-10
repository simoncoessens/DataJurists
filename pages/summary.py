import os
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from agent_with_memory import AgentWithMemory
import utils

# Fetch the OpenAI API key from Streamlit secrets
openai_api_key = st.secrets["openai"]["api_key"]
os.environ["OPENAI_API_KEY"] = openai_api_key

# Set the page configuration to wide layout and collapse the sidebar
st.set_page_config(page_title="ANNA", layout="wide", initial_sidebar_state="collapsed")

# Apply custom CSS for layout and buttons
st.markdown(
    """
    <style>
        /* Hide the Streamlit default hamburger menu */
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
        .big-input {
            font-size: 18px !important;
            height: 100px !important;
            width: 100% !important;
        }
        /* Adjust the main container to have full width */
        .main .block-container{
            max-width: 90%;
            padding-left: 5%;
            padding-right: 5%;
        }
        /* Styling for the checklist container */
        /* Styling for headers */
        h1, h2 {
            color: #2F5496;
        }
        /* Styling for buttons */
        .stButton button {
            background-color: black;
            color: white;
            width: 100%;
            height: 45px;
            border-radius: 5px;
            font-size: 16px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state for agent and messages
if 'agent' not in st.session_state:
    # Initialize the agent with context
    context = (
        "The European Union AI Act is a proposed regulation on artificial intelligence in the "
        "European Union. It aims to introduce a common regulatory and legal framework for artificial "
        "intelligence. The regulation classifies AI applications into risk categories and imposes "
        "different regulatory requirements depending on the category."
    )
    st.session_state.agent = AgentWithMemory(context=context, model="gpt-4")
    st.session_state.messages = []

# Function to render the next question button (if needed)
def render_next_question_button(next_page):
    # Add a next question button at the bottom-right of the page
    if st.button("Next Question", type="primary"):
        st.write("Next question functionality is not implemented in this example.")

# Main function to render the page
def render_page():
    #utils.add_bg_from_base64()  # If you have a background image utility

    # Create layout with adjusted gap
    left_col, right_col = st.columns([1, 1], gap="large")

    # Left side for the checklist
    with left_col:
        st.markdown("<h2>Your Personalized AIA Checklist</h2>", unsafe_allow_html=True)
        st.markdown("<div class='checklist-container'>", unsafe_allow_html=True)

        # Checklist items
        checklist_items = [
            "Set up a risk management system to spot and reduce any foreseeable risks your AI system might create. (Article 9)",
            "Make sure your training data meets the quality standards required by the AIA. (Article 10)",
            "Prepare and keep technical documentation to show that you're following the AIA rules. (Article 11)",
            "Enable automatic logging in your system and keep these logs to ensure compliance. (Articles 12, 19)",
            "Ensure transparency in how your system operates, so other actors can better interpret the system output. (Article 13)",
            "Include tools for human oversight in your AI system’s design to allow a human to intervene if needed. (Article 14)",
            "Design for accuracy, robustness, and cybersecurity so your AI system performs reliably. (Article 15)",
            "Provide your contact details, including your name or trademark and your address, for easy contact.",
            "Affix the CE marking to your high-risk AI system. (Article 48)",
            "Implement a quality management system to make sure you’re following the AIA requirements. (Article 17)",
            "Undergo the proper conformity assessment procedure before releasing your system to the market. (Article 43)",
            "Create an EU declaration of conformity to confirm your system complies with the regulations. (Article 47)",
            "Register your high-risk AI system in the official EU database. (Articles 49, 71)",
            "After launching, be ready to fix issues and update the market surveillance authority if something goes wrong. (Article 20)",
            "Be able to prove compliance with the AIA if a national authority requests it.",
            "Ensure your system meets accessibility requirements.",
            "Train your staff to have the necessary AI literacy to operate and manage the system effectively (Article 4).",
            "Put in place a post-marketing monitoring system proportionate to the nature and risks of your AI system (Article 72)",
            "Report any serious incidents to the competent market surveillance authority (Article 73)",
        ]

        # Display the checklist using Streamlit checkboxes
        for idx, item_text in enumerate(checklist_items):
            st.checkbox(item_text, key=f"check_{idx}")

        st.markdown("</div>", unsafe_allow_html=True)

    # Right side for the chatbot
    with right_col:
        st.markdown("<h2>Chatbot Assistant</h2>", unsafe_allow_html=True)

        # Chatbot input
        prompt = st.chat_input("Ask a question about the AI Act...")

        if prompt:
            st.session_state.messages.append({"role": "user", "content": prompt})

            with st.spinner("Generating response..."):
                response = st.session_state.agent.run(prompt)
                chatbot_response = response['output']

            st.session_state.messages.append({"role": "assistant", "content": chatbot_response})

        # Display chat history
        if st.session_state.messages:
            for message in st.session_state.messages:
                if message["role"] == "user":
                    with st.chat_message("user"):
                        st.markdown(message["content"])
                else:
                    with st.chat_message("assistant"):
                        st.markdown(message["content"])

    # Spacer before the PDF viewer
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Center the PDF viewer at the bottom using columns
    st.markdown("<h2 style='text-align: center;'>AI Act PDF Viewer</h2>", unsafe_allow_html=True)
    # Create three columns with the middle one wider
    empty_col1, pdf_col, empty_col2 = st.columns([1, 2, 1])

    with pdf_col:
        pdf_viewer(
            "AIA.pdf",
            width=1000,
            height=1400
        )


# Call the main function to render the page
render_page()
