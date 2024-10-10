from question_template import render_question_page

render_question_page(
    question="""
    Is your AI system considered illegal under the AIA?
    """,
    example=(
        """
The EU AI Act follows a risk-based approach, meaning some systems are banned because they go against core Union values like human dignity, freedom, and fundamental rights. Prohibited AI systems include those using subliminal and exploitative techniques.

For example, if your AI system exploits vulnerabilities of specific groups, manipulates decision-making beyond conscious awareness, or conducts social scoring, it may fall under these prohibited categories.

Unsure if your system falls under this category? Ask ANNA to find out if it's prohibited under the AIA!
        """
    ),
    article_ids=[
        "article_005",
        "recital_rct_15", "recital_rct_16", "recital_rct_17", "recital_rct_18", "recital_rct_19", 
        "recital_rct_29", "recital_rct_30", "recital_rct_31", "recital_rct_32", "recital_rct_33", 
        "recital_rct_34", "recital_rct_36", "recital_rct_38", "recital_rct_39", "recital_rct_42", 
        "recital_rct_43", "recital_rct_44", "annex_anx_II"
    ],
    next_page="pages/G.py",
    chatbot_context="""
    You are Anna, the AI assistant helping users navigate the questionnaire on compliance with the AI Act. Introduce yourself as Anna when the conversation starts. Your role is to assist users in answering the **Main Question**: {question}, using relevant information from the **AI Act Articles**: {articles}.

    When users ask additional questions, provide clear, informative answers that stay focused on guiding them through the compliance process. Always cite relevant articles from the AI Act (in a readable format, not as internal codes) to support your answers. Your goal is to help users accurately complete the questionnaire by providing concise and relevant information.
    """,
    question_id=6
)
