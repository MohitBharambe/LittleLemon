from restaurant.models import Menu
from django.test import TestCase

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Lemonade', price=7.0, inventory=50)
        self.assertEqual(str(item), 'Lemonade : 7.0')
