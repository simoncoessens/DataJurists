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
    articles = """
Article 50:
1. Providers must ensure that AI systems designed to interact directly with natural persons are developed in a way that ensures those persons are informed they are interacting with an AI system unless it is obvious from the context. This does not apply to AI systems used for detecting, preventing, or prosecuting criminal offences, unless available for the public to report crimes.

2. Providers of AI systems that generate synthetic audio, image, video, or text content must ensure that the content is marked in a machine-readable format to make it detectable as artificially generated. These systems must be robust and reliable, considering technical standards, costs, and limitations of various types of content. Exemptions apply when systems assist in standard editing without significantly altering the input or when authorized for criminal offence detection or prosecution.
    """,
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
