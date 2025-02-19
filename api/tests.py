from django.test import TestCase
from django.urls import reverse
from api.models import Order, User
from rest_framework import status

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

        assert response.status_code == status.HTTP_200_OK
        orders = response.json()
        self.assertTrue(all(order['user'] == user.id for order in orders))

    def test_user_order_list_unauthententicated(self):
        response = self.client.get(reverse('user_orders'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
