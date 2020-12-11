import re
from django.shortcuts import render, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .forms import LoginForm, RegistrationForm
from .models import EmailConfirmed

# Create your views here.


def logout_view(request):
    logout(request)
    messages.warning(
        request, "You Are Logged Out. Feel free to <a href='%s'>login</a> again." % (reverse('auth_login')), extra_tags='safe')
    messages.success(
        request, "You Are Logged Out. Feel free to login again.")
    messages.error(
        request, "You Are Logged Out. Feel free to login again.")
    return HttpResponseRedirect('%s' % (reverse('auth_login')))


def login_view(request):
    form = LoginForm(request.POST or None)
    btn = "Login"
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(
            request, "Successfully Logged In. Welcome Back!.")
        return HttpResponseRedirect(reverse('all_product'))
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
        messages.success(
            request, "Successfully registered. Please confirm your email now.")
        return HttpResponseRedirect(reverse('all_product'))
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
        try:
            instance = EmailConfirmed.objects.get(
                activation_key=activation_key)
        except EmailConfirmed.DoesNotExist:
            instance = None
            messages.error(
                request, "There was an error. Please Try again !")
            return HttpResponseRedirect(reverse('all_product'))
        if instance is not None and not instance.confirmed:
            page_message = "Confirmation successful !!"
            instance.confirmed = True
            instance.activation_key = "Confirmed"
            instance.save()
            messages.success(
                request, "Successfully Confirmed. Please Log in.")
        elif instance is not None and instance.confirmed:
            page_message = "Already Confirmed"
            messages.warning(
                request, "Already Confirmed")
        else:
            page_message = ""
        context = {"page_message": page_message}
        return render(request, 'accounts/activation_complete.html', context)
    else:
        raise Http404
