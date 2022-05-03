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
    def test_all_posts(self):
        response = self.client.get(path='/api/v1/posts/all/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ReadPostTestCase(APITestCase):
    def setUp(self):
        self.client.post(path=register_url, data=register_data, format='json')
        response = self.client.post(login_url, data=login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])

    def test_read_post(self):
        data = {
            "post_id": 1,
            "flagged_post": True,

        }
        response = self.client.post('/api/v1/posts/flag_post_as_readed/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class PostsFromFavUsersTestCase(APITestCase):
    def setUp(self):
        self.client.post(path=register_url, data=register_data, format='json')
        response = self.client.post(login_url, data=login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])

    def test_posts_from_fav_users(self):
        self.client.get('/api/v1/posts/posts_from_fav_users/')


class ReadedPostsTestCase(APITestCase):
    def setUp(self):
        self.client.post(path=register_url, data=register_data, format='json')
        response = self.client.post(login_url, data=login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])

    def test_readed_posts_filter(self):
        self.client.get('/api/v1/posts/readed_posts/?read_posts')

    def test_readed_posts_no_filter(self):
        self.client.get('/api/v1/posts/readed_posts/')

