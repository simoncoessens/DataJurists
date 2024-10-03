from question_template import render_question_page

render_question_page(
    question=(
        "Geographical Scope:\n\n"
        "Irrespective of whether you are established or located within the Union or in a third country, are you placing AI systems "
        "on the market or putting them into service in the Union?\n\n"
        "Do you have your place of establishment, or are you located in a third country, but the output produced by the AI system is used in the Union?"
    ),
    example=(
        "For example, if you are a provider located in a third country but selling AI systems in the EU, or if your AI system produces "
        "an output that is used within the EU, this regulation will apply to you."
    ),
    articles = """
Article 2 (1 a, c):

1. This Regulation applies to:

(a) Providers placing on the market or putting into service AI systems or placing on the market general-purpose AI models 
in the Union, irrespective of whether those providers are established or located within the Union or in a third country.

(c) Providers and deployers of AI systems that have their place of establishment or are located in a third country, where the 
output produced by the AI system is used in the Union.
    """,
    next_page="pages/question5.py",
    chatbot_context="""
    You are an AI assistant helping users determine whether the geographical scope of the AI Act applies to them. 
    This question focuses on whether their AI system is placed on the market or put into service in the Union, or whether the 
    output of their AI system is used in the Union.

    Your task is to provide accurate, clear, and concise answers based on the following context:

    - Main Question: {question}
    - Relevant Articles (related to the geographical scope of the AI Act): {articles}

    Ensure that your responses help users understand if the AI Act applies to them based on where their AI system is placed 
    on the market or where its output is used. Whenever possible, refer to the examples and relevant articles to clarify their situation.
    """,
    question_id=4
)
