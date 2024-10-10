from question_template import render_question_page

render_question_page(
    question=(
        "Does your AI system pose a significant risk of harm to the health, safety, or fundamental rights of any person? "
        "Based on your previous responses, the chatbot will assist you in determining whether your AI system might be considered high-risk under Article 6."
        "\n\nIf you are unsure, you can ask the chatbot for more information on specific conditions that define significant risks."
    ),
    example=(
        "For example, if your AI system is intended to perform profiling of natural persons or if it influences decision-making outcomes, "
        "it may pose a significant risk. The chatbot can help you explore whether your system meets these or other high-risk conditions."
    ),
    article_ids=[
        "article_006",
        "recital_rct_48", "recital_rct_53"
    ],
    next_page="pages/question10.py",
    chatbot_context="""
    You are an Anna the AI assistant whose primary task is to help users answer the main question in the questionnaire with relation to the AI act. At introduction you say your name.
    Users may also ask additional questions related to the main question, and your role is to assist them by providing clear and accurate answers.

    Your main responsibilities include:

    - Assisting users in answering the **Main Question**: {question}
    - Referencing the **Relevant Articles** (from the AI Act): {articles}

    Ensure that your responses remain focused on helping users address the main question and always reference the articles you used (in bold and write them in readable text not as the internal representation) to give the information (but only use the **Relevant Articles** given above). Provide informative, easy-to-understand answers to any other questions they may have, 
    using the articles and examples provided to support your responses. The goal is to guide users in completing the questionnaire effectively.
    """,
    question_id=9
)
