import os
import streamlit as st
from pinecone import Pinecone
from evaluator import classify_and_suggest  # Your existing evaluator
from agent_with_memory import AgentWithMemory
import time

# Fetch the OpenAI and Pinecone API keys from Streamlit secrets
openai_api_key = st.secrets["openai"]["api_key"]
pinecone_api_key = st.secrets["pinecone"]["api_key"]

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = openai_api_key

# Initialize Pinecone connection
pc = Pinecone(api_key=pinecone_api_key)
index = pc.Index("aiact")

def fetch_articles(article_ids):
    all_fetched_texts = []

    for article_id in article_ids:
        # If an article ID does not specify a section (like "article_5"), fetch all subsections (e.g., "article_5_1", "article_5_2", ...)
        if article_id.count('_') == 1:  # If it contains only one underscore (like "article_5")
            # Construct all possible subsection IDs (this assumes a predefined range of subsections, e.g., 1 to 10)
            subsection_ids = [f"{article_id}_{i}" for i in range(1, 11)]  # Adjust the range as needed
            result = index.fetch(ids=subsection_ids)
            
            # Add the fetched subsections to the result
            for subsection_id in subsection_ids:
                if subsection_id in result['vectors']:
                    all_fetched_texts.append(f"{subsection_id}:\n{result['vectors'][subsection_id]['metadata']['text']}")
                else:
                    all_fetched_texts.append(f"No article found for ID: {subsection_id}")
        else:
            # For specific IDs (like "article_5_1"), fetch normally
            result = index.fetch(ids=[article_id])
            if article_id in result['vectors']:
                all_fetched_texts.append(f"{article_id}:\n{result['vectors'][article_id]['metadata']['text']}")
            else:
                all_fetched_texts.append(f"No article found for ID: {article_id}")

    return "\n\n".join(all_fetched_texts)



# Function to render the next question button
def render_next_question_button(next_page):
    # Add a next question button at the bottom-right of the page
    if st.button("Next Question", type="primary"):
        st.switch_page(next_page)

# Main function to render the question page
def render_question_page(question, example, article_ids, next_page, chatbot_context, question_id):
    if 'answers' not in st.session_state:
        st.session_state['answers'] = {}

    # Fetch articles from Pinecone based on the provided article IDs
    articles = fetch_articles(article_ids)

    # Format the initial context based on the current question and articles
    context = chatbot_context.format(question=question, articles=articles)

    # Add previous answers to the context
    previous_answers = "\n\n".join([f"Q: {q}\nA: {a}" for q, a in st.session_state['answers'].items()])
    
    # Combine previous answers with the current context
    if previous_answers:
        context += f"\n\nPrevious Questions and Answers:\n{previous_answers}"

    # Initialize agent and messages in session state if they don't exist
    st.session_state.agent = AgentWithMemory(context=context, model="gpt-3.5-turbo")
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
            if user_input:
                st.session_state['answers'][question_id] = user_input

                result = classify_and_suggest(question, user_input)

                classification = result.response_quality
                suggestions = result.suggestions

                st.markdown(f"<p style='color:{'green' if classification == 'Good' else 'orange' if classification == 'Good Enough' else 'red'}'><b>Classification: {classification}</b></p>", unsafe_allow_html=True)

                # Display suggestions
                if suggestions:
                    st.markdown("<h4>Suggestions for Improvement:</h4>", unsafe_allow_html=True)
                    for suggestion in suggestions:
                        st.write(f"- {suggestion}")

    # Right side for examples and chatbot
    with right_col:
        with st.container():
            st.markdown("<h4>Example Explanation</h4>", unsafe_allow_html=True)
            st.write(example)

        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

        with st.container():
            st.markdown("<h4>Chatbot Assistant</h4>", unsafe_allow_html=True)

            prompt = st.chat_input("Ask a question about the main questionnaire question...")

            chat_placeholder = st.container()

            if prompt:
                st.session_state.messages.append({"role": "user", "content": prompt})

                response = st.session_state.agent.run(prompt)
                chatbot_response = response['output']

                st.session_state.messages.append({"role": "assistant", "content": chatbot_response})

            with chat_placeholder:
                for message in reversed(st.session_state.messages):
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])

    # Render the Next Question button
    render_next_question_button(next_page)
