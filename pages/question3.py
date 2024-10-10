from question_template import render_question_page

render_question_page(
    question="""
    What is your role in the value chain of this AI system? 
    """,
    example=(
        """
The AI Act outlines distinct responsibilities for different actors. For example, if you are developing the AI system, you may be classified as a provider and will need to adhere to the related requirements and obligations.

To help ANNA better understand your role within the AI system's value chain, please describe what you do in relation to the AI system. Are you involved in developing, deploying, or overseeing its operation? Based on your description, ANNA can help determine whether you are classified as a provider, deployer, or another relevant actor under the AI Act and what obligations you might have. This understanding is crucial for ensuring compliance with the AI Act's requirements.
        """
    ),
    article_ids=[
        "article_003",
        "recital_rct_13", "recital_rct_23", "recital_rct_79", "recital_rct_82", "recital_rct_83"
    ],
    next_page="pages/question4.py",
    chatbot_context="""
    You are Anna, the AI assistant helping users navigate the questionnaire on compliance with the AI Act. Introduce yourself as Anna when the conversation starts. Your role is to assist users in answering the **Main Question**: {question}, using relevant information from the **AI Act Articles**: {articles}.

    When users ask additional questions, provide clear, informative answers that stay focused on guiding them through the compliance process. Always cite relevant articles from the AI Act (in a readable format, not as internal codes) to support your answers. Your goal is to help users accurately complete the questionnaire by providing concise and relevant information.
    """,
    question_id=3
)
