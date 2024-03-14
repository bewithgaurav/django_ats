from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Candidate

class CandidateAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_candidate(self):
        url = '/candidates/'
        data = {
            "name": "John Doe",
            "age": 25,
            "gender": "Male",
            "years_of_exp": 4,
            "phone_number": "1234567890",
            "email": "john@example.com",
            "current_salary": 50000,
            "expected_salary": 60000,
            "status": "Applied"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Candidate.objects.count(), 1)
        self.assertEqual(Candidate.objects.get().name, 'John Doe')

    def test_name_search(self):
        url = '/name_search/Ajay%20Kumar%20yadav'
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
