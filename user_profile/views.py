from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import login, authenticate, logout

# Create your views here.



def login_view(request):
    """Login  view"""

    if request.user.is_authenticated:
        messages.warning(request,"You are already logged in!")
        return redirect('dashboard')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('login')

    return render(request, 'user_profile/login.html')



def logout_view(request):
    logout(request)
    messages.info(request, "You are now logged out")
    return redirect('login')


def forgot_password(request):
    return render(request, 'user_profile/forgot-password.html')