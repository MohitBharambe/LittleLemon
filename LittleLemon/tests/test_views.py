from django.test import TestCase
from restaurant.models import Menu  
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(title="Pizza",  price=12.99, inventory = 10)
        Menu.objects.create(title="Pasta", price=9.99, inventory = 50)
        self.client = APIClient()  

    def test_get_all_menus(self):
        url = reverse('menu-items')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = [
            {'id': 1, 'title': 'Pizza', 'price': '12.99', 'inventory': 10},
            {'id': 2, 'title': 'Pasta', 'price': '9.99', 'inventory': 50},
        ]

        self.assertEqual(response.data, expected_data)
