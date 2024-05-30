from django.urls import path

from .import views


urlpatterns = [
    path("",views.signin,name='login'),
    path("signout/",views.signout,name="logout"),
    path("register/",views.register,name="register"),
]
