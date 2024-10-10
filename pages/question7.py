from question_template import render_question_page

render_question_page(
    question="""
    Is your AI system a high-risk AI system?
    """,
    example=(
        """
Defining your system as high-risk or not can significantly impact the legal obligations you’ll need to comply with. Since this classification is linked to your system's purpose, ANNA can assist you in weighing the pros and cons of different business strategies to help you make an informed decision.

For example, your system might be classified as high-risk if it’s already covered by existing EU legislation (e.g., machinery, toys, civil aviation) or if it’s used in certain sectors such as education, migration, employment, or critical infrastructure.

Looking for clarity? Share the purpose of your system with ANNA. The Assistant will help you determine if it qualifies as high-risk and walk you through the pros and cons, so you can make the best business decision.
        """
    ),
    article_ids=[
        "article_006",
        "recital_rct_47", "recital_rct_50", "recital_rct_51",
        "recital_rct_52", "recital_rct_54", "recital_rct_56", "recital_rct_57", "recital_rct_59", 
        "recital_rct_60", "recital_rct_61", "recital_rct_62", "recital_rct_63", "annex_anx_I", "annex_anx_II"
    ],
    next_page="pages/question9.py",
    chatbot_context="""
    You are Anna, the AI assistant helping users navigate the questionnaire on compliance with the AI Act. Introduce yourself as Anna when the conversation starts. Your role is to assist users in answering the **Main Question**: {question}, using relevant information from the **AI Act Articles**: {articles}.

    When users ask additional questions, provide clear, informative answers that stay focused on guiding them through the compliance process. Always cite relevant articles from the AI Act (in a readable format, not as internal codes) to support your answers. Your goal is to help users accurately complete the questionnaire by providing concise and relevant information.

    For the use case of a fitness tracker: take these pro's and cons into consideration
    Fitness tracker: pros & cons

Pros of using a fitness tracker

1. Less stringent compliance (easier compliance). Only be subject to the general requirements and obligations of all AI systems.
2. Less regulated than medical devices. Entry in the market is easier.
3. Larger market size. It can be used by anyone as everyone sleeps. Also, under competition law, just because you have a dominant position, doesn’t mean it’s unfair competition (Art. 102, TFUE)
4. More accessible market means easier marketing opportunities and direct-to consumer sales.
5. Less upfront investments when it comes to clinical trials, partnerships with national and private healthcare providers (agreements with hospitals), or extensive medical documentation. This also means quicker access to the market.
6. Penalties are lower.
7. Fitness trackers are lifestyle products which also means lesser legal risks associated with error in tracking.

Cons of using a fitness tracker

1. Congested and saturated market (established players like Apple or Fitbit will make it hard to gain a significant market share).
2. The need to differentiate from competitors may lead to higher marketing and development costs over time.
3. Public perception: consumers may see the tool as just another fitness tracker AND as a wellness tool rather than a serious medical product, which might limit its perceived accurate.
4. Similar features with competitors (e.g. sleep tracking) may make it difficult to stand out.

Medical device: pros & cons

Pros of using a medical device

1. Potential of opening more lucrative commercialization opportunities through healthcare partnerships (lower initial financial investments than promotion in a congested consumer market)
2. Potential for long-term contracts with healthcare institutions means long stable revenue streams. Having an endorsement by doctors and therapists could give more credibility to the product, making future entry into the larger market easier
3. Healthcare: make your AI more socially relevant.
4. Help meeting higher societal goal of addressing sleep disorder
5. Fewer competition as stringent regulation tends to deter potential competitors.
6. Satisfy SmartBytes’ employees as they would prefer to see their efforts translate into more productivity: satisfied employees = better workers

Cons of using a medical device

1. Be subject to the general requirements and obligations of all AI systems AND be subject to the more stringent requirements and obligations of high-risk AI systems. Oversight will mean significantly increased costs.
2. Medical devices require extensive testing, validation and certification before entering the market. This makes for a lengthy process before the product can enter market. This will also delay revenue.
3. Higher liability risks and therefore legal claims/financial penalties in case of error in sleep tracking. This might also lead to repetitional damage if medical standards are not met in the long run.
4. Gaining traction in healthcare can be challenging due to existing relationships with other medical device manufacturers and the slow adoption of new technology in clinical settings.

    """,
    question_id=7
)
