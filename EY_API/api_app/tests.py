# tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

api_url = '/api/add/'
class AddNumbersAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_valid_input(self):
        print('-' * 50)
        print('test_valid_input')
        data = {
            "batchid": "id0101",
            "payload": [[1, 2], [3, 4]]
        }
        response = self.client.post(api_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.status_code, response.data)
        print('-' * 50)
        self.assertEqual(response.data['response'], [3, 7])

    def test_empty_input(self):
        print('-' * 50)
        print('test_empty_input')
        data = {}  # Empty payload
        response = self.client.post(api_url, data, format='json')
        print(response.status_code, response.data)
        print('-' * 50)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_batch_id(self):
        print('-' * 50)
        print('test_missing_batch_id')
        data = {"payload": [[1, 2], [3, 4]]}  # Missing batch ID
        response = self.client.post(api_url, data, format='json')
        print(response.status_code, response.data)
        print('-' * 50)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_non_integer_elements(self):
        print('-' * 50)
        print('test_non_integer_elements')
        data = {
            "batchid": "id0101",
            "payload": [[1, 2], [3, 'a']]
        }
        response = self.client.post(api_url, data, format='json')
        print(response.status_code, response.data)
        print('-' * 50)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_input_payload(self):
        print('-' * 50)
        print('test_invalid_input_payload')
        data = {
            "batchid": "id0101",
            "payload": [1, 2, 3, 4]
        }
        response = self.client.post(api_url, data, format='json')
        print(response.status_code,response.data)
        print('-' * 50)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)