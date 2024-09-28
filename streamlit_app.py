import streamlit as st
import google.generativeai as genai
import os

st.title("Product Description Generator")
st.write("This app generates a product description based on the product name and keywords you provide.")

# Set the API key from an environment variable

api_key = st.text_input("Enter your Gemini API key:")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

product_name = st.text_input("Enter product name:")
keywords = st.text_input("Enter keywords (seperated by a comma):")

response = model.generate_content(f"Write about {product_name} and use keywords: {keywords}, also use emojis")

if st.button("Generate"):
    st.write(response.text)
else:
    st.write("Click the button to generate the product description.")
