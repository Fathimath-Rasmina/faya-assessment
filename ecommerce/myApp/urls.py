from django.urls import path
from .views import (
    CustomerListCreateView,
    CustomerRetrieveUpdateDeleteView,
    ProductListCreateView,
    ProductRetrieveUpdateDeleteView,
    activate_deactivate_product
)

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDeleteView.as_view(), name='customer-retrieve-update-delete'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDeleteView.as_view(), name='product-retrieve-update-delete'),
    path('products/<int:product_id>/activate-deactivate/', activate_deactivate_product, name='activate-deactivate-product'),
]