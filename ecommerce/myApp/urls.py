from django.urls import path
from .views import (
    CustomerListCreateView,
    CustomerRetrieveUpdateDeleteView,
    ProductListCreateView,
    ProductRetrieveUpdateDeleteView,
    deactivate_product,activate_product,
)

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    
    
    
    path('customers/<int:pk>/', CustomerRetrieveUpdateDeleteView.as_view(), name='customer-retrieve-update-delete'),
    path('products/<int:pk>/', ProductRetrieveUpdateDeleteView.as_view(), name='product-retrieve-update-delete'),
    path('products/<int:product_id>/deactivate/', deactivate_product, name='deactivate-product'),
    path('products/<int:product_id>/activate/', activate_product, name='activate-product'),
    
]