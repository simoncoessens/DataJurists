import re
import os
from pinecone import Pinecone, ServerlessSpec
from bs4 import BeautifulSoup
from openai import OpenAI
import streamlit as st


# Initialize Pinecone using the new API method
pinecone_api_key = st.secrets["pinecone"]["api_key"]
pc = Pinecone(api_key=pinecone_api_key)

# Create or connect to Pinecone index
index_name = "aiact"

# Connect to the index
index = pc.Index(index_name)

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["openai"]["api_key"])


# Function to generate embeddings for text (Using the new OpenAI client method)
def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")  # Clean text by removing newlines
    return client.embeddings.create(input=[text], model=model).data[0].embedding

# Load your HTML file (make sure the path to 'ai_act.html' is correct)
file_path = 'ai_act.xml.html'
with open(file_path, 'r') as file:
    soup = BeautifulSoup(file, 'lxml')  # You can use 'features="xml"' if it's an XML document

# Extract recitals using regex (e.g., <div class="eli-subdivision" id="rct_1">)
def extract_recitals(soup, unique_ids):
    recitals = []
    recital_divs = soup.find_all('div', id=re.compile(r'^rct_\d+$'))  # Matches IDs like rct_1, rct_2, etc.
    for div in recital_divs:
        recital_id = f"recital_{div.get('id')}"  # Add "recital_" prefix to make the ID unique
        if recital_id not in unique_ids:  # Check if the ID is unique
            unique_ids.add(recital_id)  # Add to the set of unique IDs
            recital_text = div.get_text().strip()  # Extract all text inside the div
            recitals.append({'id': recital_id, 'text': recital_text})
    return recitals

# Extract articles (e.g., <div id="001.001">, <div id="002.001">)
def extract_articles(soup, unique_ids):
    articles = []
    # Use regex to match article IDs in the format like '001.001', '002.001', etc.
    article_divs = soup.find_all('div', id=re.compile(r'^\d{3}\.\d{3}$'))  # Matches IDs like 101.002, 101.003, etc.
    
    for div in article_divs:
        paragraph_id = div.get('id')  # Get the paragraph ID, e.g., 101.002
        parent_article = div.find_parent('div', id=re.compile(r'^\d{3}$'))  # Find parent section like <div id="101">
        if parent_article:
            section_id = parent_article.get('id')  # Get the parent article ID (e.g., 101)
            unique_article_id = f"article_{section_id}_{paragraph_id}"  # Combine the parent ID and paragraph ID
        else:
            unique_article_id = f"article_{paragraph_id}"  # In case there's no clear parent
        
        if unique_article_id not in unique_ids:  # Check if the ID is unique
            unique_ids.add(unique_article_id)  # Add to the set of unique IDs
            article_text = div.get_text().strip()  # Extract all text inside the div
            articles.append({'id': unique_article_id, 'text': article_text})
    return articles

# Extract annexes using regex (e.g., <div class="eli-container" id="anx_II">)
def extract_annexes(soup, unique_ids):
    annexes = []
    annex_divs = soup.find_all('div', id=re.compile(r'^anx_[IVXLCDM]+$'))  # Matches IDs like anx_II, anx_III, etc.
    for div in annex_divs:
        annex_id = f"annex_{div.get('id')}"  # Add "annex_" prefix to make the ID unique
        if annex_id not in unique_ids:  # Check if the ID is unique
            unique_ids.add(annex_id)  # Add to the set of unique IDs
            annex_text = div.get_text().strip()  # Extract all text inside the div
            annexes.append({'id': annex_id, 'text': annex_text})
    return annexes

# Initialize a set to keep track of unique IDs
unique_ids = set()

# Extract data from the HTML document
recitals = extract_recitals(soup, unique_ids)
articles = extract_articles(soup, unique_ids)
annexes = extract_annexes(soup, unique_ids)

# Combine all results into one structure
content = recitals + articles + annexes

# Generate embeddings and upsert to Pinecone
for item in content:
    text = item['text']
    embedding = get_embedding(text)  # Get the embedding for the text
    index.upsert(vectors=[(item['id'], embedding, {'text': text})])  # Upsert the vector with metadata

print("Data has been pushed to Pinecone.")
