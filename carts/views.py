from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .models import Cart, CartItem
from products.models import Product, Variation

# Create your views here.


def cart(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        return render(request, 'carts/index.html', {'cart': cart})
    else:
        empty_message = 'Your cart is empty, please keep shopping!'
        return render(request, 'carts/index.html', {'empty': True, 'empty_message': empty_message, })


def add_to_cart(request, slug):
    request.session.set_expiry(120000)  # after 120000 secs cart will be empty

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass

    product_var = []
    if request.method == 'POST':
        qty = request.POST['qty']
        for item in request.POST:
            key = item
            val = request.POST[key]
            try:
                v = Variation.objects.get(
                    product=product, category__iexact=key, title__iexact=val)
                product_var.append(v)
            except:
                pass

        cart_item = CartItem.objects.create(
            cart=cart, product=product)

        if len(product_var) > 0:
            cart_item.variations.add(*product_var)
        cart_item.quantity = qty
        cart_item.save()

        new_total = 0.00
        for item in cart.cartitem_set.all():
            line_total = float(item.product.price) * item.quantity
            new_total += line_total

        request.session['items_total'] = cart.cartitem_set.count()
        cart.total = new_total
        cart.save()
        return HttpResponseRedirect(reverse('cart'))

    return HttpResponseRedirect(reverse('cart'))
