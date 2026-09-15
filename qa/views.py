from django.shortcuts import render

# Create your views here.
from .forms import DocumentUploadForm
from .models import Document
from pypdf import PdfReader

def upload_document(request):
    extracted_text = None
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            doc = Document.objects.create(file=request.FILES['document'])
            reader = PdfReader(doc.file.path)
            extracted_text = ""
            for page in reader.pages:
                extracted_text += page.extract_text() or ""
    else:
        form = DocumentUploadForm()
    return render(request, 'qa/upload.html', {'form': form, 'text': extracted_text})