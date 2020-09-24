from django.shortcuts import render
from .models import Product, ProductImage

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html',{
        'products': products
    })

def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/all_product.html',{
        'products': products
    })