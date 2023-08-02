from django.shortcuts import render

from rest_framework import generics
from .models import Customer, Product
from .serializers import CustomerSerializer, ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    

@csrf_exempt
@api_view(['POST'])
def activate_deactivate_product(request, product_id):
    print("aaaaaaaaaaaaaaaaa")
    try:
        product = Product.objects.get(pk=product_id)
        print("zzzzzzzzzzzz")
    except Product.DoesNotExist:
        print("ssssssssss")
        return Response({"error": "Product not found"}, status=404)

    print("cccccccccccccccccc")
    
    print("Current date:", datetime.now().date())
    print("Product created date:", product.created_at.date())
    
    if timezone.now() - product.created_at >= timedelta(minutes=1):
        print("fffffffffffffffffffffffffff")
        product.is_active = not product.is_active
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxx")
        product.save()
        print("yyyyyyyyyyyyyyyyy")
        return Response({"message": "Product activated/deactivated successfully."}, status=200)
    else:
        return Response({"error": "Product can only be deactivated if registered before 1 minut."}, status=400)