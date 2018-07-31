from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
# Create your views here.

def index(request):
    username = request.GET.get('')
    if username:
        return HttpResponse("Front Home page")
    else:
        return redirect(reverse('front:login'))

def login(request):
    return HttpResponse("This is Front login Page")
