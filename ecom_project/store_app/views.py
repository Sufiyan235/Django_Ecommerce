from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import random
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@login_required(login_url="login")
def home(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    context = {
        "categories":categories,
        "brands":brands
    }
    return render(request,'home.html',context)

@login_required(login_url="login")
def category_store(request,category_slug):

    category = Category.objects.get(category_slug=category_slug)
    products = Product.objects.filter(category=category, is_available=True)

    context = {
        "products":products,
    }
    return render(request,'category_store.html',context)

@login_required(login_url="login")
def store(request):
    products = Product.objects.all()
    listed=list(products)
    products=random.sample(listed,k=9)
    context = {
        "products":products,
    }
    return render(request,'store.html',context)

@login_required(login_url="login")
def product_detail(request,product_slug):
    product = Product.objects.get(product_slug=product_slug)
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

@login_required(login_url="login")
def brand_store(request,brand_slug):
    brand = Brand.objects.get(brand_slug=brand_slug)
    products = Product.objects.filter(brand=brand, is_available=True)
    context = {
        "products":products,
    }
    return render(request,'brand_store.html',context)

@login_required(login_url="login")
def add_to_cart(request,product_id):
    user = request.user
    product = Product.objects.get(id=product_id)

    cart ,_ = Cart.objects.get_or_create(user=user)
    cart_item = CartItems.objects.create(cart=cart,product=product)
    variant = request.GET.get("variant")
    if variant :
        variant = request.GET.get('variant')
        size_variant = SizeVariant.objects.get(size_name=variant)
        cart_item.size_variant = size_variant
        cart_item.save()
    else:
        cart_item.save()
    return redirect("product_detail",product_slug=product.product_slug)

@login_required(login_url="login")
def cart(request):
    cart_items = CartItems.objects.filter(cart__is_paid=False,cart__user = request.user)
    cart = Cart.objects.filter(user=request.user).first()

    if request.method =='POST':
        coupon_code = request.POST.get('coupon')
        coupon_obj = Coupon.objects.filter(coupon_name__icontains = coupon_code)
        if not coupon_obj.exists() :
            messages.error(request,'Invalid Coupon')
            if request.GET.get("next_page"):
                return redirect(request.GET.get("next_page"))
            return redirect("cart")
        
        if cart.coupon :
            messages.error(request,'Coupon Already Exists')
            if request.GET.get("next_page"):
                return redirect(request.GET.get("next_page"))
            return redirect("cart")
        
        if cart.get_cart_total() < coupon_obj[0].minimum_amount:
            messages.error(request,f'Minimum amount to apply this coupun should be {coupon_obj[0].minimum_amount}')
            if request.GET.get("next_page"):
                return redirect(request.GET.get("next_page"))
            return redirect("cart")
        
        if coupon_obj[0].is_expired:
            messages.error(request,"Coupon Expired")
            if request.GET.get("next_page"):
                return redirect(request.GET.get("next_page"))
            return redirect("cart")
        
        cart.coupon = coupon_obj[0]
        cart.save()
        messages.success(request,'Coupon Applied')
        if request.GET.get("next_page"):
            return redirect(request.GET.get("next_page"))
        
    context = {
        "cart_items":cart_items,
        "cart":cart
    }
    return render(request,'cart.html',context)


def remove_coupon(request,cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.coupon = None
    cart.save()
    messages.success(request,'Coupon Removed')
    if request.GET.get("next_page"):
        return redirect(request.GET.get("next_page"))
    return redirect('cart')

@login_required(login_url="login")
def remove_cart_item(request,cart_item_id):
    
    try:
        cart_item = CartItems.objects.get(id=cart_item_id)
        cart_item.delete()
    except Exception as e:
        print(e)
    if request.GET.get("next_page"):
        return redirect(request.GET.get("next_page"))
    return redirect("cart")



@login_required(login_url="login")
def checkout(request):
    cart_items = CartItems.objects.filter(cart__is_paid=False,cart__user = request.user)
    cart = Cart.objects.filter(user=request.user).first()
    grand_total = cart.get_cart_total() + 8.95
    
    context = {
        "cart_items":cart_items,
        "cart":cart,
        "grand_total":grand_total
    }
    return render(request,'checkout_pages/checkout.html',context)



@login_required(login_url="login")
def checkout_shipping(request):
    return render(request,'checkout_pages/checkout-shipping.html')

@login_required(login_url="login")
def checkout_payment(request):
    return render(request,'checkout_pages/checkout-payment.html')