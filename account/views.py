from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import HttpResponse

# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/shop")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'account/login.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken.')
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken.')
                return redirect(register)
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'Password not matching..')
            return redirect('register')
        return redirect('register')

    else:
        print('not cerated')
    return render(request,'account/registation.html')

def logout(request):
    auth.logout(request)
    return redirect("/shop")
