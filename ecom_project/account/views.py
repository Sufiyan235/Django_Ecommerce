from django.shortcuts import render,redirect
from .models import Account
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        passwd = request.POST['passwd']
        acc = Account.objects.create_user(first_name = fname,last_name=lname,email=email,password=passwd)
        acc.save()
        return redirect('login')
    return render(request,'accounts/register.html')



def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['passwd']
        user = authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        messages.error(request,"Wrong Credentials")
    return render(request,'accounts/login.html')


def signout(request):
    logout(request)
    return redirect('login')