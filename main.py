import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
from PIL import Image
from io import BytesIO

# Set page config FIRST
st.set_page_config(page_title="Text-to-Image Generator", page_icon="🖼️")

# Load environment variables
load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

# Initialize the InferenceClient
client = InferenceClient(token=HF_TOKEN)

st.title("🖼️ Text-to-Image with Hugging Face InferenceClient")

prompt = st.text_input("Enter your image prompt:", "Astronaut riding a horse")

if st.button("Generate Image"):
    if not HF_TOKEN:
        st.error("Hugging Face API token not found! Please set HUGGINGFACE_TOKEN in your .env file.")
    else:
        with st.spinner("Generating image..."):
            try:
                image = client.text_to_image(
                    prompt,
                    model="black-forest-labs/FLUX.1-dev"
                )
                st.image(image, caption=prompt)
            except Exception as e:
                st.error(f"Failed to generate image: {e}")
