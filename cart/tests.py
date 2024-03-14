from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Product, CartItem

class AddToCartAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(name='Test Product', price=10.0)

    def test_add_to_cart(self):
        url = reverse('add_to_cart')
        data = {'product_id': self.product.id, 'quantity': 2}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CartItem.objects.count(), 1)
        cart_item = CartItem.objects.first()
        self.assertEqual(cart_item.product, self.product)
        self.assertEqual(cart_item.quantity, 2)
