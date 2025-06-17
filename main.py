from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv
from utils.preprocess import extract_structured_content  # Make sure this function is implemented

# Load API key
load_dotenv()
API_TOKEN = os.getenv("HF_TOKEN")  # .env should contain HF_TOKEN=your_huggingface_token

# Initialize client
client = InferenceClient(model="HuggingFaceH4/zephyr-7b-beta", token=API_TOKEN)

# Chunk long content into small parts
def chunk_text(text, max_words=300):
    words = text.split()
    return [" ".join(words[i:i+max_words]) for i in range(0, len(words), max_words)]

#  Generate flashcards from content with structured section support
def generate_flashcards(content):
    if not content.strip():
        return []

    # Step 1: Extract structured sections
    structured = extract_structured_content(content)
    all_flashcards = []

    # Step 2: Iterate through each section
    for section in structured:
        section_heading = section["heading"]
        section_text = section["content"]
        chunks = chunk_text(section_text)

        for i, chunk in enumerate(chunks):
            prompt = (
                f"Generate flashcards from the following educational content under the heading '{section_heading}'.\n"
                "For each flashcard, assign a difficulty level (Easy, Medium, Hard).\n"
                "Format:\nQ: ...\nA: ...\nDifficulty: ...\n\n"
                f"Content:\n{chunk}"
            )
            try:
                response = client.text_generation(
                    prompt,
                    generate_kwargs={"max_new_tokens": 256, "temperature": 0.7},
                    details=False,
                    stream=False,
                )
                all_flashcards.append({
                    "section": section_heading,
                    "raw_output": response.strip()
                })
            except Exception as e:
                all_flashcards.append({
                    "section": section_heading,
                    "raw_output": f"Error from section '{section_heading}' chunk {i+1}: {str(e)}"
                })

    return all_flashcards
