from question_template import render_question_page

render_question_page(
    question=(
        "Downstream Modification:\n\n"
        "Will a downstream modification happen?\n\n"
        "This includes:\n"
        "- Putting another name or trademark on a high-risk AI system already placed on the market or put into service;\n"
        "- Making a substantial modification to a high-risk AI system that has already been placed on the market or put into service;\n"
        "- Modifying the intended purpose of an AI system, including a general-purpose AI system, which has not been classified as high-risk, "
        "but has already been placed on the market or put into service, in such a way that it becomes a high-risk AI system in accordance with Article 6."
    ),
    example=(
        "For example, if you rebrand an AI system already classified as high-risk, or modify an existing AI system in a way that it now meets the high-risk criteria, "
        "you may fall under the obligations of a provider according to the AI Act."
    ),
    article_ids=[
        "article_25",
        "recital_rct_84", "recital_rct_86"
    ],
    next_page="pages/question6.py",
    chatbot_context="""
    You are an AI assistant whose primary task is to help users answer the main question in the questionnaire. 
    Users may also ask additional questions related to the main question, and your role is to assist them by providing clear and accurate answers.

    Your main responsibilities include:

    - Assisting users in answering the **Main Question**: {question}
    - Referencing the **Relevant Articles** (from the AI Act): {articles}

    Ensure that your responses remain focused on helping users address the main question. Provide informative, easy-to-understand answers to any other questions they may have, 
    using the articles and examples provided to support your responses. The goal is to guide users in completing the questionnaire effectively.
    """,
    question_id=5
)
