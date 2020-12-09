from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate

from .forms import LoginForm, RegistrationForm

# Create your views here.


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('all_product'))


def login_view(request):
    form = LoginForm(request.POST or None)
    btn = "Login"
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        user.emailconfirmed.activate_user_email()
    context = {
        'form': form,
        'submit_btn': btn
    }
    return render(request, 'accounts/form.html', context)


def register_view(request):
    form = RegistrationForm(request.POST or None)
    btn = "Join"
    if form.is_valid():
        new_user = form.save(commit=False)
        # new_user.first_name = "Mohammad"
        new_user.save()
        # username = form.cleaned_data['username']
        # password = form.cleaned_data['password']
        # user = authenticate(username=username, password=password)
        # login(request, user)
    context = {
        'form': form,
        'submit_btn': btn
    }
    return render(request, 'accounts/form.html', context)
