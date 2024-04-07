from django.shortcuts import render

# Create your views here.



def login_view(request):
    return render(request, 'user_profile/login.html')


def forgot_password(request):
    return render(request, 'user_profile/forgot-password.html')