from question_template import render_question_page

render_question_page(
    question="""
    Is your AI system designed to interact directly with people, or does it generate synthetic audio, images, videos, or text content?
    """,
    example=(
        """
Some AI systems, regardless of whether they are classified as high-risk, may still present transparency issues that need to be addressed. For example, if your AI system generates synthetic videos or text content, you may be required to ensure that the outputs are clearly marked as artificially generated. Similarly, if your system interacts directly with people, it may need to inform users that they are interacting with an AI, unless this is obvious.

Transparency measures can be critical for building trust and compliance. If you're unsure about your system's transparency requirements, ANNA can help guide you through the necessary steps to address them.
        """
    ),
    article_ids=[
        "article_050",
        "recital_rct_116"
    ],
    next_page="pages/risk_placement.py",
    chatbot_context="""
    You are Anna, the AI assistant helping users navigate the questionnaire on compliance with the AI Act. Introduce yourself as Anna when the conversation starts. Your role is to assist users in answering the **Main Question**: {question}, using relevant information from the **AI Act Articles**: {articles}.

    When users ask additional questions, provide clear, informative answers that stay focused on guiding them through the compliance process. Always cite relevant articles from the AI Act (in a readable format, not as internal codes) to support your answers. Your goal is to help users accurately complete the questionnaire by providing concise and relevant information.
    """,
    question_id=10
)
