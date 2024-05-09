from django.shortcuts import render


# Create your views here.


def product_listing(request):
    #comment
    return render(request, 'product/product-list.html')