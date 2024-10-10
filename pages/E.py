from question_template import render_question_page

render_question_page(
    question="""
    Is any downstream modification happening with your AI system?
    """,
    example=(
        """
The AI Act recognizes changes in the AI value chain, which is why it considers modifications made by others to fairly distribute responsibilities. For example, if there's a major change, some of your obligations might be shared with the deployer.

For instance, if you rebrand an AI system already classified as high-risk, or modify an existing AI system in a way that it now meets the high-risk criteria, you may fall under the obligations of a provider according to the AI Act.

Ask ANNA to learn more about what counts as a "downstream modification"!
        """
    ),
    article_ids=[
        "article_025",
        "recital_rct_84", "recital_rct_86"
    ],
    next_page="pages/F.py",
    chatbot_context="""
    You are Anna, the AI assistant helping users navigate the questionnaire on compliance with the AI Act. Introduce yourself as Anna when the conversation starts. Your role is to assist users in answering the **Main Question**: {question}, using relevant information from the **AI Act Articles**: {articles}.

    When users ask additional questions, provide clear, informative answers that stay focused on guiding them through the compliance process. Always cite relevant articles from the AI Act (in a readable format, not as internal codes) to support your answers. Your goal is to help users accurately complete the questionnaire by providing concise and relevant information.
    """,
    question_id=5
)
