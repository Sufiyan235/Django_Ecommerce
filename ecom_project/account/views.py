from django.shortcuts import render,redirect
from .models import Account
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        passwd = request.POST['passwd']

        if Account.objects.filter(email=email).exists():
            messages.error(request,'Email already exists')
        else:
            acc = Account.objects.create_user(first_name = fname,last_name=lname,email=email,password=passwd)
            acc.save()
            messages.success(request,'Account Created Successfully!!!')
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
        messages.error(request,"Invalid Credentials")
    return render(request,'accounts/login.html')

@login_required(login_url="login")
def signout(request):
    logout(request)
    return redirect('login')


@login_required(login_url="login")
def update_shipping_address(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        address = request.POST.get("address")
        country = request.POST.get("country")
        state = request.POST.get("state")
        zip_code = request.POST.get("zip_code")

        fetched_acc = Account.objects.get(id=request.user.id)
        fetched_acc.first_name = fname
        fetched_acc.last_name = lname
        fetched_acc.email = email
        fetched_acc.address = address
        fetched_acc.country = country
        fetched_acc.state = state
        fetched_acc.zip_code = zip_code

        fetched_acc.save()

        messages.success(request,"Information Updated!!")
        return redirect("checkout")


def forgotpassword(request):
    if request.method=='POST':
        email=request.POST['email']
        if Account.objects.filter(email=email).exists():
            user=Account.objects.get(email__exact=email)
            current_site=get_current_site(request)
            mail_subject="Reset your password"
            message=render_to_string('emails/reset_password_email.html',
                         {'user':user,
                          'domain':current_site,
                          'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                          'token':default_token_generator.make_token(user)})
            to_email=email
            send_email=EmailMessage(mail_subject,message,to=[to_email])
            send_email.send()
            messages.warning(request,f'Password reset email has been sent to {email}')
            return redirect('login')
        else:
            messages.error(request,'Account does not exist')
            return redirect('forgotpassword')
    return render(request,'accounts/forgotten-password.html')


def resetpassword_validate(request,uid,token):
    try:
       uid=urlsafe_base64_decode(uid).decode()
       user=Account._default_manager.get(pk=uid)
    except Exception:
        user=None
    if user is not None and default_token_generator.check_token(user,token):
        request.session['uid']=uid
        user.save()
        messages.warning(request,"Enter New Password")
        return redirect('resetpassword')
    else:
        messages.error(request,"link expired")
        return redirect('register')

def resetpassword(request):
    if request.method=='POST':
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            uid=request.session.get('uid')
            user=Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request,'Password reset was successful')
            return redirect('login')
        else:
            messages.error(request,'Password do not match')
            return redirect('resetpassword')
    return render(request,'accounts/resetpassword.html')