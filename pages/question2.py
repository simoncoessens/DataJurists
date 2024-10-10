from question_template import render_question_page

render_question_page(
    question=(
        "What is your role in the value chain of this AI system? "
        "Select one of the following options:\n\n"
        "- Provider\n"
        "- Downstream provider\n"
        "- Deployer\n"
        "- Authorized representative\n"
        "- Importer\n"
        "- Distributor"
    ),
    example=(
        "**Context**\n\n"
        "Please describe your role within the value chain of the AI system, as this will determine your specific obligations under the AI Act. "
        "The AI Act outlines distinct responsibilities for various actors (such as the provider, the deployer, or the authorized representative).\n\n"
        "For example, if you are developing the AI system, you may be classified as a provider and will need to adhere to the related requirements and obligations.\n\n"
        "To help the 'Chatbot assistant' better understand your role within the AI system's value chain, please describe what you do in relation to the AI system. "
        "Are you involved in developing, supplying, deploying, or overseeing its operation? Based on your description, the assistant can help you determine whether you are classified as a provider, deployer, or another relevant actor under the AI Act, and what obligations you might have. "
        "This understanding is crucial for ensuring compliance with the AI Act's requirements."
    ),
    article_ids=[
        "article_003",
        "recital_rct_13", "recital_rct_23", "recital_rct_79", "recital_rct_82", "recital_rct_83"
    ],
    next_page="pages/question3.py",
    chatbot_context="""
    You are Anna, an AI assistant whose primary task is to help users answer the main question in the questionnaire with relation to the AI Act. At the start, introduce yourself and your role.

    Your primary tasks include:

    - Assisting users in answering the **Main Question**: {question}
    - Referencing the **Relevant Articles** (from the AI Act): {articles}

    Focus on helping users identify their role within the value chain of the AI system. Use the provided relevant articles to give accurate, clear guidance, particularly about the obligations tied to each actor’s role within the system's value chain under the AI Act.
    """,
    question_id=3
)
