
from django.urls import path, include
from admin_panel import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('product-list', views.product_list, name='product-list'),
]
