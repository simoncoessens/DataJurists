from question_template import render_question_page

render_question_page(
    question=(
        "Does your AI system pose a significant risk of harm to the health, safety, or fundamental rights of any person? "
        "Based on your previous responses, the chatbot will assist you in determining whether your AI system might be considered high-risk under Article 6."
        "\n\nIf you are unsure, you can ask the chatbot for more information on specific conditions that define significant risks."
    ),
    example=(
        "For example, if your AI system is intended to perform profiling of natural persons or if it influences decision-making outcomes, "
        "it may pose a significant risk. The chatbot can help you explore whether your system meets these or other high-risk conditions."
    ),
    articles = """
Article 6:
1. An AI system is considered to pose a significant risk of harm to the health, safety, or fundamental rights of persons if it materially influences the outcome of decision-making or performs specific tasks that impact these areas. However, an AI system listed in Annex III is not considered high-risk where it meets any of the following conditions:

(a) The AI system is intended to perform a narrow procedural task.
(b) The AI system is intended to improve the result of a previously completed human activity.
(c) The AI system is intended to detect decision-making patterns or deviations from prior decision-making patterns without replacing human assessment.
(d) The AI system is intended to perform a preparatory task for an assessment relevant to the use cases in Annex III.

However, an AI system referred to in Annex III will **always** be considered high-risk where it performs profiling of natural persons.
    
Providers must document their assessment if they believe the system is not high-risk and be ready to provide documentation to national authorities when required.
    """,
    next_page="pages/question10.py",
    chatbot_context="""
    You are an AI assistant helping users determine whether their AI system poses a significant risk of harm to health, safety, or fundamental rights based on Article 6.

    - Main Question: {question}
    - Relevant Articles: {articles}

    Use the user's previous responses to help them assess whether their AI system poses significant risks. You should:
    
    1. Consider if the system performs profiling of natural persons or materially influences decision-making outcomes.
    2. Suggest conditions that would exempt the system from being high-risk (e.g., performing a narrow task, assisting human activities, etc.).
    3. Provide detailed information on documenting the assessment for systems that may not be high-risk according to the user's specific use case.

    If the user asks, explain that an AI system referred to in Annex III will always be high-risk if it performs profiling of natural persons or significantly impacts decision-making without human review.
    """,
    question_id=9
)
