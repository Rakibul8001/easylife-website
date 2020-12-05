from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('orders/', views.orders, name='user_orders')
]
