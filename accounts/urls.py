from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name="auth_logout"),
    path('login/', views.login_view, name="auth_login"),
    path('register/', views.register_view, name="auth_register"),
    path('activate/<activation_key>/',
         views.activation_view, name="activation_view"),
]
