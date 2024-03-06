from django.urls import path
from .views import ShoppingCartView, AddToCartView

urlpatterns = [
    path('shopping-cart/', ShoppingCartView.as_view(), name='shopping-cart'),
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    # Add more URL patterns as needed
]
