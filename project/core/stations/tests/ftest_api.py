from django.test import TestCase

from stations.models import Station, Net
from tools.urls import reverse_api
from tools.tests import FunctionalTestCase


class StationTestCase(FunctionalTestCase, TestCase):
    def test_list_station(self):
        user = self.create_user(username='chuck d')
        client = self.get_client(user)
        stations = [
            Station.objects.create(owner=user, name='hey'),
            Station.objects.create(owner=user, name='sugar'),
            Station.objects.create(owner=user, name='whatsup')
        ]
        response = client.get(reverse_api('stations:station-list'))

        # assert we got our list
        self.assertEqual(response.status_code, 200)

        # assert the payload result has three items
        payload = response.json()
        self.assertEqual(len(payload['results']), 3)


    def test_create_station(self):
        user = self.create_user(username='boner')
        client = self.get_client(user)
        response = self.api_post(client, reverse_api('stations:station-list'), {})
        # no empty data!
        self.assertEqual(response.status_code, 400)

        data = {
            'name': 'wang',
        }
        response = self.api_post(client, reverse_api('stations:station-list'), data)
        self.assertEqual(response.status_code, 201)

        # name is required unique, doing it again should fail. 
        response = self.api_post(client, reverse_api('stations:station-list'), data)
        self.assertEqual(response.status_code, 400)