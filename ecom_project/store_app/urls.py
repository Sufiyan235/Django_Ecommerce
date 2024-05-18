from django.urls import path

from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("category_store/<slug:category_slug>/",views.store,name="store"),
]
