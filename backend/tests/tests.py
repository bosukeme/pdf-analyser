import os
from django.test import TestCase
from django.urls import reverse
from backend.models import PDFData
from django.core.files.uploadedfile import SimpleUploadedFile
from mongoengine import connect, disconnect, get_connection
from dotenv import load_dotenv

load_dotenv()


class PDFUploadTests(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.connection_uri = os.environ.get("MONGO_URI")
        
        if cls.connection_uri:
            try:
                connect(db='test_database', host=cls.connection_uri, ssl=True, retryWrites=True)
            except Exception as e:
                raise ValueError("Failed to establish MongoDB connection") from e
        else:
            raise ValueError("MONGO_URI environment variable not set.")

    @classmethod
    def tearDownClass(cls):
        try:
            conn = get_connection()
            if conn:
                conn.drop_database('test_database')
            disconnect()
        except Exception as e:
            print(f"Error during teardown: {str(e)}")
        
        super().tearDownClass()

    def setUp(self):
        self.conn = get_connection()
        if not self.conn:
            raise ConnectionError("No active connection found")
        
        self.upload_url = reverse('upload_pdf')
        
        self.valid_email = 'test@example.com'
        self.invalid_email = 'test_example'
        
        pdf_file_path = os.path.join(os.path.dirname(__file__), 'test_files', 'test.pdf')

        # Check if the file exists
        if not os.path.exists(pdf_file_path):
            raise FileNotFoundError(f"Test PDF file not found at: {pdf_file_path}")

        # Create a SimpleUploadedFile object
        with open(pdf_file_path, 'rb') as pdf_file:
            self.valid_pdf = SimpleUploadedFile(
                name='test.pdf',
                content=pdf_file.read(),
                content_type='application/pdf'
            )

    def test_upload_pdf_valid(self):
        response = self.client.post(self.upload_url, {
            'email': self.valid_email,
            'pdf_file': self.valid_pdf
        })

        self.assertEqual(response.status_code, 302)
        self.created_record = PDFData.objects(email=self.valid_email).first()
        self.assertIsNotNone(self.created_record)
        self.assertEqual(self.created_record.email, self.valid_email)

    def test_display_data(self):

        if not hasattr(self, 'created_record'):
            self.skipTest("No PDFData record found. Ensure test_upload_pdf_valid runs first.")

        display_url = reverse('display_data', kwargs={'email': self.valid_email})
        response = self.client.get(display_url)

        # Check if the response is 200 OK and contains the data
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.created_record.email)
        self.assertContains(response, self.created_record.extracted_nouns)
        self.assertContains(response, self.created_record.extracted_verbs)
        self.assertContains(response, self.created_record.pdf_name)


    def test_upload_pdf_invalid_email(self):        
        response = self.client.post(self.upload_url, {
            'email': self.invalid_email,
            'pdf_file': self.valid_pdf
        })

        self.assertNotEqual(response.status_code, 302)
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')

