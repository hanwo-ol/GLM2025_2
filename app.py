import streamlit as st
import os
import base64
from utils.rag import build_index
from utils.bot import MathBot
from PIL import Image

st.set_page_config(page_title="Math Chatbot with RAG & Code Execution", layout="wide")

st.title("🧮 Math Chatbot powered by Gemini & RAG")

# Sidebar
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    
    st.divider()
    
    st.header("Knowledge Base")
    if st.button("Build/Rebuild Knowledge Base"):
        if not api_key:
            st.error("Please enter an API Key first.")
        else:
            with st.spinner("Fetching data from GitHub and building index... (This may take a minute)"):
                try:
                    build_index(api_key)
                    st.success("Knowledge Base Built Successfully!")
                except Exception as e:
                    st.error(f"Error: {e}")

    st.divider()
    st.markdown("### Features")
    st.markdown("- **RAG**: Queries `hanwo-ol/GLM2025_2`")
    st.markdown("- **Python & R**: Can execute code")
    st.markdown("- **Multimodal**: Upload images/PDFs")

# Main Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

if "bot" not in st.session_state and api_key:
    st.session_state.bot = MathBot(api_key)

# File Uploader
uploaded_file = st.file_uploader("Upload an image (PNG, JPG) or PDF for visual math problems", type=["png", "jpg", "jpeg", "pdf"])
file_data = None

if uploaded_file:
    # Check type
    mime_type = uploaded_file.type
    
    if "image" in mime_type:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    elif "pdf" in mime_type:
        st.info(f"PDF Uploaded: {uploaded_file.name}")
    
    # Process for Gemini (Common for both Image and PDF)
    bytes_data = uploaded_file.getvalue()
    base64_data = base64.b64encode(bytes_data).decode('utf-8')
    
    file_data = {
        "mime_type": mime_type,
        "data": base64_data
    }

# Display Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "images" in msg and msg["images"]:
            for img_path in msg["images"]:
                if os.path.exists(img_path):
                    st.image(img_path)

# Input
if prompt := st.chat_input("Ask a math question..."):
    if not api_key:
        st.error("Please enter your API Key in the sidebar.")
        st.stop()
        
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Pass both prompt and file_data (if any)
                response_text, generated_images = st.session_state.bot.generate_response(prompt, file_data)
                
                st.markdown(response_text)
                if generated_images:
                    for img in generated_images:
                        st.image(img)
                
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": response_text,
                    "images": generated_images
                })
            except Exception as e:
                st.error(f"An error occurred: {e}")
