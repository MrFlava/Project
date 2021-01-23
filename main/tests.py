from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Portfolio

# Create your tests here.


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
                'email': 'fakemail@gmail.com',
                'username': 'User_1',
                'password': 'aaa24rcd@'
                }
        response = self.client.post("auth/users/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProfileViewTestCase(APITestCase):

    profile_url = 'auth/users/me'
    username_url = 'auth/users/set_username/'
    logout_url = 'auth/users/logout'

    def setUp(self):
        self.user = User.objects.create_user(username='User_1',
                                             email='fakemail@gmail.com',
                                             password='aaa24rcd@')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_profile_authenticated(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_set_username(self):
        data = {
            'new_username': 'Userr_1',
            'current_password': 'aaa24rcd@'
        }
        response = self.client.post(self.username_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_delete(self):
        response = self.client.delete(self.profile_url+'/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_logged_out(self):
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PortfolioViewTestCase(ProfileViewTestCase):

    portfolios_url = 'main/portfolio/'

    def test_profile_list_portfolios(self):
        response = self.client.get(self.portfolios_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_create_portfolio(self):
        data = {
            'name': 'Portfolio1',
            'description': 'Lorem Ipsum'
        }
        response = self.client.post(self.portfolios_url+'create', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_update_portfolio(self):
        new_portfolio = Portfolio.objects.create(name='Portfolio2', description='Lorem Ipsummm',
                                                 profile_id=self.user.pk)
        data = {
            'name': 'Portfolioo2',
            'description': 'Lorem Ipsummm'
        }

        response = self.client.patch(reverse('update-portfolio', kwargs={'pk': 1}), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ImageViewTestCase(ProfileViewTestCase):

    images_url = 'images/'

    def test_profile_list_images(self):
        response = self.client.get(self.images_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_create_image(self):
        data = {
            'name': 'Portfolio1',
            'description': 'Lorem Ipsum',
            'image': 'path/to/file.png',
            'portfolio_id': 1

        }

        response = self.client.post(self.images_url+'create', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
