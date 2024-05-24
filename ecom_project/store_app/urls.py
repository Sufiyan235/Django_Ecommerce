from django.urls import path

from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("category_store/<slug:category_slug>/",views.store,name="store"),
    path("brand_store/<slug:brand_slug>/",views.brand_store,name="brand_store"),
    path("product_detail/<int:id>/",views.product_detail,name="product_detail"),
]
