from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import CartItem
from product.models import Product
from .serializers import CartItemSerializer, ProductSerializer  # Import ProductSerializer

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class AddToCart(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def create(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Check if the product is already in the cart
        cart_item, created = CartItem.objects.get_or_create(product=product)
        
        # If the product is already in the cart, increment quantity
        if not created:
            cart_item.quantity += int(quantity)
            cart_item.save()
        
        return Response({"message": "Product added to cart successfully"}, status=status.HTTP_200_OK)
