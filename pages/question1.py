from question_template import render_question_page

render_question_page(
    question="""
    Describe the AI system that will be the target of this compliance analysis. Include
    details about its functionality and whether it can be classified as an AI system or a
    General Purpose AI system.
    """,
    example=(
        """
**Context**
Defining what constitutes an AI system can sometimes be tricky. The European
Union has opted to align with an international definition, aiming to distinguish AI
systems from traditional software. The EU AI Act focuses on two primary targets:
AI systems and General Purpose AI (GPAI) models.
An AI system is characterized by the following features:
**Autonomy**: It’s designed to operate with varying degrees of independence.
**Adaptability**: The system may show adaptive behavior after deployment,
working towards explicit or implicit objectives.
**Inference**: It processes input to generate outputs like predictions, content,
recommendations, or decisions.
**Impact**: These outputs can affect physical or virtual environments.
A General Purpose AI (GPAI) model, on the other hand, has these characteristics:
It demonstrates significant generality.
It can competently perform a wide variety of tasks,
It can be integrated into various downstream systems or applications.
    """
    ),
    article_ids=["article_003", "recital_rct_12", "recital_rct_97", "recital_rct_100"],
    next_page="pages/question2.py",
    chatbot_context="""
    You are an Anna the AI assistant whose primary task is to help users answer the main question in the questionnaire with relation to the AI act. At introduction you say your name.
    Users may also ask additional questions related to the main question, and your role is to assist them by providing clear and accurate answers.

    Your main responsibilities include:

    - Assisting users in answering the **Main Question**: {question}
    - Referencing the **Relevant Articles** (from the AI Act): {articles}

    Ensure that your responses remain focused on helping users address the main question and always reference the articles you used (in bold) to give the information (but only use the **Relevant Articles** given above). Provide informative, easy-to-understand answers to any other questions they may have, 
    using the articles and examples provided to support your responses. The goal is to guide users in completing the questionnaire effectively.
    """,
    question_id=1
)
