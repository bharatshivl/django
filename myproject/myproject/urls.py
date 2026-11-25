
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse,render

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home),
    path('about',about),
    path('contact',contact)
]
