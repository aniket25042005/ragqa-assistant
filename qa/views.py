from django.shortcuts import render
import json
import faiss
import numpy as np
from django.shortcuts import get_object_or_404
from langchain_text_splitters import RecursiveCharacterTextSplitter
from .rag_utils import embedding_model, retrieve_relevant_chunks, generate_answer
from .forms import DocumentUploadForm
from .models import Document
from pypdf import PdfReader
from django.shortcuts import redirect


# Create your views here.
def upload_document(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            doc = Document.objects.create(file=request.FILES['document'])

            # Extract text
            reader = PdfReader(doc.file.path)
            text = "".join(page.extract_text() or "" for page in reader.pages)

            # Chunk
            splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=100)
            chunks = splitter.split_text(text)

            # Embed + index
            embeddings = embedding_model.encode(chunks).astype('float32')
            faiss.normalize_L2(embeddings)
            index = faiss.IndexFlatIP(embeddings.shape[1])
            index.add(embeddings)

            # Save index + chunks
            index_path = f"media/indexes/doc_{doc.id}.faiss"
            faiss.write_index(index, index_path)
            doc.chunks_json = json.dumps(chunks)
            doc.index_path = index_path
            doc.save()

            return redirect('ask_question', doc_id=doc.id)
    else:
        form = DocumentUploadForm()
    return render(request, 'qa/upload.html', {'form': form})


def ask_question(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    answer = None
    source_chunks = None

    if request.method == 'POST':
        query = request.POST.get('query')
        chunks = json.loads(document.chunks_json)
        index = faiss.read_index(document.index_path)

        source_chunks = retrieve_relevant_chunks(query, index, chunks, k=3)
        answer = generate_answer(query, source_chunks)

    return render(request, 'qa/ask.html', {
        'document': document,
        'answer': answer,
        'source_chunks': source_chunks,
    })

