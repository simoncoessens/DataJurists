from question_template import render_question_page

render_question_page(
    question="Does the Artificial Intelligence Act (AIA) apply to you, or are you excluded from its scope?",
    example=(
        "For example, you may be excluded if your AI system is used exclusively for military purposes, "
        "or if it is deployed by a third-country public authority for international cooperation with the Union. "
        "Alternatively, if the AI system is part of research and development activities not yet placed on the market, "
        "you may also be exempt from the regulation."
    ),
    articles = """
Art. 2 (3, 4, 6, 8, 10, 12)

3. This Regulation does not apply to areas outside the scope of Union law, and shall not, in any event, affect the
competences of the Member States concerning national security, regardless of the type of entity 
entrusted by the Member State with carrying out tasks in relation to those competences.

4. This Regulation applies neither to public authorities in a third country nor to international organisations falling
within the scope of this Regulation pursuant to paragraph 1, where those authorities or organisations use AI systems in the
framework of international cooperation or agreements for law enforcement and judicial cooperation with the Union or
with one or more Member States, provided that such a third country or international organisation provides adequate
safeguards with respect to the protection of fundamental rights and freedoms of individuals.

6. This Regulation does not apply to AI systems or AI models, including their output, specifically developed and put into
service for the sole purpose of scientific research and development.

8. This Regulation does not apply to any research, testing or development activity regarding AI systems or AI models
prior to their being placed on the market or put into service. Such activities shall be conducted in accordance with
applicable Union law. Testing in real world conditions shall not be covered by that exclusion.

10. This Regulation does not apply to obligations of deployers who are natural persons using AI systems in the course of
a purely personal non-professional activity.

12. This Regulation does not apply to AI systems released under free and open-source licences, unless they are placed on
the market or put into service as high-risk AI systems or as an AI system that falls under Article 5 or 50.
    """,
    next_page="pages/question3.py",
    chatbot_context="""
    You are an AI assistant helping users determine whether the Artificial Intelligence Act (AIA) applies to their AI systems. 
    Users may be excluded from its scope under certain conditions outlined in the regulation.

    Your task is to provide accurate, clear, and concise answers based on the following context:

    - Main Question: {question}
    - Relevant Articles (related to AIA exceptions): {articles}

    Ensure that your responses help users understand whether they are excluded from the AIA based on the specific conditions outlined.
    Whenever possible, refer to the examples and relevant articles provided to clarify their situation.
    """,
    question_id=2
)
