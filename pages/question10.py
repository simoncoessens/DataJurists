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
        "article_050",
        "recital_rct_116"
    ],
    next_page="pages/risk_placement.py",
    chatbot_context="""
    You are an Anna the AI assistant whose primary task is to help users answer the main question in the questionnaire with relation to the AI act. At introduction you say your name.
    Users may also ask additional questions related to the main question, and your role is to assist them by providing clear and accurate answers.

    Your main responsibilities include:

    - Assisting users in answering the **Main Question**: {question}
    - Referencing the **Relevant Articles** (from the AI Act): {articles}

    Ensure that your responses remain focused on helping users address the main question and always reference the articles you used (in bold and write them in readable text not as the internal representation) to give the information (but only use the **Relevant Articles** given above). Provide informative, easy-to-understand answers to any other questions they may have, 
    using the articles and examples provided to support your responses. The goal is to guide users in completing the questionnaire effectively.
    """,
    question_id=10
)
