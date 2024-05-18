from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    categories = Category.objects.all()
    context = {
        "categories":categories,
    }
    return render(request,'home.html',context)


def store(request,category_slug):
    print("here")
    print(category_slug)
    return redirect('home')