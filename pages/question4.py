from question_template import render_question_page

render_question_page(
    question=(
        "Are you under the geographical scope of the AIA?\n\n"
        "Please provide more information about the country where you are established and where your activities are based. "
        "Specifically, consider the following questions to help the Chatbot Assistant guide you through your obligations under the AI Act:\n\n"
        "- Are you placing AI systems on the market or putting them into service within the European Union (EU)?\n"
        "- Is your place of establishment or location outside the EU, but the AI system's output is used within the EU?"
    ),
    example=(
        "For example, if you are a provider located in a third country but selling AI systems in the EU, or if your AI system produces "
        "an output that is used within the EU, this regulation will apply to you."
    ),
    article_ids=[
        "article_002.001", "article_002.002",
        "recital_rct_21", "recital_rct_22", "recital_rct_82"
    ],
    next_page="pages/question5.py",
    chatbot_context="""
    You are Anna, an AI assistant whose primary task is to help users answer the main question in the questionnaire with relation to the AI Act. At the start, introduce yourself and your role.

    Your primary tasks include:

    - Assisting users in answering the **Main Question**: {question}
    - Referencing the **Relevant Articles** (from the AI Act): {articles}

    Focus on helping users determine whether their activities fall under the geographical scope of the AI Act, particularly if they are based outside the EU but may still be subject to the Act’s regulations. Use the provided relevant articles to give accurate, clear guidance based on their situation.
    """,
    question_id=4
)
