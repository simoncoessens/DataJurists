from question_template import render_question_page

render_question_page(
    question="""
    Provide a detailed description of the AI system that is the subject of this compliance analysis. Focus on its functionality and classify it as either an AI system or a General Purpose AI (GPAI) system. Explain the reasoning behind your classification.
    """,
    example=(
        """
**Context**

Understanding the nature of an AI system is essential when assessing compliance with regulations like the EU AI Act. The European Union uses an international definition that distinguishes AI systems from traditional software, focusing on two key categories: AI systems and General Purpose AI (GPAI) models.

An AI system is generally defined by the following characteristics:

- **Autonomy**: It operates with varying levels of independence, without constant human intervention.
- **Adaptability**: The system may evolve or learn after deployment, adjusting its behavior toward specific goals or objectives.
- **Inference**: It generates outputs such as predictions, recommendations, or decisions based on processing inputs.
- **Impact**: Its outputs can influence physical or virtual environments.

A General Purpose AI (GPAI) model is characterized by:

- **Generality**: It is designed to perform a broad range of tasks rather than being specialized.
- **Versatility**: It can be integrated into various downstream applications or systems.
- **Competency**: It demonstrates competence in multiple domains or tasks beyond its original scope.
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

    Ensure that your responses remain focused on helping users address the main question and always reference the articles you used (in bold and write them in readable text not as the internal representation) to give the information (but only use the **Relevant Articles** given above). Provide informative, easy-to-understand answers to any other questions they may have, 
    using the articles and examples provided to support your responses. The goal is to guide users in completing the questionnaire effectively.
    """,
    question_id=1
)
