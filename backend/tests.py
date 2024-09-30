from django.test import TestCase
from django.urls import reverse
from .models import PDFData
from django.core.files.uploadedfile import SimpleUploadedFile


class PDFUploadTests(TestCase):
    def setUp(self):
        self.valid_email = 'test@example.com'
        self.invalid_email = 'invalid-email'
        self.pdf_file = SimpleUploadedFile(
            name='test.pdf',
            content=b'%PDF-1.4\n%....',  # Replace with valid PDF content as needed
            content_type='application/pdf'
        )

    def test_upload_pdf_valid(self):
        """Test uploading a valid PDF file with a valid email."""
        response = self.client.post(reverse('upload_pdf'), {
            'email': self.valid_email,
            'pdf_file': self.pdf_file
        })
        
        self.assertEqual(response.status_code, 302)  # Expect a redirect after successful upload
        self.assertTrue(PDFData.objects.filter(email=self.valid_email).exists())
        
        # Check that the data was saved correctly
        pdf_data = PDFData.objects.get(email=self.valid_email)
        self.assertIsNotNone(pdf_data.extracted_nouns)  # Ensure nouns were extracted
        self.assertIsNotNone(pdf_data.extracted_verbs)   # Ensure verbs were extracted

    def test_upload_pdf_invalid_email(self):
        """Test uploading a PDF file with an invalid email."""
        response = self.client.post(reverse('upload_pdf'), {
            'email': self.invalid_email,
            'pdf_file': self.pdf_file
        })
        
        self.assertEqual(response.status_code, 200)  # Should return to the form with errors
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')

    def test_display_data(self):
        """Test displaying data after uploading a PDF."""
        # First, upload a valid PDF
        self.client.post(reverse('upload_pdf'), {
            'email': self.valid_email,
            'pdf_file': self.pdf_file
        })
        
        response = self.client.get(reverse('display_data', args=[self.valid_email]))
        self.assertEqual(response.status_code, 200)  # Expect success
        self.assertContains(response, self.valid_email)  # Check that the email is in the response

        # Check that the extracted nouns and verbs are present in the response
        pdf_data = PDFData.objects.get(email=self.valid_email)
        self.assertContains(response, pdf_data.extracted_nouns[0])  # Check first noun
        self.assertContains(response, pdf_data.extracted_verbs[0])   # Check first verb
