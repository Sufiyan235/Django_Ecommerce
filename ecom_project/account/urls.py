from django.urls import path

from .import views


urlpatterns = [
    path("",views.signin,name='login'),
    path("signout/",views.signout,name="logout"),
    path("register/",views.register,name="register"),

    path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
    path('resetpassword_validate/<uid>/<token>/',views.resetpassword_validate,name="resetpassword_validate"),
    path('resetpassword/',views.resetpassword,name="resetpassword"),
]
