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

Context:
{context}

User's AI System Information:
{system_info}

Classify the AI system into one of the following risk categories:

1. **High Risk**: AI systems that have a significant impact on people's lives and safety. This includes systems used in critical infrastructures, education, employment, essential services, law enforcement, migration, and administration of justice.

   - **Examples**:
     - AI used in medical diagnosis (e.g., robot-assisted surgery)
     - AI for recruitment processes (e.g., CV-sorting software)
     - AI in credit scoring
     - AI for law enforcement purposes

2. **Limited Risk**: AI systems that interact with humans and may pose risks associated with transparency and informed consent.

   - **Examples**:
     - AI chatbots
     - AI-generated content (deep fakes)

3. **Minimal or No Risk**: AI systems that pose little to no risk to users.

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
        enum=["High Risk", "Limited Risk", "Minimal or No Risk"],
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
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo").with_structured_output(
    RiskAssessment
)

# Create a function that assesses the risk based on context and system information
def assess_risk(context, system_info):
    risk_chain = risk_assessment_prompt | llm
    result = risk_chain.invoke({"context": context, "system_info": system_info})
    return result

print(assess_risk(
"""
High risk
AI systems identified as high-risk include AI technology used in:

critical infrastructures (e.g. transport), that could put the life and health of citizens at risk
educational or vocational training, that may determine the access to education and professional course of someone’s life (e.g. scoring of exams)
safety components of products (e.g. AI application in robot-assisted surgery)
employment, management of workers and access to self-employment (e.g. CV-sorting software for recruitment procedures)
essential private and public services (e.g. credit scoring denying citizens opportunity to obtain a loan)
law enforcement that may interfere with people’s fundamental rights (e.g. evaluation of the reliability of evidence)
migration, asylum and border control management (e.g. automated examination of visa applications)
administration of justice and democratic processes (e.g. AI solutions to search for court rulings)
High-risk AI systems are subject to strict obligations before they can be put on the market:

adequate risk assessment and mitigation systems
high quality of the datasets feeding the system to minimise risks and discriminatory outcomes
logging of activity to ensure traceability of results
detailed documentation providing all information necessary on the system and its purpose for authorities to assess its compliance
clear and adequate information to the deployer
appropriate human oversight measures to minimise risk
high level of robustness, security and accuracy
All remote biometric identification systems are considered high-risk and subject to strict requirements. The use of remote biometric identification in publicly accessible spaces for law enforcement purposes is, in principle, prohibited.

Narrow exceptions are strictly defined and regulated, such as when necessary to search for a missing child, to prevent a specific and imminent terrorist threat or to detect, locate, identify or prosecute a perpetrator or suspect of a serious criminal offence.

Those usages is subject to authorisation by a judicial or other independent body and to appropriate limits in time, geographic reach and the data bases searched.

Limited risk
Limited risk refers to the risks associated with lack of transparency in AI usage. The AI Act introduces specific transparency obligations to ensure that humans are informed when necessary, fostering trust. For instance, when using AI systems such as chatbots, humans should be made aware that they are interacting with a machine so they can take an informed decision to continue or step back. Providers also have to ensure that AI-generated content is identifiable. Besides, AI-generated text published with the purpose to inform the public on matters of public interest must be labelled as artificially generated. This also applies to audio and video content constituting deep fakes.

Minimal or no risk
The AI Act allows the free use of minimal-risk AI. This includes applications such as AI-enabled video games or spam filters. The vast majority of AI systems currently used in the EU fall into this category.

""", 
"""
Im developping a cvscreening application to be deployed in germany. 
"""
))
