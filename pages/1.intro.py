import streamlit as st
import utils

def render_intro():
    #utils.add_bg_from_base64("encoded_background.txt")

    # Introduction Section with professional styling
    st.markdown(
        """
        <h1 style='text-align: center; font-size: 36px;'>Welcome to ANNA - Your AI Act Compliance Chancellor</h1>
        """, 
        unsafe_allow_html=True
    )
    st.write("""
        **ANNA** *(AIA Norms Navigation Assistant)* is here to guide you through ensuring your AI system complies with the European Union's 
        Artificial Intelligence Act (AIA). Let’s simplify the process and keep you on the right track with regulatory requirements.
    """)

    st.markdown("---")

    st.markdown(
        """
        <h2 style='text-align: center;'>What is the AI Act? (or Regulation (EU) 2024/1689)</h2>
        """, 
        unsafe_allow_html=True
    )
    st.write("""
        The **AI Act** (AIA) is a set of regulations created by the European Union to ensure that AI technologies are **safe**, **transparent**, 
        and respect **fundamental rights**. It classifies AI systems based on risk levels and enforces strict regulations on those presenting 
        high risks to European citizens' rights.
        
        If you’re a provider of an AI system in the EU, you’ll want to make sure your systems meet these compliance standards.
    """)

    st.markdown("---")

    st.markdown(
        """
        <h2 style='text-align: center;'>How Can ANNA Help?</h2>
        """, 
        unsafe_allow_html=True
    )
    st.write("""
        Are you a company, startup, or individual providing an AI system within the European Union? **ANNA** is here to:
        - **Assess risks** your AI system may present.
        - **Identify obligations** your system must comply with under the AIA.
        - **Highlight penalties** for non-compliance.

        Save time and ensure your system is ready for the EU market by navigating AIA requirements with ease. With just a few simple questions, 
        ANNA will provide you with a clear overview of your compliance status.
    """)

    st.markdown("---")

    # Add disclaimer
    st.info("""
        **DISCLAIMER**: The AI Act represents only a portion of the rules that apply to stakeholders in the AI value chain. 
        Compliance with the AI Act does not automatically ensure compliance with other applicable Union laws, such as data protection, 
        consumer protection, or product safety regulations. For full legal assurance, consult a qualified legal advisor.
    """)

    # Add CSS for Next Page button styling
    st.markdown(
    """
    <style>
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
        font-family: sans-serif !important;  /* Use the system default font */
        font-size: 18px;
    }
    button[kind="primary"]:hover {
        background-color: #333 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )

    # Add the "Next Page" button to navigate to the questionnaire
    if st.button("Proceed", type="primary"):
        st.switch_page("pages/A.py") 

render_intro()
