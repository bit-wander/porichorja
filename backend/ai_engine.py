import base64
import os
import pandas as pd
import numpy as np
import faiss
from dotenv import load_dotenv
from ollama import Client
from sentence_transformers import SentenceTransformer

load_dotenv()

# Data paths
DATA_DIR = 'backend/data/'
df = pd.read_csv(os.path.join(DATA_DIR, 'clean_agriculture_qa.csv'))

_index = None
_embeddings = None

def get_faiss_index():
    global _index
    if _index is None:
        _index = faiss.read_index(os.path.join(DATA_DIR, 'agri_index.faiss'))
    return _index

def get_embeddings():
    global _embeddings
    if _embeddings is None:
        _embeddings = np.load(os.path.join(DATA_DIR, 'agri_embeddings.npy'))
    return _embeddings

# Models
embedding_model = SentenceTransformer("intfloat/multilingual-e5-small")

# Ollama Client
ollama_client = Client(
    host="https://ollama.com",
    headers={'Authorization': 'Bearer ' + os.getenv('OLLAMA_API_KEY')}
)

def retrieve_context(query, k=3):
    query_embedding = embedding_model.encode(
        ["query: " + query],
        convert_to_numpy=True
    )
    idx = get_faiss_index()
    distance, indices = idx.search(query_embedding, k)
    results = df.iloc[indices[0]]
    return results

def build_prompt(query, retrieved_docs):
    context = ""
    for i, row in retrieved_docs.iterrows():
        context += f"\nপ্রশ্ন: {row['question']}\nউত্তর: {row['answer']}\n"

    prompt = f"""
আপনি একজন কৃষি বিশেষজ্ঞ।

নিচের তথ্য ব্যবহার করে প্রশ্নের উত্তর দিন।

তথ্য:
{context}

ব্যবহারকারীর প্রশ্ন:
{query}

বাংলায় সংক্ষিপ্ত ও পরিষ্কার উত্তর দিন।
"""
    return prompt

def generator(prompt, image_url=None):
    messages = [{"role": "user", "content": prompt}]

    # images = []
    # if image_url:
    #     # Extract base64 part if it's a data URL
    #     if image_url.startswith("data:"):
    #         base64_data = image_url.split(",")[1]
    #         images.append(base64_data)
    #     else:
    #         images.append(image_url)

    response = ollama_client.chat(
        model='gemma3:4b',
        messages=messages,
        # images=images if images else None,
        stream=False
    )
    return response.message.content

def rag_answer(query, image_url=None):
    docs = retrieve_context(query)
    prompt = build_prompt(query, docs)
    response = generator(prompt, image_url=image_url)
    return response

def get_diagnosis(image_path, user_text_bangla):
    image_url = None
    if image_path:
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
        image_url = f"data:image/jpeg;base64,{encoded_image}"

    response = rag_answer(user_text_bangla, image_url=image_url)
    return response