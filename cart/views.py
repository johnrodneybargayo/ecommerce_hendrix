from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CartItem, Cart, Product
from .serializers import CartItemSerializer, ProductSerializer, CartSerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class AddToCartAPIView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]  # Ensure user is authenticated

    def create(self, request, *args, **kwargs):
        # Extract product_id and quantity from the request data
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        # Validate that product_id is provided
        if not product_id:
            return Response({"error": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Retrieve the product using the provided product_id
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        # Get or create the user's cart
        cart, _ = Cart.objects.get_or_create(user=request.user if request.user.is_authenticated else None)

        # Get or create the cart item for the product
        cart_item, created = CartItem.objects.get_or_create(
            product=product,
            cart=cart,
            defaults={'quantity': quantity}
        )

        # If the cart item already exists, update the quantity
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        # Serialize the cart item and return the response
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CartDetailAPIView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
   # permission_classes = [IsAuthenticated]  # Ensure user is authenticated

    def get_object(self):
        # Retrieve the cart associated with the authenticated user
        return self.request.user.cart
