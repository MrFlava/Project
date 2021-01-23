from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from rest_framework.test import force_authenticate

from .models import Portfolio, Image, Comment

# Create your tests here.


class AuthTestSetUp(APITestCase):
    def setUp(self):
        self.register_url = 'auth/users/'
        self.login_url = 'auth/token/login/'

        self.user_data = {
            'email': 'fakemail@gmail.com',
            'username': 'User_1',
            'password': 'aaa24rcd@'
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()


class TestViews(AuthTestSetUp):

    def test_registration(self):
        result = self.client.post(self.register_url, self.user_data)
        self.assertEqual(result.status_code, 200)

    def test_login(self):
        result = self.client.post(self.login_url, self.user_data)
        self.assertEqual(result.status_code, 200)

    def test_logout(self):
        result = self.client.logout(self.login_url, self.user_data)
        self.assertEqual(result.status_code, 200)