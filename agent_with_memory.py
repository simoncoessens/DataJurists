import os
from langchain.agents import initialize_agent
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.memory import ConversationBufferMemory

# Set your OpenAI API key
# Fetch the OpenAI API key from Streamlit secrets
openai_api_key = st.secrets["openai"]["api_key"]

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = openai_api_key


class AgentWithMemory:
    def __init__(self,  model, context=""):
        # Initialize the conversation memory with the provided context
        self.memory = ConversationBufferMemory(memory_key="chat_history")
        if context:
            # Add the initial context to the memory as an AI message
            self.memory.chat_memory.add_ai_message(context)
        
        # Initialize the language model
        self.llm = ChatOpenAI(temperature=0, model=model)
        
        # Create the agent without tools and with conversation memory
        self.agent_chain = initialize_agent(
            [],
            self.llm,
            agent="conversational-react-description",
            memory=self.memory,
            verbose=True,
            handle_parsing_errors=True 
        )
    
    def run(self, prompt):
        # Use the invoke method instead of run
        # Prepare the input as a dictionary
        return self.agent_chain.invoke({"input": prompt})

# Example usage from another function
def main():
    # Initialize the agent with some context about the AI Act
    context = (
        "The European Union AI Act is a proposed regulation on artificial intelligence in the "
        "European Union. It aims to introduce a common regulatory and legal framework for artificial "
        "intelligence. The regulation classifies AI applications into risk categories and imposes "
        "different regulatory requirements depending on the category."
    )
    agent = AgentWithMemory(context=context)
    
    # Let the user prompt some questions
    prompts = [
        "I am developing a cv screening application, what applies to me?",
        "What am i developping?"
    ]
    
    for prompt in prompts:
        response = agent.run(prompt)
        print(f"Prompt: {prompt}\nResponse: {response['output']}\n")

if __name__ == "__main__":
    main()
