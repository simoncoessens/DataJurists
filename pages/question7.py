from question_template import render_question_page

render_question_page(
    question=(
        "Does your AI system (or the product for which your AI system is a 'safety component') fall within any of the following high-risk categories? "
        "Please review the categories listed:"
        "\n\n**Annex I, Section B:**\n"
        "- Civil aviation security\n"
        "- Two- or three-wheel vehicles and quadricycles\n"
        "- Agricultural and forestry vehicles\n"
        "- Marine equipment\n"
        "- Interoperability of the rail systems\n"
        "- Motor vehicles and their trailers\n"
        "- Civil aviation\n\n"
        "**Annex I, Section A:**\n"
        "- Machinery\n"
        "- Toys\n"
        "- Recreational craft & personal watercraft\n"
        "- Lifts and safety components of lifts\n"
        "- Equipment and protective systems intended for use in potentially explosive atmospheres\n"
        "- Radio equipment\n"
        "- Pressure equipment\n"
        "- Cableway installations\n"
        "- Personal protective equipment\n"
        "- Appliances burning gaseous fuels\n"
        "- Medical devices\n"
        "- In vitro diagnostic medical devices"
    ),
    example=(
        "For example, if your AI system is used in motor vehicles, medical devices, or civil aviation, it may fall under high-risk categories, "
        "which are subject to strict regulations under the AI Act. Additionally, if your AI system is a safety component in machinery "
        "or personal protective equipment, it may also be considered high-risk."
    ),
    article_ids=[
        "article_006",
        "recital_rct_47", "recital_rct_50", "recital_rct_51"
    ],
    next_page="pages/question8.py",
    chatbot_context="""
    You are an Anna the AI assistant whose primary task is to help users answer the main question in the questionnaire with relation to the AI act. At introduction you say your name.
    Users may also ask additional questions related to the main question, and your role is to assist them by providing clear and accurate answers.

    Your main responsibilities include:

    - Assisting users in answering the **Main Question**: {question}
    - Referencing the **Relevant Articles** (from the AI Act): {articles}

    Ensure that your responses remain focused on helping users address the main question and always reference the articles you used (in bold) to give the information (but only use the **Relevant Articles** given above). Provide informative, easy-to-understand answers to any other questions they may have, 
    using the articles and examples provided to support your responses. The goal is to guide users in completing the questionnaire effectively.
    """,
    question_id=7
)
