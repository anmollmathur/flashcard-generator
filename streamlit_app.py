import streamlit as st
from dotenv import load_dotenv
import os
from utils.preprocess import extract_content_from_pdf
from transformers import pipeline
import textwrap

# Load environment variables from .env
load_dotenv()

# Cache the model to avoid reloading
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-base")

pipe = load_model()

#  Chunk content to avoid token limit issues
def chunk_text(text, max_tokens=450):
    return textwrap.wrap(text, max_tokens)

#  Generate flashcards in chunks
def generate_flashcards(content):
    if not content.strip():
        return "No content provided."

    chunks = chunk_text(content)
    flashcards = []

    for i, chunk in enumerate(chunks):
        prompt = (
            "Create flashcards from the following content.\n"
            "Format each flashcard as:\n"
            "Q: Question?\nA: Answer.\n\n"
            f"{chunk}"
        )
        try:
            output = pipe(prompt, max_new_tokens=256)[0]["generated_text"]
            flashcards.append(f"Chunk {i+1}:\n{output}")
        except Exception as e:
            flashcards.append(f"Error in chunk {i + 1}: {str(e)}")

    return "\n\n".join(flashcards)

#  Streamlit UI
st.title("📘 Flashcard Generator")

uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())
        content = extract_content_from_pdf("temp.pdf")

    elif uploaded_file.type == "text/plain":
        content = uploaded_file.read().decode("utf-8")
    else:
        content = ""

    if content:
        st.info("Generating flashcards... Please wait.")
        flashcards_output = generate_flashcards(content)
        st.subheader("📝 Generated Flashcards")
        st.text_area("Output", flashcards_output, height=400)
    else:
        st.error("❌ Failed to extract content from file.")

