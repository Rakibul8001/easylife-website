from django.shortcuts import render, Http404
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

def single(request, slug):
    try:
        product = Product.objects.get(slug = slug)
        return render(request, 'products/single.html',{
            'product': product
    })
    except:
        raise Http404