from django.shortcuts import render, HttpResponseRedirect
from .models import Cart
from products.models import Product
from django.urls import reverse
# Create your views here.
def cart(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    if the_id:
        carts = Cart.objects.get(id = the_id)
        return render(request,'carts/index.html',{'carts':carts})
    else:
        empty_message = 'Your cart is empty, please keep shopping!'
        return render(request,'carts/index.html',{'empty': True,'empty_message': empty_message,})

def update_cart(request, slug):
    request.session.set_expiry(120000)  #after 120000 secs cart will be empty
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id = the_id)
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
    request.session['items_total'] = cart.products.count()
    cart.total = new_total
    cart.save()
    return HttpResponseRedirect(reverse('cart'))