from question_template import render_question_page

render_question_page(
    question=(
        "What is the purpose or context in which the AI system is going to be used? "
        "Based on your previous responses, the chatbot will suggest which high-risk category your AI system might fall under according to Article 6."
        "\n\nHigh-risk categories include areas such as biometrics, critical infrastructure, education, employment, law enforcement, migration, or justice."
        "\n\nYou can also ask the chatbot for more detailed information on each of these categories if needed."
    ),
    example=(
        "For example, if your AI system is used for biometric identification or in the management of critical infrastructure, "
        "it may fall under high-risk categories as defined by the AI Act. The chatbot will suggest relevant categories based on your responses."
    ),
    articles = """
High-risk AI systems pursuant to Article 6(2) are listed in the following areas:
1. **Biometrics** (remote identification, categorisation, emotion recognition).
2. **Critical Infrastructure** (AI systems as safety components in digital infrastructure, traffic, utilities like water, gas, heating, electricity).
3. **Education** (determining access, evaluating outcomes, monitoring behavior).
4. **Employment** (recruitment, performance monitoring, task allocation).
5. **Access to essential services** (creditworthiness, public benefits, emergency services).
6. **Law Enforcement** (risk assessment, evidence evaluation, polygraphs).
7. **Migration and Border Control** (risk assessment, visa applications).
8. **Administration of Justice** (supporting judicial authorities, influencing elections).
    """,
    next_page="pages/question9.py",
    chatbot_context="""
    You are an AI assistant helping users identify the high-risk category their AI system might belong to based on Article 6 of the AI Act.
    
    - Main Question: {question}
    - Relevant Articles: {articles}

    Use the user's previous responses to suggest which high-risk category their AI system likely falls into. You have access to the following high-risk areas:
    1. **Biometrics**:
        - AI systems for remote biometric identification (excluding verification for confirming a person’s identity).
        - AI systems for biometric categorisation based on sensitive/protected attributes.
        - AI systems for emotion recognition.
    
    2. **Critical Infrastructure**:
        - AI systems as safety components in digital infrastructure, road traffic, or utilities like water, gas, heating, electricity.
    
    3. **Education and Vocational Training**:
        - AI systems for determining access/admission, evaluating learning outcomes, or monitoring behavior in educational institutions.
    
    4. **Employment and Workers’ Management**:
        - AI systems for recruitment, job filtering, performance monitoring, task allocation, or contract decisions.
    
    5. **Access to Essential Services**:
        - AI systems for evaluating creditworthiness, public benefits eligibility, or emergency services dispatching.

    6. **Law Enforcement**:
        - AI systems for risk assessment, polygraphs, evaluating evidence, or assessing re-offense risk.
    
    7. **Migration, Asylum, and Border Control**:
        - AI systems for risk assessments related to migration or assisting with asylum or visa applications.
    
    8. **Administration of Justice and Democratic Processes**:
        - AI systems supporting judicial authorities or influencing elections/referenda outcomes.

    Your task is to:
    1. Suggest the most relevant high-risk categories based on the user's answers to previous questions.
    2. Provide detailed information about any category if requested by the user.
    """,
    question_id=8
)
