from question_template import render_question_page

render_question_page(
    question=(
        "Downstream Modification:\n\n"
        "Will a downstream modification happen?\n\n"
        "This includes:\n"
        "- Putting another name or trademark on a high-risk AI system already placed on the market or put into service;\n"
        "- Making a substantial modification to a high-risk AI system that has already been placed on the market or put into service;\n"
        "- Modifying the intended purpose of an AI system, including a general-purpose AI system, which has not been classified as high-risk, "
        "but has already been placed on the market or put into service, in such a way that it becomes a high-risk AI system in accordance with Article 6."
    ),
    example=(
        "For example, if you rebrand an AI system already classified as high-risk, or modify an existing AI system in a way that it now meets the high-risk criteria, "
        "you may fall under the obligations of a provider according to the AI Act."
    ),
    articles = """
Article 25: Responsibilities along the AI value chain

1. Any distributor, importer, deployer or other third-party shall be considered to be a provider of a high-risk AI system
for the purposes of this Regulation and shall be subject to the obligations of the provider under Article 16, in any of the
following circumstances:
(a) they put their name or trademark on a high-risk AI system already placed on the market or put into service, without
prejudice to contractual arrangements stipulating that the obligations are otherwise allocated;
(b) they make a substantial modification to a high-risk AI system that has already been placed on the market or has already
been put into service in such a way that it remains a high-risk AI system pursuant to Article 6;
(c) they modify the intended purpose of an AI system, including a general-purpose AI system, which has not been classified
as high-risk and has already been placed on the market or put into service in such a way that the AI system concerned
becomes a high-risk AI system in accordance with Article 6.

2. Where the circumstances referred to in paragraph 1 occur, the provider that initially placed the AI system on the
market or put it into service shall no longer be considered to be a provider of that specific AI system for the purposes of
this Regulation. That initial provider shall closely cooperate with new providers and shall make available the necessary
information and provide the reasonably expected technical access and other assistance that are required for the fulfilment of
the obligations set out in this Regulation, in particular regarding the compliance with the conformity assessment of
high-risk AI systems. This paragraph shall not apply in cases where the initial provider has clearly specified that its AI
system is not to be changed into a high-risk AI system and therefore does not fall under the obligation to hand over the
documentation.

3. In the case of high-risk AI systems that are safety components of products covered by the Union harmonisation
legislation listed in Section A of Annex I, the product manufacturer shall be considered to be the provider of the high-risk
AI system, and shall be subject to the obligations under Article 16 under either of the following circumstances:
(a) the high-risk AI system is placed on the market together with the product under the name or trademark of the product
manufacturer;
(b) the high-risk AI system is put into service under the name or trademark of the product manufacturer after the product
has been placed on the market.

4. The provider of a high-risk AI system and the third party that supplies an AI system, tools, services, components, or
processes that are used or integrated in a high-risk AI system shall, by written agreement, specify the necessary information,
capabilities, technical access and other assistance based on the generally acknowledged state of the art, in order to enable
the provider of the high-risk AI system to fully comply with the obligations set out in this Regulation. This paragraph shall
not apply to third parties making accessible to the public tools, services, processes, or components, other than
general-purpose AI models, under a free and open-source licence.

The AI Office may develop and recommend voluntary model terms for contracts between providers of high-risk AI systems
and third parties that supply tools, services, components or processes that are used for or integrated into high-risk AI
systems. When developing those voluntary model terms, the AI Office shall take into account possible contractual
requirements applicable in specific sectors or business cases. The voluntary model terms shall be published and be available
free of charge in an easily usable electronic format.

5. Paragraphs 2 and 3 are without prejudice to the need to observe and protect intellectual property rights, confidential
business information and trade secrets in accordance with Union and national law.
    """,
    next_page="pages/question6.py",
    chatbot_context="""
    You are an AI assistant helping users understand whether they are subject to obligations related to downstream modifications 
    of high-risk AI systems under the AI Act.

    Your task is to provide accurate, clear, and concise answers based on the following context:

    - Main Question: {question}
    - Relevant Articles (related to downstream modifications of high-risk AI systems): {articles}

    Ensure that your responses help users understand whether their actions will be classified as a downstream modification and 
    whether they will be considered as a provider of a high-risk AI system. Whenever possible, refer to the examples and relevant 
    articles to clarify their situation.
    """,
    question_id=5
)
