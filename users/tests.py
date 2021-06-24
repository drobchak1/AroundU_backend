from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import User

class UsersTests(APITestCase):
    def test_get_users_list(self):
        """
        Ensure we can get list of users.
        """
        url = reverse('users')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_api_jwt(self):
        """
        Ensure we can create user and create event using JWT-token.
        """
        url = reverse('token_obtain_pair')
        u = User.objects.create_user(username='user', email='user@foo.com', password='pass')
        u.is_active = False
        u.save()

        resp = self.client.post(url, {'email':'user@foo.com', 'password':'pass'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        u.is_active = True
        u.save()

        resp = self.client.post(url, {'username':'user', 'password':'pass'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        print(resp.data)
        self.assertTrue('access' in resp.data)
        self.assertTrue('refresh' in resp.data)
        token = resp.data['access']

        verification_url = reverse('api:event-list')
        

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + 'abc')
        resp = client.post(verification_url,     {
            "title": "event24",
            "description": "jfgjgfjfg",
            "event_type": "PRI",
            "city": "Kyiv",
            "address": "dfsfsdfsdf",
            "date_and_time_of_event": "2021-07-30T15:09:00Z"
        })
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        resp = client.post(verification_url, {
            "title": "event24",
            "description": "jfgjgfjfg",
            "event_type": "PRI",
            "city": "Kyiv",
            "address": "dfsfsdfsdf",
            "date_and_time_of_event": "2021-07-30T15:09:00Z"
        })
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)


    def test_register(self):
        """
        Ensure we can register user
        """
        url = reverse('auth_register')
        resp = self.client.post(url,     {
            "username": "user3",
            "password": "lol1lol1",
            "password2": "lol1lol1",
            "email": "lol@gmail.com",
            "first_name": "",
            "last_name": "",
            "bio": ""
        })
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
