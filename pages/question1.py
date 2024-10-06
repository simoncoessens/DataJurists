from question_template import render_question_page

render_question_page(
    question="Describe the AI system you are developing. Include details about its functionality and whether it can be classified as a General Purpose AI (GPAI) model or an AI system.",
    example=(
        "For example, the system you are developing could be an AI-based chatbot for customer support, "
        "an autonomous decision-making algorithm, or a machine learning model designed to predict user behavior. "
        "Alternatively, if you are working on a General Purpose AI (GPAI) model, it might be intended for broad applications "
        "such as language processing or image recognition across multiple industries."
    ),
    article_ids=["article_3_1", "article_3_63", "recital_rct_12", "recital_rct_97", "recital_rct_100"],
    next_page="pages/question2.py",
    chatbot_context="""
    You are an AI assistant whose primary task is to help users answer the main question in the questionnaire. 
    Users may also ask additional questions related to the main question, and your role is to assist them by providing clear and accurate answers.

    Your main responsibilities include:

    - Assisting users in answering the **Main Question**: {question}
    - Referencing the **Relevant Articles** (from the AI Act): {articles}

    Ensure that your responses remain focused on helping users address the main question. Provide informative, easy-to-understand answers to any other questions they may have, 
    using the articles and examples provided to support your responses. The goal is to guide users in completing the questionnaire effectively.
    """,
    question_id=1
)
