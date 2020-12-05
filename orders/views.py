import time
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from carts.models import Cart
from .models import Order

# Create your views here.


def checkout(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse('cart'))

    new_order, created = Order.objects.get_or_create(cart=cart)
    if created:
        new_order.order_id = str(time.time())
        new_order.save()
    if new_order.status == "Finished":
        cart.delete()
        del request.session['cart_id']
        del request.session['items_total']
    context = {}
    return render(request, 'products/all_product.html', context)
