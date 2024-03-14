from django.urls import path
from .views import ProductList, AddToCart

urlpatterns = [
    path('api/products/', ProductList.as_view(), name='product-list'),
    path('add-to-cart/', AddToCart.as_view(), name='add_to_cart'), 
]
