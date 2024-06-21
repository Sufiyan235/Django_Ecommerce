from django.shortcuts import render,redirect
from .models import *

import random

from django.db.models import Q

# Create your views here.
def home(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    context = {
        "categories":categories,
        "brands":brands
    }
    return render(request,'home.html',context)


def category_store(request,category_slug):

    category = Category.objects.get(category_slug=category_slug)
    products = Product.objects.filter(category=category, is_available=True)

    context = {
        "products":products,
    }
    return render(request,'category_store.html',context)


def store(request):
    products = Product.objects.all()
    listed=list(products)
    products=random.sample(listed,k=9)
    context = {
        "products":products,
    }
    return render(request,'store.html',context)

def product_detail(request,id):
    product = Product.objects.get(id=id)
    product_images = ProductImage.objects.filter(product=product)
    available_designs = AvailableDesign.objects.filter(available_products=product)

    related_products = Product.objects.filter(
    Q(brand=product.brand) | Q(category=product.category)).exclude(product_name=product.product_name).distinct()

    
    context = {
        "product":product,
        "product_images":product_images,
        "related_products":related_products,
        "available_designs":available_designs
    }

    if request.GET.get('size'):
        size = request.GET.get('size')
        price = product.get_product_price_by_size(size)
        context['updated_price'] = price
        context['selected_size'] = size
    return render(request,'details.html',context)


def brand_store(request,brand_slug):
    brand = Brand.objects.get(brand_slug=brand_slug)
    products = Product.objects.filter(brand=brand, is_available=True)
    context = {
        "products":products,
    }
    return render(request,'brand_store.html',context)


def cart(request):
    return render(request,'cart.html')


def checkout(request):
    return render(request,'checkout_pages/checkout.html')


def checkout_shipping(request):
    return render(request,'checkout_pages/checkout-shipping.html')


def checkout_payment(request):
    return render(request,'checkout_pages/checkout-payment.html')