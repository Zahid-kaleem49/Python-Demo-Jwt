from django.test import TestCase

# Create your tests here.

import math
import pytest
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


def testsquare():
    # sourcery skip: equality-identity, simplify-numeric-comparison
    num = 7
    assert 7*7 == 49


def testequality():
   assert 11 == 11


class TestUserApi(APITestCase):

    @pytest.fixture
    def client(self):
        return APIClient()

    def test_get_user_login_api_with_valid_data(self):
        #    """
        #     Test Login api with valid data.
        #     """
        #    self.add_default_user()
       data = {
           "username": "test_admin",
           "password": "Admin123@"
       }
       response = self.client.post('/login/', data=data)
       assert response.status_code == status.HTTP_200_OK
