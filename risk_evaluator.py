# evaluator.py

from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import streamlit as st
from pydantic import BaseModel, Field
from typing import List
import os

# Fetch the OpenAI API key from Streamlit secrets
openai_api_key = st.secrets["openai"]["api_key"]

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = openai_api_key

# Define the risk assessment prompt template based on the EU AI Act
risk_assessment_prompt = ChatPromptTemplate.from_template(
    """
You are an AI risk assessment expert well-versed in the EU AI Act.

Based on the following context and information about the user's AI system, determine the risk category according to the EU AI Act.

Relevant Articles from the AI act:
{context}

User's AI System Information:
{system_info}

Classify the AI system into one of the following risk categories:

1. **Prohibited Risk**: AI systems that are considered unacceptable and are prohibited under the EU AI Act.

   - **Examples**:
     - AI systems that manipulate human behavior to circumvent users' free will.
     - Social scoring by governments.
     - Real-time biometric identification systems used by law enforcement in public spaces (with some exceptions).

2. **High Risk**: AI systems that have a significant impact on people's lives and safety. This includes systems used in critical infrastructures, education, employment, essential services, law enforcement, migration, and administration of justice.

   - **Examples**:
     - AI used in medical diagnosis (e.g., robot-assisted surgery)
     - AI for recruitment processes (e.g., CV-sorting software)
     - AI in credit scoring
     - AI for law enforcement purposes

3. **Transparency Risk**: AI systems that interact with humans and may pose risks associated with transparency and informed consent.

   - **Examples**:
     - AI chatbots
     - AI-generated content (deep fakes)

4. **Minimal Risk**: AI systems that pose little to no risk to users.

   - **Examples**:
     - AI-enabled video games
     - Spam filters

Provide the following:

- **Risk Category**: The risk level of the AI system.
- **Explanation**: A brief explanation justifying the classification.
- **Obligations or Recommendations**: Outline any obligations the AI system must comply with according to the EU AI Act or recommend actions to mitigate risks.

Return the information in a structured format.
"""
)

# Define a custom model for risk classification and obligations
class RiskAssessment(BaseModel):
    risk_category: str = Field(
        ...,
        enum=["Prohibited Risk", "High Risk", "Transparency Risk", "Minimal Risk"],
        description="Risk level of the AI system according to the EU AI Act",
    )
    explanation: str = Field(
        ...,
        description="Explanation for the risk classification",
    )
    obligations_or_recommendations: List[str] = Field(
        default=[],
        description="Obligations or recommendations for compliance or risk mitigation",
    )

# Initialize the LLM with structured output for risk assessment
llm = ChatOpenAI(temperature=0, model="gpt-4").with_structured_output(
    RiskAssessment
)

# Create a function that assesses the risk based on context and system information
def assess_risk(context, system_info):
    risk_chain = risk_assessment_prompt | llm
    result = risk_chain.invoke({"context": context, "system_info": system_info})
    return result

# Example usage
print(assess_risk(
    """
Prohibited Risk:
AI systems identified as prohibited risk include AI technology used in:
- Subliminal techniques beyond a person's consciousness to materially distort a person's behavior in a manner that causes or is likely to cause physical or psychological harm.
- Exploitation of vulnerabilities of a specific group of persons due to their age, physical, or mental disability.
- Social scoring by governments.
- Real-time biometric identification systems used by law enforcement in public spaces (with some exceptions).

High Risk:
AI systems identified as high-risk include AI technology used in:
- Critical infrastructures (e.g., transport) that could put the life and health of citizens at risk.
- Educational or vocational training that may determine the access to education and professional course of someone's life (e.g., scoring of exams).
- Safety components of products (e.g., AI application in robot-assisted surgery).
- Employment, management of workers, and access to self-employment (e.g., CV-sorting software for recruitment procedures).
- Essential private and public services (e.g., credit scoring denying citizens the opportunity to obtain a loan).
- Law enforcement that may interfere with people's fundamental rights (e.g., evaluation of the reliability of evidence).
- Migration, asylum, and border control management (e.g., automated examination of visa applications).
- Administration of justice and democratic processes (e.g., AI solutions to search for court rulings).

High-risk AI systems are subject to strict obligations before they can be put on the market:
- Adequate risk assessment and mitigation systems.
- High quality of the datasets feeding the system to minimize risks and discriminatory outcomes.
- Logging of activity to ensure traceability of results.
- Detailed documentation providing all information necessary on the system and its purpose for authorities to assess its compliance.
- Clear and adequate information to the deployer.
- Appropriate human oversight measures to minimize risk.
- High level of robustness, security, and accuracy.

Transparency Risk:
Transparency risk refers to the risks associated with lack of transparency in AI usage. The AI Act introduces specific transparency obligations to ensure that humans are informed when necessary, fostering trust. For instance, when using AI systems such as chatbots, humans should be made aware that they are interacting with a machine so they can make an informed decision to continue or step back. Providers also have to ensure that AI-generated content is identifiable. Additionally, AI-generated text published with the purpose of informing the public on matters of public interest must be labeled as artificially generated. This also applies to audio and video content constituting deep fakes.

Minimal Risk:
The AI Act allows the free use of minimal-risk AI. This includes applications such as AI-enabled video games or spam filters. The vast majority of AI systems currently used in the EU fall into this category.
    """,
    """
I'm developing a CV screening application to be deployed in Germany.
    """
))
