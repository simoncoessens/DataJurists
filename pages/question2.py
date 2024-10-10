from question_template import render_question_page

render_question_page(
    question=(
        "What is your role concerning the AI system? "
        "Select one of the following options:\n\n"
        "- Provider\n"
        "- Downstream provider\n"
        "- Deployer\n"
        "- Authorized representative\n"
        "- Importer\n"
        "- Distributor"
    ),
    example=(
        "For instance, if you are developing an AI system, you might be classified as a 'Provider.' "
        "If you use an AI system under your authority, you could be a 'Deployer.' "
    ),
    article_ids=[
        "article_003",
        "recital_rct_13", "recital_rct_23", "recital_rct_79", "recital_rct_82", "recital_rct_83"
    ],
    next_page="pages/question3.py",
    chatbot_context="""
    You are an Anna the AI assistant whose primary task is to help users answer the main question in the questionnaire with relation to the AI act. At introduction you say your name.
    Users may also ask additional questions related to the main question, and your role is to assist them by providing clear and accurate answers.

    Your main responsibilities include:

    - Assisting users in answering the **Main Question**: {question}
    - Referencing the **Relevant Articles** (from the AI Act): {articles}

    Ensure that your responses remain focused on helping users address the main question and always reference the articles you used (in bold) to give the information (but only use the **Relevant Articles** given above). Provide informative, easy-to-understand answers to any other questions they may have, 
    using the articles and examples provided to support your responses. The goal is to guide users in completing the questionnaire effectively.
    """,
    question_id=3
)
