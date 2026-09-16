<<<<<<< HEAD
# 📄 DocQA — RAG-Based Document Q&A Assistant

A web application that lets you upload a PDF and ask natural-language questions about it, receiving accurate, **source-grounded** answers instead of hallucinated ones. Built with a Retrieval-Augmented Generation (RAG) pipeline from scratch — no black-box frameworks, just a transparent, understandable implementation.

## ✨ Features

- **PDF Upload** — drag in any PDF document (lecture notes, reports, research papers)
- **Semantic Search** — finds the most relevant sections of your document for any question, not just keyword matches
- **Grounded Answers** — the LLM is instructed to answer *only* from retrieved context, reducing hallucination
- **Source Citations** — every answer displays the exact document excerpts used to generate it
- **Fast Inference** — powered by Groq's LPU infrastructure for near-instant responses

## 🧠 How It Works (RAG Pipeline)

```
PDF Upload
    │
    ▼
Text Extraction (pypdf)
    │
    ▼
Chunking (LangChain — 700 chars, 100 char overlap)
    │
    ▼
Embedding Generation (Sentence-Transformers: all-MiniLM-L6-v2)
    │
    ▼
Vector Storage (FAISS index, saved per document)
    │
    ▼
[User asks a question]
    │
    ▼
Query Embedding → Similarity Search (top-k chunks)
    │
    ▼
Context + Question → LLM (Groq / OpenAI GPT-OSS)
    │
    ▼
Grounded Answer + Source Excerpts displayed to user
```

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Embeddings | Sentence-Transformers (`all-MiniLM-L6-v2`) |
| Vector Store | FAISS |
| Text Splitting | LangChain Text Splitters |
| PDF Parsing | pypdf |
| LLM Inference | Groq API |
| Frontend | Django Templates, vanilla CSS |

## 📂 Project Structure

```
ragqa-assistant/
├── manage.py
├── ragqa/                  # Django project config
│   ├── settings.py
│   └── urls.py
├── qa/                      # Main app
│   ├── models.py            # Document model
│   ├── views.py              # Upload + Q&A logic
│   ├── rag_utils.py          # Embedding, retrieval, generation
│   ├── forms.py
│   └── templates/qa/
│       ├── base.html
│       ├── upload.html
│       └── ask.html
├── notebooks/
│   └── rag_experiments.ipynb # Prototyping & validation notebook
├── media/                    # Uploaded PDFs + FAISS indexes (gitignored)
├── requirements.txt
└── .env                      # API keys (gitignored)
```

## 🚀 Getting Started

### Prerequisites
- Python 3.11 (recommended — newer versions may lack pre-built wheels for some ML dependencies)
- A free [Groq API key](https://console.groq.com)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ragqa-assistant.git
   cd ragqa-assistant
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root:
   ```
   GROQ_API_KEY=your_key_here
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000/` in your browser.

## 📖 Usage

1. Upload a PDF document on the home page
2. Once processed, you'll be taken to the Q&A page for that document
3. Ask any question related to the document's content
4. View the generated answer along with the exact source excerpts it was based on

## 🧪 Development Notes

Chunking and embedding logic was first prototyped and validated in `notebooks/rag_experiments.ipynb` before being integrated into the Django application — allowing for quick iteration on chunk size, overlap, and retrieval quality before committing to production code.

## 🔮 Future Improvements

- [ ] Multi-document support with per-document filtering
- [ ] Conversational memory (multi-turn Q&A)
- [ ] Support for additional file types (.docx, .txt)
- [ ] Confidence scoring alongside answers
- [ ] Deployed live demo

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙋 Author

**Aniket Kumar Singh**
B.Tech CSE (AI & ML) — JSS Academy of Technical Education
[GitHub](https://github.com/aniket25042005) • [LinkedIn](#)
=======

>>>>>>> 299b1bdd2cbd199f3416f18b3102217c455b0ee3
