from question_template import render_question_page

render_question_page(
    question=(
        "What is the purpose or context in which the AI system is going to be used? "
        "Based on your previous responses, the chatbot will suggest which high-risk category your AI system might fall under according to Article 6."
        "\n\nHigh-risk categories include areas such as biometrics, critical infrastructure, education, employment, law enforcement, migration, or justice."
        "\n\nYou can also ask the chatbot for more detailed information on each of these categories if needed."
    ),
    example=(
        "For example, if your AI system is used for biometric identification or in the management of critical infrastructure, "
        "it may fall under high-risk categories as defined by the AI Act. The chatbot will suggest relevant categories based on your responses."
    ),
    article_ids=[
        "article_006",
        "recital_rct_52", "recital_rct_54", "recital_rct_56", "recital_rct_57", "recital_rct_59", 
        "recital_rct_60", "recital_rct_61", "recital_rct_62", "recital_rct_63"
    ],
    next_page="pages/question9.py",
    chatbot_context="""
    You are an Anna the AI assistant whose primary task is to help users answer the main question in the questionnaire with relation to the AI act. At introduction you say your name.
    Users may also ask additional questions related to the main question, and your role is to assist them by providing clear and accurate answers.

    Your main responsibilities include:

    - Assisting users in answering the **Main Question**: {question}
    - Referencing the **Relevant Articles** (from the AI Act): {articles}

    Ensure that your responses remain focused on helping users address the main question and always reference the articles you used (in bold) to give the information (but only use the **Relevant Articles** given above). Provide informative, easy-to-understand answers to any other questions they may have, 
    using the articles and examples provided to support your responses. The goal is to guide users in completing the questionnaire effectively.
    """,
    question_id=8
)
