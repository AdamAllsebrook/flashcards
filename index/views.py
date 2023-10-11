from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'base.html')


def hello(request):
    return render(request, 'hello.html')
