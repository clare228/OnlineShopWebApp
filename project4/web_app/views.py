from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "web_app/home.html")

def home(request):
    return render(request, "web_app/home.html")

def collection(request):
    return render(request, "web_app/collection.html")

def about(request):
    return render(request, "web_app/about.html")

def contact(request):
    return render(request, "web_app/contact.html")

def category(request):
    return render(request, "web_app/category.html")

