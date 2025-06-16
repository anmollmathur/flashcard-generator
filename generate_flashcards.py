import re
import streamlit as st
import textwrap
from transformers import pipeline
from utils.structure import extract_structured_content

# ✅ Load model only once using Streamlit's cache
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-base")

pipe = load_model()

# ✅ Chunk text into manageable parts
def chunk_text(text, max_tokens=400):
    return textwrap.wrap(text, max_tokens)

# ✅ Generate flashcards from content
def generate_flashcards(content):
    if not content.strip():
        return []

    chunks = chunk_text(content)
    flashcards = []

    for i, chunk in enumerate(chunks):
        prompt = (
            "Generate 3 flashcards from the content below.\n"
            "Each flashcard must follow this format:\n"
            "Q: <question>\nA: <answer>\n\n"
            f"Content:\n{chunk}"
        )
        try:
            output = pipe(prompt, max_new_tokens=512)[0]["generated_text"]
            parsed = parse_flashcards(output)

            if parsed:
                flashcards.extend(parsed)
            else:
                st.warning(f"⚠️ Chunk {i + 1} returned no valid flashcards.")
        except Exception as e:
            st.warning(f"❌ Error in chunk {i + 1}: {str(e)}")

    return flashcards

# ✅ Extract Q&A from output text
def parse_flashcards(output_text):
    cards = []
    matches = re.findall(r"Q:\s*(.*?)\nA:\s*(.*?)(?=\nQ:|\Z)", output_text, re.DOTALL)
    for q, a in matches:
        q, a = q.strip(), a.strip()
        if q and a:
            cards.append({
                "question": q,
                "answer": a,
                "difficulty": "Medium"
            })
    return cards
