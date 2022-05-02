from rest_framework.test import APITestCase
from rest_framework import status

register_data = {
    "user": {
        "username": "user7",
        "email": "user7@user.user",
        "password": "qweasdzxc"
    }
}
register_url = '/api/v1/auth/user/'

login_data = {
    "user": {
        "email": "user7@user.user",
        "password": 'qweasdzxc'
    }
}
login_url = '/api/v1/auth/user/login/'


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


class CreatePostTestCase(APITestCase):
    def setUp(self):
        self.client.post(path=register_url, data=register_data, format='json')
        response = self.client.post(login_url, data=login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])

    def test_create_post(self):
        data = {
            "title": "some title",
            "text": "some text"
        }
        response = self.client.post(path='/api/v1/posts/add/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class AllPostsTestCase(APITestCase):
    def setUp(self):
        self.client.post(path=register_url, data=register_data, format='json')
        response = self.client.post(login_url, data=login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])

    def test_all_posts(self):
        response = self.client.get(path='/api/v1/posts/all/')
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

    # def test_fix_fav_user(self):
    #     data = {
    #         "secondary_user_id": 1,
    #         "favorite_user": False
    #     }
    #     response = self.client.patch(path='/api/v1/auth/users/favorite_user_update/', data=data, format='json')
    #     print(response.json())
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
