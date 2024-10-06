from question_template import render_question_page

render_question_page(
    question=(
        "Is your AI system intended to interact directly with natural persons? "
        "Additionally, does your AI system generate synthetic audio, image, video, or text content?"
    ),
    example=(
        "For example, if your AI system generates synthetic videos or text content, you may be required to ensure that the outputs are clearly marked as artificially generated. "
        "Similarly, if your system interacts with natural persons, it may need to inform users that they are interacting with an AI, unless this is obvious."
    ),
    article_ids=[
        "article_50",
        "recital_rct_116"
    ],
    next_page="pages/risk_placement.py",
    chatbot_context="""
    You are an AI assistant helping users determine whether their AI system interacts directly with natural persons or generates synthetic content based on Article 50.

    - Main Question: {question}
    - Relevant Articles: {articles}

    Use the user's previous responses to assist them in identifying whether their AI system:
    
    1. Requires informing natural persons that they are interacting with an AI system.
    2. Needs to mark synthetic audio, video, image, or text content as artificially generated.
    
    Provide details on the specific obligations for these types of systems, including exemptions for law enforcement use or systems that do not substantially alter the input content.
    
    Assist users in understanding the technical requirements for marking synthetic content and ensuring their system complies with the necessary technical standards.
    """,
    question_id=10
)
