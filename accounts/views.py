from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):
    if request.method == 'POST':
        #tHE USER WANTS TO SIGN UP!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html',{'error':'Username allready exist!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html',{'error':'password not match!'})

    else:
         #user wants to enter info   
        return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

# TODO need to rout to home page

def logout(request):
    return render(request, 'accounts/signout.html')



    