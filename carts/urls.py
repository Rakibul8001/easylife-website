from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart, name='cart'),
    path('<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('<slug>/', views.add_to_cart, name='add_to_cart'),
]
