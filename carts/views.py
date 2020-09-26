from django.shortcuts import render
from .models import Cart
# Create your views here.
def cart(request):
    carts = Cart.objects.all()[0]
    return render(request, 'carts/index.html',{
        'carts': carts
    })