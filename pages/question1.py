from question_template import render_question_page

render_question_page(
    question="Is the system you are developing categorized as an AI system or a General Purpose AI (GPAI) model?",
    example=(
    "For example, the system you are developing could be an AI-based chatbot for customer support, "
    "an autonomous decision-making algorithm, or a machine learning model designed to predict user behavior. "
    "Alternatively, if you are working on a General Purpose AI (GPAI) model, it might be intended for broad applications "
    "such as language processing or image recognition across multiple industries."
),
    articles = """
AI system’ means a machine-based system that is designed to operate with varying levels of autonomy and that may
exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the input it receives,
how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or
virtual environments;

general-purpose AI model’ means an AI model, including where such an AI model is trained with a large amount of
data using self-supervision at scale, that displays significant generality and is capable of competently performing
a wide range of distinct tasks regardless of the way the model is placed on the market and that can be integrated into
a variety of downstream systems or applications, except AI models that are used for research, development or
prototyping activities before they are placed on the market;
    """,
    next_page="pages/question2.py",
    chatbot_context="""
    You are an AI assistant helping users with questions about deploying, using, or putting systems into service. 
    Users will ask questions to clarify the main inquiry they are working on.

    Your task is to provide accurate, clear, and concise answers based on the following context:

    - Main Question: {question}
    - Relevant Articles (related to the AI Act): {articles}

    Ensure that your responses are informative and assist users in understanding the main question.
    Whenever possible, refer to the example provided, and offer additional insight based on the relevant articles.
    """,
    question_id=1
)
