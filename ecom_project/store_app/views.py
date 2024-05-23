from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    context = {
        "categories":categories,
        "brands":brands
    }
    return render(request,'home.html',context)


def store(request,category_slug):
    
    return render(request,'store.html')