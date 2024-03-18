from django.urls import path
from .views import ProductListAPIView, AddToCartAPIView, CartDetailAPIView

urlpatterns = [
    path('api/products/', ProductListAPIView.as_view(), name='product-list'),
    path('add/', AddToCartAPIView.as_view(), name='add-to-cart'),
    path('cart/detail/', CartDetailAPIView.as_view(), name='cart-detail'),
]
