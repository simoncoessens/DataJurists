import os
import streamlit as st
from evaluator import classify_and_suggest  # Your existing evaluator
from agent_with_memory import AgentWithMemory
import time

# Fetch the OpenAI API key from Streamlit secrets
openai_api_key = st.secrets["openai"]["api_key"]

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = openai_api_key

# Set the page layout to wide
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Function to render the next question button
def render_next_question_button(next_page):
    # Add a next question button at the bottom-right of the page
    if st.button("Next Question", type="primary"):
        st.switch_page(next_page)

# Function to display a question page
def render_question_page(question, example, articles, next_page, chatbot_context, question_id):
    if 'answers' not in st.session_state:
        st.session_state['answers'] = {}

    
    # Initialize chat history and agent in session state
    context = chatbot_context.format(question=question, articles=articles)

    # Initialize agent and messages in session state if they don't exist
    if "agent" not in st.session_state:
        st.session_state.agent = AgentWithMemory(context=context)

    if "messages" not in st.session_state:
        st.session_state.messages = []

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
    </style>
    """,
    unsafe_allow_html=True,
)

    # Layout split with adjusted gap
    left_col, right_col = st.columns([1, 1], gap="large")

    # Left side for the question and user input
    with left_col:
        st.markdown(f"<h2>{question}</h2>", unsafe_allow_html=True)
        user_input = st.text_area("Answer here:", placeholder="Type your answer", key="big_input")

        if st.button("Submit Answer"):
            
            # Classify and suggest improvement
            if user_input:
                # Save the answer in session state
                st.session_state['answers'][question_id] = user_input

                result = classify_and_suggest(question, user_input)

                classification = result.response_quality
                suggestions = result.suggestions

                if classification == "Good":
                    st.markdown(f"<p style='color:green'><b>Classification: {classification}</b></p>", unsafe_allow_html=True)
                elif classification == "Good Enough":
                    st.markdown(f"<p style='color:orange'><b>Classification: {classification}</b></p>", unsafe_allow_html=True)
                elif classification == "Vague":
                    st.markdown(f"<p style='color:yellow'><b>Classification: {classification}</b></p>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<p style='color:red'><b>Classification: {classification}</b></p>", unsafe_allow_html=True)

                # Display suggestions
                if suggestions:
                    st.markdown("<h4>Suggestions for Improvement:</h4>", unsafe_allow_html=True)
                    for suggestion in suggestions:
                        st.write(f"- {suggestion}")

    # Right side for examples and chatbot
    # Right side for examples and chatbot
    with right_col:
        with st.container():
            st.markdown("<h4>Example Explanation</h4>", unsafe_allow_html=True)
            st.write(example)

        # Add space between the two containers
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

        with st.container():
            st.markdown("<h4>Chatbot Assistant</h4>", unsafe_allow_html=True)

            # Input form for chatbot
            prompt = st.chat_input("Ask a question about the main questionnaire question...")

            # Create a container for chat messages
            chat_placeholder = st.container()

            if prompt:
                # Append user message to chat history
                st.session_state.messages.append({"role": "user", "content": prompt})

                # Get chatbot response from the agent
                response = st.session_state.agent.run(prompt)
                chatbot_response = response['output']

                # Append assistant message to chat history
                st.session_state.messages.append({"role": "assistant", "content": chatbot_response})

            # Display chat messages from history in reverse order
            with chat_placeholder:
                for message in reversed(st.session_state.messages):
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])


    # Render the Next Question button
    render_next_question_button(next_page)
