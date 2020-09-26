from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart, name = 'cart'),
    path('<slug>/', views.update_cart, name = 'update'),
]