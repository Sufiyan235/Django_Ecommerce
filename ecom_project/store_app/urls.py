from django.urls import path

from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path('store/',views.store,name="store"),
    path("category_store/<slug:category_slug>/",views.category_store,name="category_store"),
    path("brand_store/<slug:brand_slug>/",views.brand_store,name="brand_store"),
    path("product_detail/<slug:product_slug>/",views.product_detail,name="product_detail"),
    path("add_to_cart/<int:product_id>/",views.add_to_cart,name="add_to_cart"),
    path("cart/",views.cart,name="cart"),
    path("remove_cart_item/<int:cart_item_id>/",views.remove_cart_item,name="remove_cart_item"),
    path("checkout/",views.checkout,name="checkout"),
    # path("checkout_shipping/",views.checkout_shipping,name="checkout_shipping"),
    path("checkout_payment/",views.checkout_payment,name="checkout_payment"),
    path("remove_coupon/<int:cart_id>/",views.remove_coupon,name="remove_coupon"),
    path("add_quantity/<int:cart_id>/<int:product_id>/",views.add_quantity,name="add_quantity"),
    path("remove_quantity/<int:cart_id>/<int:product_id>/",views.remove_quantity,name="remove_quantity")
]
