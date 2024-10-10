import os
import time
from openai import OpenAI
from pinecone import Pinecone
import streamlit as st

# Initialize API keys
pinecone_api_key = st.secrets["pinecone"]["api_key"]
openai_api_key = st.secrets["openai"]["api_key"]

# Initialize Pinecone
pc = Pinecone(api_key=pinecone_api_key)

# Define the index name
index_name = "aiact"

# Connect to the index
index = pc.Index(index_name)

client = OpenAI(api_key=st.secrets["openai"]["api_key"])


def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")  # Clean text by removing newlines
    return client.embeddings.create(input=[text], model=model).data[0].embedding

# Function to upsert data into Pinecone
def upsert_to_pinecone(item_id, text, index):
    """
    Generates an embedding for the given text and upserts it to the Pinecone index.
    
    Args:
        item_id (str): The unique identifier for the item.
        text (str): The text content to be embedded and upserted.
        index: Pinecone index instance where the vector is upserted.
    """
    # Generate embedding for the given text
    embedding = get_embedding(text)
    
    # Upsert the item with the embedding and metadata into Pinecone
    index.upsert(vectors=[{'id': item_id, 'values': embedding, 'metadata': {'text': text}}])

    print(f"Upserted: {item_id} - {text[:30]}...")  # Prints the first 30 characters of the text for confirmation

# Example usage
if __name__ == "__main__":
    # Example text and ID to upsert
    file_path = 'temp.txt'  # Replace with the actual path to your text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text_value = file.read()
    unique_id = input('Type the ID: ')

    # Call the upsert function
    upsert_to_pinecone(unique_id, text_value, index)

    # Optionally, check the upserted record
    time.sleep(2)  # Sleep to allow time for the data to be indexed
    result = index.fetch(ids=[unique_id])
    
    if 'vectors' in result and unique_id in result['vectors']:
        print(f"Fetched text: {result['vectors'][unique_id]['metadata']['text']}")
    else:
        print(f"No record found for ID: {unique_id}")
