from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("CMS Home page")

def login(request):
    return HttpResponse("This is login Page")
