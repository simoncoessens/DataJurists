from question_template import render_question_page

render_question_page(
    question="""
    Describe the AI system that will be the target of this compliance analysis. Include details about its functionality and whether it can be classified as an AI system or a General Purpose AI system.
    """,
    example=(
        """

Defining what constitutes an AI system can sometimes be tricky. The European Union has opted to align with an international definition, aiming to distinguish AI systems from traditional software (such as a system that calculates your BMI). The EU AI Act focuses on two primary targets: AI systems and General Purpose AI (GPAI) models.

An AI system is characterized by the following features:

- **Autonomy**
- **Adaptability**
- **Inference**
- **Impact**

A General Purpose AI (GPAI) model, on the other hand, has these characteristics:

- **Significant generality**
- **Performs a wide variety of tasks**
- **Integrated into downstream systems**

Not sure where your AI system fits in? No worries! Ask **ANNA** to help clear things up and guide you through the process.
        """
    ),
    article_ids=["article_003", "recital_rct_12", "recital_rct_97", "recital_rct_100"],
    next_page="pages/B.py",
    chatbot_context="""
    You are Anna, the AI assistant helping users navigate the questionnaire on compliance with the AI Act. Introduce yourself as Anna when the conversation starts. Your role is to assist users in answering the **Main Question**: {question}, using relevant information from the **AI Act Articles**: {articles}.

    When users ask additional questions, provide clear, informative answers that stay focused on guiding them through the compliance process. Always cite relevant articles from the AI Act (in a readable format, not as internal codes) to support your answers. Your goal is to help users accurately complete the questionnaire by providing concise and relevant information.
    """,
    question_id=1
)
