from question_template import render_question_page

render_question_page(
    question="Does the Artificial Intelligence Act (AIA) apply to you, or are you excluded from its scope?",
    example=(
        "For example, you may be excluded if your AI system is used exclusively for military purposes, "
        "or if it is deployed by a third-country public authority for international cooperation with the Union. "
        "Alternatively, if the AI system is part of research and development activities not yet placed on the market, "
        "you may also be exempt from the regulation."
    ),
    article_ids=[
        "article_2_3", "article_2_4", "article_2_6", "article_2_8", "article_2_10", "article_2_12",
        "recital_rct_24", "recital_rct_25"
    ],
    next_page="pages/question4.py",
    chatbot_context="""
    You are an AI assistant whose primary task is to help users answer the main question in the questionnaire. 
    Users may also ask additional questions related to the main question, and your role is to assist them by providing clear and accurate answers.

    Your main responsibilities include:

    - Assisting users in answering the **Main Question**: {question}
    - Referencing the **Relevant Articles** (from the AI Act): {articles}

    Ensure that your responses remain focused on helping users address the main question. Provide informative, easy-to-understand answers to any other questions they may have, 
    using the articles and examples provided to support your responses. The goal is to guide users in completing the questionnaire effectively.
    """,
    question_id=3
)
