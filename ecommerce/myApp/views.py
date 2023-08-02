from rest_framework import generics
from .models import Customer, Product
from .serializers import CustomerSerializer, ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.

#view for customer creation
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


#view for customer CRUD operations
class CustomerRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


#view for product creation
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


#view for customer CRUD operations
class ProductRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
    
#view for deactivating product 
@csrf_exempt
@api_view(['POST'])
def deactivate_product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)
    
    
    # Check if the product is already deactivated
    if not product.is_active:
        return Response({"error": "Product is already deactivated."}, status=400)
    
    
    #Check if the product is registered two months ago or more
    if timezone.now() - product.created_at >= timedelta(minutes=1):
        product.is_active = not product.is_active
        product.save()
        return Response({"message": "Product deactivated successfully."}, status=200)
    else:
        return Response({"error": "Product can only be deactivated if registered before 2 months."}, status=400)
    
    

#view for activate the product   
@csrf_exempt
@api_view(['POST'])
def activate_product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)

    # Check if the product is already activated
    if product.is_active:
        return Response({"error": "Product is already activated."}, status=400)
    else: 
        product.is_active = True
        product.save()
        return Response({"message": "Product activated successfully."}, status=200)