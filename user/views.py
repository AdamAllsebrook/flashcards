from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout as logout_user, login as login_user
from django.shortcuts import render, redirect
from dataclasses import dataclass
from .forms import RegisterForm, LoginForm


def register(request):
    context = {}
    form = RegisterForm(request.POST)

    if request.method == "POST":

        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password']
            )
            auth_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if auth_user is not None:
                login_user(request, auth_user)
                return redirect('/')

        else:
            stringify_errors(form)

    context['form'] = form
    return render(request, 'register.html', context)


def login(request):
    context = {}
    form = LoginForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login_user(request, user)
                return redirect('/')
            else:
                context['error'] = 'Invalid username or password!'

        else:
            stringify_errors(form)

    context['form'] = form
    return render(request, 'login.html', context)


def logout(request):
    logout_user(request)
    return redirect('/')


def stringify_errors(form):
    for field in form:
        if field.errors:
            field.error_text = ' '.join(field.errors)
        else:
            field.error_text = None
