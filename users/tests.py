from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import User
from events.models import Event

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
        Ensure we can register user and create event using JWT-token.
        """
        url = reverse('token_obtain_pair')
        url_register = reverse('auth_register')
        resp = self.client.post(url_register,     {
            "username": "user",
            "password": "lol1lol1",
            "password2": "lol1lol1",
            "email": "lol@gmail.com",
            "first_name": "",
            "last_name": "",
            "bio": ""
        })
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'user')

        resp = self.client.post(url, {'email':'lol@gmail.com', 'password':'lol1lol1'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)


        resp = self.client.post(url, {'username':'user', 'password':'lol1lol1'}, format='json')
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
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Event.objects.get().title, 'event24')


    def test_update(self):
        """
        Ensure we can update user
        """
        url_register = reverse('auth_register')
        resp = self.client.post(url_register,     {
            "username": "user",
            "password": "lol1lol1",
            "password2": "lol1lol1",
            "email": "lol@gmail.com",
            "first_name": "",
            "last_name": "",
            "bio": ""
        })
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        url_auth = reverse('token_obtain_pair')
        resp = self.client.post(url_auth, {'username':'user', 'password':'lol1lol1'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        token = resp.data['access']

        url_upd = reverse('auth_update_profile', kwargs={'pk': 1})
        print(url_upd)

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        resp = client.patch(url_upd,     {
            "username": "user3",
            "email": "lol@gmail.com",
            "first_name": "",
            "last_name": "",
            "image": "",
            "bio": "",
            "city": "",
            "phone": ""
        })
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get().username, 'user3')
