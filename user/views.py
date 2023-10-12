from django.contrib.auth.models import User
from django.shortcuts import render
from dataclasses import dataclass
from .forms import RegisterForm


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
            print(user)
        else:
            for field in form:
                if field.errors:
                    field.error_text = ' '.join(field.errors)
                else:
                    field.error_text = None

    context['form'] = form
    return render(request, 'register.html', context)
