from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class EventTests(APITestCase):
    def test_get_event_list(self):
        """
        Ensure we can get list of events.
        """
        url = reverse('api:event-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        