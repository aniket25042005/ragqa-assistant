import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Load models once, not on every request
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def retrieve_relevant_chunks(query, index, chunks, k=3):
    query_embedding = embedding_model.encode([query]).astype('float32')
    faiss.normalize_L2(query_embedding)
    distances, indices = index.search(query_embedding, k)
    return [chunks[idx] for idx in indices[0]]


def generate_answer(query, relevant_chunks):
    context = "\n\n".join(relevant_chunks)
    prompt = f"""Answer the question using ONLY the context below. 
If the answer isn't in the context, say "I couldn't find that in the document."

Context:
{context}

Question: {query}

Answer:"""

    response = groq_client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
    )
    return response.choices[0].message.content