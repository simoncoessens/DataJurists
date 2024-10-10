from question_template import render_question_page

render_question_page(
    question="""
    Is your AI system possibly excluded from the AI Act because it’s for military or scientific research use?
    """,
    example=(
        """
**Context**

For national security purposes and to protect innovation, the AI Act excludes from its scope systems used for certain purposes. For example, AI systems developed or used for military, defense, or national security purposes may be excluded, as well as AI systems developed solely for scientific research under specific conditions.

Want to dive deeper? Chat with ANNA for more details!
        """
    ),
    article_ids=[
        "article_002.003", "article_002.004", "article_002.006", "article_002.008","article_002.010","article_002.012", "recital_rct_25", "recital_rct_24"
    ],
    next_page="pages/E.py",
    chatbot_context="""
    You are Anna, the AI assistant helping users navigate the questionnaire on compliance with the AI Act. Introduce yourself as Anna when the conversation starts. Your role is to assist users in answering the **Main Question**: {question}, using relevant information from the **AI Act Articles**: {articles}.

    When users ask additional questions, provide clear, informative answers that stay focused on guiding them through the compliance process. Always cite relevant articles from the AI Act (in a readable format, not as internal codes) to support your answers. Your goal is to help users accurately complete the questionnaire by providing concise and relevant information.
    """,
    question_id=4
)
