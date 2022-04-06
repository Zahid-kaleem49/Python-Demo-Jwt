from email.policy import HTTP
import json
import math
from rest_framework.test import APIClient, APITestCase
from rest_framework import status


class TestUserApi(APITestCase):
    """
    Tests for User Authentication Apis
    """

    def client(self):
        return APIClient()

    def jwt_headers(self):
        user = self.add_default_user()
        user_data = {
            "first_name": "Testing",
            "last_name": "account",
            "username": "testingaccount",
            "email": "testingaccount@gmail.com",
            "password": "testingaccount"
        }
        response = self.client.post('/login', data=user_data)
        response_data = response.json()
        jwt_token = response_data['access']
        return self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt_token)

    def test_endpoint(self):
        """
        Test Login api with valid data.
        """
        response = self.client.get('/api/Test-test')

        assert response.status_code == status.HTTP_200_OK

    def add_default_user(self):
        # just making it bulletproof
        user_data = {
            "first_name": "Testing",
            "last_name": "account",
            "username": "testingaccount",
            "email": "testingaccount@gmail.com",
            "password": "testingaccount"
        }
        response = self.client.post('/api/create-user', data=user_data)
        return response.json()

    def add_default_product(self):
        data = {
            "product_name": "choco",
            "product_price": "20",
            "product_quantity": 100
        }
        return self.client.post(
            '/api/cart-item/', headers=self.jwt_headers(), data=data)

    def test_get_user_login_api_with_valid_data(self):
        """
        Test Login api with valid data.
        """
        user = self.add_default_user()
        data = {
            "username": "testingaccount",
            "password": "testingaccount"
        }
        response = self.client.post('/login', data=data)
        assert response.status_code == status.HTTP_200_OK

    def test_get_user_login_api_with_invalid_data(self):
        """
        Test Login api with Invalid data.
        """
        user = self.add_default_user()
        data = {
            "username": "test",
            "password": "test"
        }
        response = self.client.post('/login', data=data)
        response_data = response.json()

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response_data['detail'] == 'No active account found with the given credentials'

    def test_get_user_register_api_with_invalid_data(self):
        """
        Test register api with Invalid data.
        """
        user_data = {
            'username': 'test_admin',

        }
        response = self.client.post('/api/create-user', data=user_data)
        response_data = response.json()
        print(response_data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response_data['Error']['password'][0] == "This field is required."

    def test_get_user_register_api_with_valid_data(self):
        data = {
            "first_name": "Testing",
            "last_name": "account",
            "username": "testsingaccount",
            "email": "qtestingaccount@gmail.com",
            "password": "testingaccount"
        }
        response = self.client.post('/api/create-user', data=data)
        response_data = response.json()
        assert response.status_code == status.HTTP_201_CREATED
        assert response_data["message"] == "User Registered"

    def test_get_product_with_valid_url(self):

        response = self.add_default_product()

        response = self.client.get(
            '/api/cart-item/1', headers=self.jwt_headers())
        response_data = response.json()
        print(response)
        assert response.status_code == status.HTTP_200_OK
        assert response_data["status"] == "success"

    def test_get_product_with_invalid_url(self):

        data = self.add_default_product()
        response = self.client.get('/api/cart-item/300')
        response_data = response.json()
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response_data["data"] == "no data found"

    def test_post_product_with_valid_data(self):
        data = {
            "product_name": "choco",
            "product_price": "20",
            "product_quantity": 100
        }
        response = self.client.post(
            '/api/cart-item/', headers=self.jwt_headers(), data=data)
        response_data = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert response_data["status"] == "success"

    def test_update_product_with_valid_data_and_url(self):
        data = self.add_default_product()
        data = {"product_name": "choco",
                "product_price": "20",
                "product_quantity": 100
                }
        response = self.client.patch(
            '/api/cart-item/1', headers=self.jwt_headers(), data=data)
        response_data = response.json()
        print(response)
        assert response.status_code == status.HTTP_200_OK
        assert response_data["status"] == "success"

    def test_update_product_with_invalid_data(self):
        data = self.add_default_product()
        data = {"product_name": "choco",
                "product_price": "zahid",
                "product_quantity": 100
                }
        response = self.client.patch(
            '/api/cart-item/1', headers=self.jwt_headers(), data=data)
        response_data = response.json()
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response_data["data"]["product_price"][0] == "A valid number is required."

    def test_delete_product_with_valid_url(self):
        data = self.add_default_product()
        response = self.client.delete('/api/cart-item/1')
        assert response.status_code == status.HTTP_200_OK
