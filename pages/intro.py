import streamlit as st
import utils

def render_intro():
    st.title("Welcome to the AIA Compliance Checker")

    #utils.add_bg_from_base64("encoded_background.txt")

    # Introduction Section
    st.header("What the AIA is (Article 1)")
    st.write("""
        The Artificial Intelligence Act (AIA) is a regulatory framework proposed by the European Union 
        that aims to ensure AI systems are safe, transparent, and respect fundamental rights. 
        According to Article 1, the AIA establishes rules and obligations regarding AI systems 
        and their development, implementation, and use in various sectors.
    """)

    st.header("What Services We Offer")
    st.write("""
        We offer a comprehensive assessment tool to help organizations ensure their AI systems 
        are compliant with the AIA. Our service includes:
        - AI system analysis
        - AIA compliance evaluation
        - Detailed reporting and recommendations
    """)

    st.header("Why You Should Be Concerned and Use Our App")
    st.write("""
        With the increasing adoption of AI technologies, compliance with the AIA is crucial to 
        avoid penalties, ensure ethical AI usage, and maintain trust with consumers. Our tool 
        helps you navigate the complexity of the AIA, ensuring that your AI system meets all 
        regulatory requirements.
    """)

    # Add disclaimer
    st.warning("""
        **DISCLAIMER**: The AI Act represents only a portion of the rules that apply to the various 
        stakeholders in the AI value chain. It's important to remember that being compliant with the 
        AI Act does not mean you are automatically compliant with other existing Union laws. 
        Specifically, the AI Act complements regulations on data protection, consumer protection, 
        fundamental rights, employment and worker protection, and product safety. 

        Please keep in mind that while this compliance tool is designed with legal accuracy in mind, 
        it may still make errors. Always verify the information with a qualified (human) legal advisor 
        to ensure full compliance.
    """)

    # Add CSS for Next Page button styling
    st.markdown(
    """
    <style>
        /* Style for the next page button */
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
    </style>
    """,
    unsafe_allow_html=True,
)

    # Add the "Next Page" button to navigate to the questionnaire
    if st.button("Next Page", type="primary"):
        st.switch_page("pages/question1.py") 

render_intro()
