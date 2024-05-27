
from django.urls import path, include
from user_profile import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('forgot-password', views.forgot_password, name='forgot-password'),
    path('employee-list', views.employee_list, name='employee-list'),
    path('employee/add', views.add_employee, name='add-employee'),
]
