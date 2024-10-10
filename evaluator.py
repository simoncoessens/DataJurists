# evaluator.py

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import streamlit as st
from pydantic import BaseModel, Field
from typing import List
import os


# Fetch the OpenAI API key from Streamlit secrets
openai_api_key = st.secrets["openai"]["api_key"]

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = openai_api_key

# Define the classification and suggestion prompt template
tagging_prompt = ChatPromptTemplate.from_template(
    """
Evaluate the user's response based on the following question:

Question: {question}

Response: {input}

Classify the response into one of the following categories:
1. Good Enough - The response answers the question well and in detail.
2. Good - The response is an answer to the question.
3. Vague - The response has nothing to do with the question.
4. Too Vague - The response is not a sentence in English.

Provide suggestions for improvement if necessary. These suggestions should help the user provide more clarity, detail, or relevance.

Return both the classification and suggestions for improvement.
"""
)

# Define a custom model for response quality and suggestions
class Classification(BaseModel):
    response_quality: str = Field(
        ...,
        enum=["Good Enough", "Good", "Vague", "Too Vague"],
        description="Classify how well the user's response answers the question",
    )
    suggestions: List[str] = Field(
        ...,
        description="Suggestions for improving the user's response",
    )

# Initialize the LLM with structured output for classification and suggestions
llm = ChatOpenAI(temperature=0.5, model="gpt-3.5-turbo").with_structured_output(
    Classification
)

# Create a reusable function that evaluates responses based on the template
def classify_and_suggest(question, user_input):
    tagging_chain = tagging_prompt | llm
    result = tagging_chain.invoke({"question": question, "input": user_input})
    return result