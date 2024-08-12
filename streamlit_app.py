import streamlit as st
import google.generativeai as genai
import os

# Set the API key directly (replace 'YOUR_API_KEY' with your actual key)
genai.configure(api_key='AIzaSyAl4kXbygumAaURklrsR8J6a5xGYy5cBAY')
model = genai.GenerativeModel('gemini-1.5-flash')


st.title("Product Description Generator")
st.write("This app generates a product description based on the product name and keywords you provide.")

product_name = st.text_input("Enter product name:")
keywords = st.text_input("Enter keywords (seperated by a comma):")

response = model.generate_content(f"Write about {product_name} and use keywords {keywords}")
print(response.text)