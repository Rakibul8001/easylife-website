from django.shortcuts import render, HttpResponseRedirect
from .models import Cart
from products.models import Product
from django.urls import reverse
# Create your views here.
def cart(request):
    carts = Cart.objects.all()[0]
    return render(request, 'carts/index.html',{
        'carts': carts
    })

def update_cart(request, slug):
    cart = Cart.objects.all()[0]
    try:
        product = Product.objects.get(slug = slug)
    except Product.DoesNotExist:
        pass
    if not product in cart.products.all():
        cart.products.add(product)
    else:
        cart.products.remove(product)

    new_total = 0.00
    for item in cart.products.all():
        new_total += float(item.price)
    cart.total = new_total
    cart.save()
    return HttpResponseRedirect(reverse('cart'))