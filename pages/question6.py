from question_template import render_question_page

render_question_page(
    question=(
        "Prohibited AI Systems:\n\n"
        "Is your system one of the following:\n"
        "- AI system that deploys subliminal techniques?\n"
        "- Exploitative AI systems?\n"
        "- Social scoring AI systems?\n"
        "- Predictive policing AI systems?\n"
        "- Scraping AI systems?\n"
        "- Biometric categorization AI systems?\n"
        "- ‘Real-time’ remote biometric identification systems in publicly accessible spaces?"
    ),
    example=(
        "For example, if your AI system exploits vulnerabilities of specific groups, manipulates decision-making beyond "
        "conscious awareness, or conducts social scoring, it may fall under these prohibited categories."
    ),
    article_ids=[
        "article_5",
        "recital_rct_15", "recital_rct_16", "recital_rct_17", "recital_rct_18", "recital_rct_19", 
        "recital_rct_29", "recital_rct_30", "recital_rct_31", "recital_rct_32", "recital_rct_33", 
        "recital_rct_34", "recital_rct_36", "recital_rct_38", "recital_rct_39", "recital_rct_42", 
        "recital_rct_43", "recital_rct_44"
    ],
    next_page="pages/question7.py",
    chatbot_context="""
    You are an AI assistant whose primary task is to help users answer the main question in the questionnaire. 
    Users may also ask additional questions related to the main question, and your role is to assist them by providing clear and accurate answers.

    Your main responsibilities include:

    - Assisting users in answering the **Main Question**: {question}
    - Referencing the **Relevant Articles** (from the AI Act): {articles}

    Ensure that your responses remain focused on helping users address the main question. Provide informative, easy-to-understand answers to any other questions they may have, 
    using the articles and examples provided to support your responses. The goal is to guide users in completing the questionnaire effectively.
    """,
    question_id=6
)
