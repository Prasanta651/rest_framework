from django.test import TestCase
from django.urls import reverse
from api.models import Order, User

# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='user1', password='test')
        user2 = User.objects.create_user(username='user2', password='test')
        Order.objects.create(user=user1)
        Order.objects.create(user=user1)
        Order.objects.create(user=user1)
        Order.objects.create(user=user1)

    
    def test_user_order_endpoint_retrives_only_authententicated_user_orders(self):
        user = User.objects.get(username='user1')
        self.client.force_login(user)
        response = self.client.get(reverse('user_orders'))

        assert response.status_code == 200
        orders = response.json()
        self.assertTrue(all(order['user'] == user.id for order in orders))