import os
import streamlit as st
from risk_evaluator import assess_risk  # Import the assess_risk function from your script

# Set the page layout to wide
st.set_page_config(page_title="AI System Risk Assessment", layout="wide", initial_sidebar_state="collapsed")

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
    if st.button("Next", type="primary"):
        st.session_state['next_page'] = next_page
        st.experimental_rerun()

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
    - Critical infrastructures (e.g., transport) that could put the life and health of citizens at risk.
    - Educational or vocational training systems that may determine access to education and professional courses (e.g., scoring of exams).
    - Safety components of products (e.g., AI applications in robot-assisted surgery).
    - Employment, management of workers, and access to self-employment (e.g., CV-sorting software for recruitment).
    - Essential private and public services (e.g., credit scoring that can deny loans).
    - Law enforcement systems that may interfere with fundamental rights (e.g., evaluation of evidence reliability).
    - Migration, asylum, and border control management systems (e.g., automated visa applications).
    - Administration of justice and democratic processes (e.g., AI solutions for court ruling searches).

    High-risk AI systems are subject to strict obligations, including:
    - Adequate risk assessment and mitigation systems.
    - High-quality datasets to minimize risks and discrimination.
    - Logging activities to ensure traceability of results.
    - Detailed documentation for system compliance assessment.
    - Clear and adequate information to the deployer.
    - Appropriate human oversight to minimize risks.
    - High levels of robustness, security, and accuracy.
    
    All remote biometric identification systems in public spaces for law enforcement are considered high-risk and subject to strict requirements.

    Limited risk AI systems include those with risks associated with transparency. These systems must inform users they are interacting with AI, particularly for systems like chatbots or AI-generated content (deep fakes). Such content must be labeled as AI-generated.

    Minimal or no risk AI systems include applications such as AI-enabled video games or spam filters.

    User's AI System Information:
    {formatted_answers}
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
    st.write(f"**Obligations or Recommendations**: {', '.join(risk_assessment.obligations_or_recommendations)}")

# Render the Next Page button
render_next_question_button("summary_page")
