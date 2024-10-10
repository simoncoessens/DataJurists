from question_template import render_question_page

render_question_page(
    question="""
    Are you under the geographical scope of the AIA?
    """,
    example=(
        """
Please provide more information to ANNA about where you are located and where your activities are based. Your answers will help determine whether your activities fall within the geographical scope of the AI Act, even if you're not physically established in the EU. This will ensure proper guidance on the obligations you may have.

For example, you may be excluded if your AI system is used exclusively for military purposes, or if it is deployed by a third-country public authority for international cooperation with the Union. Alternatively, if the AI system is part of research and development activities not yet placed on the market, you may also be exempt from the regulation.
        """
    ),
    article_ids=[
        "article_002.003", "article_002.004", "article_002.006", "article_002.008", "article_002.010", "article_002.012",
        "recital_rct_24", "recital_rct_25"
    ],
    next_page="pages/C.py",
    chatbot_context="""
    You are Anna, the AI assistant helping users navigate the questionnaire on compliance with the AI Act. Introduce yourself as Anna when the conversation starts. Your role is to assist users in answering the **Main Question**: {question}, using relevant information from the **AI Act Articles**: {articles}.

    When users ask additional questions, provide clear, informative answers that stay focused on guiding them through the compliance process. Always cite relevant articles from the AI Act (in a readable format, not as internal codes) to support your answers. Your goal is to help users accurately complete the questionnaire by providing concise and relevant information.
    """,
    question_id=2
)
