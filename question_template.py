import os
import streamlit as st
from pinecone import Pinecone
from evaluator import classify_and_suggest 
from agent_with_memory import AgentWithMemory
import time
import utils

openai_api_key = st.secrets["openai"]["api_key"]
pinecone_api_key = st.secrets["pinecone"]["api_key"]

os.environ["OPENAI_API_KEY"] = openai_api_key

pc = Pinecone(api_key=pinecone_api_key)
index = pc.Index("aiact")

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

# Function to render the next question button
def render_next_question_button(next_page):
    # Add a next question button at the bottom-right of the page
    if st.button("Next Question", type="primary"):
        st.switch_page(next_page)

# Main function to render the question page
def render_question_page(question, example, article_ids, next_page, chatbot_context, question_id):

    if 'questions' not in st.session_state:
        st.session_state['questions'] = {}

    if 'answers' not in st.session_state:
        st.session_state['answers'] = {}

    # Fetch articles from Pinecone based on the provided article IDs
    articles = fetch_articles(article_ids)

    # Format the initial context based on the current question and articles
    context = chatbot_context.format(question=question, articles=articles)

    # Add previous questions and answers to the context
    previous_qas = ""
    if 'questions' in st.session_state and 'answers' in st.session_state:
        previous_qas = "\n\n".join(
            [f"**Question {i + 1}: {st.session_state['questions'].get(qid, 'Unknown Question')}**\n**Your Answer:** {a}" 
            for i, (qid, a) in enumerate(st.session_state['answers'].items())]
        )

    # Combine previous Q&As with the current context
    if previous_qas:
        context += f"\n\nPrevious Questions and Answers by the user from the questionnaire:\n{previous_qas}"

    # Initialize agent if it doesn't exist
    if 'agent' not in st.session_state:
        print("initializing new agent")
        st.session_state.agent = AgentWithMemory(context=context, model="gpt-4o")

    # Initialize messages if they don't exist
    if 'messages' not in st.session_state:
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
            background-color: white;
            color: black;
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
        .prompt-box {
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

    # Layout split with adjusted gap
    left_col, right_col = st.columns([1, 1], gap="large")

    # Left side for the question, user input, and chatbot
    with left_col:
        # Render the question
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

        # Chatbot below the question
        st.markdown("<h4>Talk to Anna</h4>", unsafe_allow_html=True)

        prompt = st.chat_input("Ask a question about the main questionnaire question...")

        if prompt:
            # Append user's message to session state
            st.session_state.messages.append({"role": "user", "content": prompt})

            # Get response from the agent
            response = st.session_state.agent.run(prompt)
            chatbot_response = response['output']

            # Append agent's response to session state
            st.session_state.messages.append({"role": "assistant", "content": chatbot_response})

        # Display chat history
        chat_placeholder = st.container()
        with chat_placeholder:
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

        # Add sample prompts section
        st.markdown("<h4>Try these sample prompts:</h4>", unsafe_allow_html=True)
        st.markdown("""
            <div class="prompt-box">
                <b>Prompt 1:</b> What is the difference between an AI system and an GPAI?
            </div>
            <div class="prompt-box">
                <b>Prompt 2:</b> How do I find what I classify as?
            </div>
        """, unsafe_allow_html=True)

    # Right side for examples
    with right_col:
        st.markdown("<h4>Context</h4>", unsafe_allow_html=True)
        st.write(example)


    # Render the Next Question button
    render_next_question_button(next_page)
