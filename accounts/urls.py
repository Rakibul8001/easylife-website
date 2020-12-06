from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name="auth_logout"),
    path('login/', views.login_view, name="auth_login"),
]
