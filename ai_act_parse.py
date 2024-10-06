import re
from bs4 import BeautifulSoup

# Load your HTML file
with open('ai_act.xml.html', 'r') as file:
    soup = BeautifulSoup(file, 'lxml')

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

# Execute the functions to extract the content with unique ID tracking
recitals = extract_recitals(soup, unique_ids)
articles = extract_articles(soup, unique_ids)
annexes = extract_annexes(soup, unique_ids)

# Combine all results into one structure
content = {
    'recitals': recitals,
    'articles': articles,
    'annexes': annexes
}

# Write the extracted content to a text file
with open('ai_act_extracted_content.txt', 'w') as f:
    for key, items in content.items():
        f.write(f"\n--- {key.upper()} ---\n")
        for item in items:
            f.write(f"ID: {item['id']}\n")
            f.write(f"Text: {item['text']}\n\n")

print("Content has been written to ai_act_extracted_content.txt")
