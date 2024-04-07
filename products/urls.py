
from django.urls import path, include
from products import views


urlpatterns = [
    path('product-list/', views.product_listing, name="product listing")
]
