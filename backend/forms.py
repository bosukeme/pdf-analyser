from django import forms


class PDFUploadForm(forms.Form):
    email = forms.EmailField()
    pdf_file = forms.FileField()
