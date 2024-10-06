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
    articles = """
Article 6:
1. Irrespective of whether an AI system is placed on the market or put into service independently of the products referred to in points (a) and (b), 
that AI system shall be considered to be high-risk where both of the following conditions are fulfilled:

(a) the AI system is intended to be used as a safety component of a product, or the AI system is itself a product, covered by the Union harmonisation legislation listed in Annex I;

(b) the product whose safety component pursuant to point (a) is the AI system, or the AI system itself as a product, is required to undergo a third-party conformity assessment, with a view to the placing on the market or the putting into service of that product pursuant to the Union harmonisation legislation listed in Annex I.
    """,
    next_page="pages/question8.py",
    chatbot_context="""
    You are an AI assistant helping users identify whether their AI system or its related product falls into the high-risk categories defined by the AI Act.
    
    - Main Question: {question}
    - Relevant Articles and Annexes: {articles}

    Assist users in determining whether their AI system is considered high-risk by referencing the provided annexes and articles. Ensure users understand 
    the specific products or applications mentioned in the legislation and how they relate to the high-risk categories.
    """,
    question_id=7
)
