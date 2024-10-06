from question_template import render_question_page

render_question_page(
    question=(
        "Geographical Scope:\n\n"
        "Irrespective of whether you are established or located within the Union or in a third country, are you placing AI systems "
        "on the market or putting them into service in the Union?\n\n"
        "Do you have your place of establishment, or are you located in a third country, but the output produced by the AI system is used in the Union?"
    ),
    example=(
        "For example, if you are a provider located in a third country but selling AI systems in the EU, or if your AI system produces "
        "an output that is used within the EU, this regulation will apply to you."
    ),
    article_ids=[
        "article_2_1", "article_2_1",
        "recital_rct_21", "recital_rct_22", "recital_rct_82"
    ],
    next_page="pages/question5.py",
    chatbot_context="""
    You are an AI assistant whose primary task is to help users answer the main question in the questionnaire. 
    Users may also ask additional questions related to the main question, and your role is to assist them by providing clear and accurate answers.

    Your main responsibilities include:

    - Assisting users in answering the **Main Question**: {question}
    - Referencing the **Relevant Articles** (from the AI Act): {articles}

    Ensure that your responses remain focused on helping users address the main question. Provide informative, easy-to-understand answers to any other questions they may have, 
    using the articles and examples provided to support your responses. The goal is to guide users in completing the questionnaire effectively.
    """,
    question_id=4
)
