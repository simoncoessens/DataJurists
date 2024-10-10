from question_template import render_question_page

render_question_page(
    question="Are you under the geographical scope of the AIA?",
    example=(
        "For example, you may be excluded if your AI system is used exclusively for military purposes, "
        "or if it is deployed by a third-country public authority for international cooperation with the Union. "
        "Alternatively, if the AI system is part of research and development activities not yet placed on the market, "
        "you may also be exempt from the regulation."
    ),
    article_ids=[
        "article_002.003", "article_002.004", "article_002.006", "article_002.008", "article_002.010", "article_002.012",
        "recital_rct_24", "recital_rct_25"
    ],
    next_page="pages/question4.py",
    chatbot_context="""
    You are Anna, an AI assistant whose primary task is to help users answer the main question in the questionnaire with relation to the AI Act. At the start, introduce yourself and your role.

    Your primary tasks include:

    - Assisting users in answering the **Main Question**: {question}
    - Referencing the **Relevant Articles** (from the AI Act): {articles}

    Focus on helping users determine if their activities fall under the geographical scope of the AI Act. Use the provided relevant articles to give accurate, clear guidance, particularly when users are based outside the EU but may still be subject to the AI Act’s requirements.
    """,
    question_id=3
)
