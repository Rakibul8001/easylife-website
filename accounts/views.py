import re
from django.shortcuts import render, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate

from .forms import LoginForm, RegistrationForm
from .models import EmailConfirmed

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


SHA_RE = re.compile('^[a-f0-9]{40}$')


def activation_view(request, activation_key):
    if SHA_RE.search(activation_key):
        print("Activation Key Is Real !!!")
        try:
            instance = EmailConfirmed.objects.get(
                activation_key=activation_key)
        except EmailConfirmed.DoesNotExist:
            instance = None
            raise Http404
        if instance is not None and not instance.confirmed:
            page_message = "Confirmation successfull !!"
            instance.confirmed = True
            instance.activation_key = "Confirmed"
            instance.save()
        elif instance is not None and instance.confirmed:
            page_message = "Already Confirmed"
        else:
            page_message = ""
        context = {"page_message": page_message}
        return render(request, 'accounts/activation_complete.html', context)
    else:
        raise Http404
