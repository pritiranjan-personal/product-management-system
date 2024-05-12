from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'admin_panel/index.html')




@login_required(login_url='login')
def product_list(request):
    return render(request, 'product-list.html')

