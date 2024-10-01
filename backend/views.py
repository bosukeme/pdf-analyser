
import re
from pypdf import PdfReader
import nltk
from django.shortcuts import render, redirect
from .forms import PDFUploadForm
from .models import PDFData

nltk.data.path.append('/tmp')
nltk.download('punkt', download_dir='/tmp')
nltk.download('averaged_perceptron_tagger', download_dir='/tmp')


def extract_nouns_and_verbs(text):
    words = nltk.word_tokenize(text)
    tagged_words = nltk.pos_tag(words)
    nouns = [word for word, pos in tagged_words if pos.startswith('NN')]
    verbs = [word for word, pos in tagged_words if pos.startswith('VB')]
    return nouns, verbs


def clean_text(extracted_text):

    gibberish_tokens = [
        '•', '-', '—', '–', '❖', '___', '–', '’', '“', '”', 'i', 'ii', 'iii'
    ]

    cleaned_words = []

    for word in extracted_text:
        word = re.sub(r'[^a-zA-Z@.]+', '', word)

        if (word and
                word not in gibberish_tokens and
                len(word) > 1 and
                not word.isdigit() and
                not all(c == '.' for c in word)):
            cleaned_words.append(word)

    return cleaned_words


def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            pdf_file = request.FILES['pdf_file']

            pdf_reader = PdfReader(pdf_file)
            pdf_text = ""
            for page_num in range(len(pdf_reader.pages)):
                pdf_text += pdf_reader.pages[page_num].extract_text()

            nouns, verbs = extract_nouns_and_verbs(pdf_text.lower())

            cleaned_nouns = clean_text(nouns)
            cleaned_verbs = clean_text(verbs)

            # Save to MongoDB using MongoEngine
            PDFData.objects(email=email).update_one(
                set_on_insert__email=email,
                set__extracted_nouns=cleaned_nouns,
                set__extracted_verbs=cleaned_verbs,
                set__pdf_name=str(pdf_file),
                upsert=True
            )

            return redirect('display_data', email=email)
    else:
        form = PDFUploadForm()

    return render(request, 'upload.html', {'form': form})


def display_data(request, email):
    data = PDFData.objects.get(email=email)
    return render(request, 'display.html', {'data': data})


def home(request):
    return render(request, 'index.html')
