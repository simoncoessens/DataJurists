from question_template import render_question_page

render_question_page(
    question=(
        "What is your role concerning the AI system or General Purpose AI (GPAI) model? "
        "Select one of the following options:\n\n"
        "- Provider\n"
        "- Downstream provider\n"
        "- Deployer\n"
        "- Authorized representative\n"
        "- Importer\n"
        "- Distributor"
    ),
    example=(
        "For instance, if you are developing an AI system, you might be classified as a 'Provider.' "
        "If you use an AI system under your authority, you could be a 'Deployer.' "
        "Alternatively, if you're working with a GPAI model, you could be an 'Authorized Representative.'"
    ),
    articles = """
Art. 3 (3-7, 68):

3. 'Provider' means a natural or legal person, public authority, agency, or other body that develops an AI system or 
a general-purpose AI model, or that has an AI system or a general-purpose AI model developed and places it on the 
market or puts it into service under its own name or trademark, whether for payment or free of charge.

4. 'Deployer' means a natural or legal person, public authority, agency, or other body using an AI system under its 
authority, except where the AI system is used in the course of a personal non-professional activity.

5. 'Authorised representative' means a natural or legal person located or established in the Union who has received and 
accepted a written mandate from a provider of an AI system or a general-purpose AI model to perform and carry out on its 
behalf the obligations and procedures established by this Regulation.

6. 'Importer' means a natural or legal person located or established in the Union that places on the market an AI system 
that bears the name or trademark of a natural or legal person established in a third country.

7. 'Distributor' means a natural or legal person in the supply chain, other than the provider or the importer, that makes 
an AI system available on the Union market.

68. 'Downstream provider' means a provider of an AI system, including a general-purpose AI system, which integrates an 
AI model, regardless of whether the AI model is provided by themselves and vertically integrated or provided by another 
entity based on contractual relations.
    """,
    next_page="pages/question4.py",
    chatbot_context="""
    You are an AI assistant helping users identify their role in relation to an AI system or General Purpose AI (GPAI) model 
    under the AI Act. Users may hold different responsibilities depending on their role, such as provider, deployer, or 
    authorized representative.

    Your task is to provide accurate, clear, and concise answers based on the following context:

    - Main Question: {question}
    - Relevant Articles (related to the AI Act definitions of roles): {articles}

    Ensure that your responses help users understand their role under the AI Act, based on the definitions provided in the 
    articles. Whenever possible, refer to the examples and relevant articles to clarify their situation.
    """,
    question_id=3
)
