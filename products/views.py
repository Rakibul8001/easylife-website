from django.shortcuts import render, Http404
from .models import Product, ProductImage

# Create your views here.
def search(request):
    try:
        k = request.GET.get('k')
    except:
        k = None
    if k:
        products = Product.objects.filter(title__icontains = k)
        return render(request, 'products/results.html',{
            'query': k,
            'products':products,
        })
    else:
        return render(request, 'products/results.html')

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
        images = ProductImage.objects.filter(product = product)
        return render(request, 'products/single.html',{
            'product': product,
            'images': images
    })
    except:
        raise Http404

