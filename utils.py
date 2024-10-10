# utils.py
import streamlit as st

# Function to read the base64 string from a file
def read_base64_from_file(file_path):
    with open(file_path, "r") as file:
        encoded_string = file.read()
    return encoded_string

# Function to add the background image from the base64 string
def add_bg_from_base64(image):
    encoded_bg_image = read_base64_from_file(image)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_bg_image}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
