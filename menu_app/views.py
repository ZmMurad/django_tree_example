from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def home_view(request:HttpRequest):
    return render(request,'index.html')

def catalog_view(request:HttpRequest):
    return render(request,'index.html')

def user_view(request:HttpRequest):
    return render(request,'index.html')
