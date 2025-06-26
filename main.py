# main.py
import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Set page config
st.set_page_config(page_title="Text-to-Image Generator", page_icon="🖼️")

# ✅ Load environment variables
load_dotenv()

# ✅ Fetch token securely
api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

if not api_key:
    st.error("❌ API token not found. Make sure it's in the .env file.")
    st.stop()

# ✅ Initialize Hugging Face client
client = InferenceClient(token=api_key)

# UI
st.title("Text to Image Generator 🎨")
prompt = st.text_input("Enter a prompt:", "a fantasy castle in the sky")

if st.button("Generate Image"):
    with st.spinner("Generating..."):
        try:
            image = client.text_to_image(prompt=prompt)
            st.image(image)
        except Exception as e:
            st.error(f"❌ Failed to generate image: {e}")
