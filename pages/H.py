from question_template import render_question_page

render_question_page(
    question="""
    Does your AI system pose a significant risk of harm to the health, safety, or fundamental rights?
    """,
    example=(
        """
To avoid overburdening, the AI Act narrows the scope of what qualifies as a high-risk AI system when it doesn’t pose a significant risk to health, safety, or fundamental rights.

For example, if your AI system is intended to perform profiling of natural persons or influences decision-making outcomes, it may pose a significant risk. However, ANNA can guide you in determining if your AI system falls under this exception, which could reduce the regulatory burden on you.
        """
    ),
    article_ids=[
        "article_006",
        "recital_rct_48", "recital_rct_53"
    ],
    next_page="pages/I.py",
    chatbot_context="""
    You are Anna, the AI assistant helping users navigate the questionnaire on compliance with the AI Act. Introduce yourself as Anna when the conversation starts. Your role is to assist users in answering the **Main Question**: {question}, using relevant information from the **AI Act Articles**: {articles}.

    When users ask additional questions, provide clear, informative answers that stay focused on guiding them through the compliance process. Always cite relevant articles from the AI Act (in a readable format, not as internal codes) to support your answers. Your goal is to help users accurately complete the questionnaire by providing concise and relevant information.
    If you are unsure if the user's system poses significant risk to health, safety or fundamental rights suggest him to comply with the most stringent requirements. For example to comply with high risk obligations.
    """,
    question_id=9
)
