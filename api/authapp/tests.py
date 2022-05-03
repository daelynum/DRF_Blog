from rest_framework.test import APITestCase
from rest_framework import status

from postapp.tests import register_url, register_data, login_url, login_data


class RegistrationTestCase(APITestCase):
    def test_registration(self):
        response = self.client.post(path=register_url, data=register_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginTestCase(APITestCase):
    def test_user_authenticated(self):
        self.client.post(path=register_url, data=register_data, format='json')
        response = self.client.post(login_url, data=login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ShowUsersTestCase(APITestCase):
    def test_all_users(self):
        response = self.client.get(path='/api/v1/auth/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_all_users_with_filter(self):
        response = self.client.get(path='/api/v1/auth/users/?count_of_posts')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class FavUserTestCase(APITestCase):
    def setUp(self):
        self.client.post(path=register_url, data=register_data, format='json')
        response = self.client.post(login_url, data=login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])

    def test_add_fav_user(self):
        data = {
            "secondary_user_id": 1,
            "favorite_user": True
        }
        response = self.client.post(path='/api/v1/auth/users/favorite_user/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



