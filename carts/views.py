from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .models import Cart, CartItem
from products.models import Product

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


def update_cart(request, slug):
    request.session.set_expiry(120000)  # after 120000 secs cart will be empty

    try:
        qty = request.GET.get('qty')
        update_qty = True
    except:
        qty = None
        update_qty = False

    notes = {}
    try:
        color = request.GET.get('color')
        notes['color'] = color
    except:
        color = None

    try:
        size = request.GET.get('size')
        notes['size']=size
    except:
        size = None


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

    cart_item, created = CartItem.objects.get_or_create(cart=cart,product=product)
    if created:
        print("Yeah, it's created")
    if update_qty and qty:
        if int(qty)<=0:
            cart_item.delete()
        else:
            cart_item.quantity = qty
            cart_item.notes = notes
            cart_item.save()
    else:
        pass

    # if not cart_item in carts.items.all():
    #     carts.items.add(cart_item)
    # else:
    #     carts.items.remove(cart_item)

    new_total = 0.00
    for item in cart.cartitem_set.all():
        line_total = float(item.product.price)* item.quantity
        new_total += line_total

    request.session['items_total'] = cart.cartitem_set.count()
    cart.total = new_total
    cart.save()
    return HttpResponseRedirect(reverse('cart'))
