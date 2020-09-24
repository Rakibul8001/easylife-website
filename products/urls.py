from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name = 'index'),
    path('all_product', views.all_products , name = 'all_product')
]