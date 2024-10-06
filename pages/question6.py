from question_template import render_question_page

render_question_page(
    question=(
        "Prohibited AI Systems:\n\n"
        "Is your system one of the following:\n"
        "- AI system that deploys subliminal techniques?\n"
        "- Exploitative AI systems?\n"
        "- Social scoring AI systems?\n"
        "- Predictive policing AI systems?\n"
        "- Scraping AI systems?\n"
        "- Biometric categorization AI systems?\n"
        "- ‘Real-time’ remote biometric identification systems in publicly accessible spaces?"
    ),
    example=(
        "For example, if your AI system exploits vulnerabilities of specific groups, manipulates decision-making beyond "
        "conscious awareness, or conducts social scoring, it may fall under these prohibited categories."
    ),
    articles = """
Article 5: Prohibited AI practices

1. The following AI practices shall be prohibited:

(a) the placing on the market, the putting into service or the use of an AI system that deploys subliminal techniques beyond
a person’s consciousness or purposefully manipulative or deceptive techniques, with the objective, or the effect of
materially distorting the behaviour of a person or a group of persons by appreciably impairing their ability to make an
informed decision, thereby causing them to take a decision that they would not have otherwise taken in a manner that
causes or is reasonably likely to cause that person, another person or group of persons significant harm;

(b) the placing on the market, the putting into service or the use of an AI system that exploits any of the vulnerabilities of
a natural person or a specific group of persons due to their age, disability or a specific social or economic situation, with
the objective, or the effect, of materially distorting the behaviour of that person or a person belonging to that group in
a manner that causes or is reasonably likely to cause that person or another person significant harm;

(c) the placing on the market, the putting into service or the use of AI systems for the evaluation or classification of natural
persons or groups of persons over a certain period of time based on their social behaviour or known, inferred or
predicted personal or personality characteristics, with the social score leading to either or both of the following:
(i) detrimental or unfavourable treatment of certain natural persons or groups of persons in social contexts that are
unrelated to the contexts in which the data was originally generated or collected;
(ii) detrimental or unfavourable treatment of certain natural persons or groups of persons that is unjustified or
disproportionate to their social behaviour or its gravity;

(d) the placing on the market, the putting into service for this specific purpose, or the use of an AI system for making risk
assessments of natural persons in order to assess or predict the risk of a natural person committing a criminal offence,
based solely on the profiling of a natural person or on assessing their personality traits and characteristics; this
prohibition shall not apply to AI systems used to support the human assessment of the involvement of a person in
a criminal activity, which is already based on objective and verifiable facts directly linked to a criminal activity;

(e) the placing on the market, the putting into service for this specific purpose, or the use of AI systems that create or
expand facial recognition databases through the untargeted scraping of facial images from the internet or CCTV footage;

(f) the placing on the market, the putting into service for this specific purpose, or the use of AI systems to infer emotions
of a natural person in the areas of workplace and education institutions, except where the use of the AI system is
intended to be put in place or into the market for medical or safety reasons;

(g) the placing on the market, the putting into service for this specific purpose, or the use of biometric categorisation
systems that categorise individually natural persons based on their biometric data to deduce or infer their race, political
opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation; this prohibition does
not cover any labelling or filtering of lawfully acquired biometric datasets, such as images, based on biometric data or
categorizing of biometric data in the area of law enforcement;

(h) the use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law
enforcement, unless and in so far as such use is strictly necessary for one of the following objectives:
(i) the targeted search for specific victims of abduction, trafficking in human beings or sexual exploitation of human
beings, as well as the search for missing persons;
(ii) the prevention of a specific, substantial and imminent threat to the life or physical safety of natural persons or
a genuine and present or genuine and foreseeable threat of a terrorist attack;
(iii) the localisation or identification of a person suspected of having committed a criminal offence, for the purpose of
conducting a criminal investigation or prosecution or executing a criminal penalty for offences referred to in
Annex II and punishable in the Member State concerned by a custodial sentence or a detention order for
a maximum period of at least four years.

Point (h) of the first subparagraph is without prejudice to Article 9 of Regulation (EU) 2016/679 for the processing of
biometric data for purposes other than law enforcement.
    """,
    next_page="pages/question7.py",
    chatbot_context="""
    You are an AI assistant helping users determine if their AI system falls under one of the prohibited practices in the AI Act.

    Your task is to provide accurate, clear, and concise answers based on the following context:

    - Main Question: {question}
    - Relevant Articles (related to prohibited AI practices): {articles}

    Ensure that your responses help users determine if their AI system falls under a prohibited category, based on the examples 
    and articles provided. Whenever possible, refer to the relevant articles to clarify their situation.
    """,
    question_id=6
)
