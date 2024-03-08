from django.contrib.auth import login as auth_login,logout as auth_logout
from django.shortcuts import render, redirect
from accounts.models import User
from accounts.forms import CustomUserCreationForm, CustomAuthenticationForm
from coupons.models import Coupon


# Create your views here.

def join(request):
    if request.user.is_authenticated:
        return redirect('posts:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/join.html',context)

def login(request):
    if request.user.is_authenticated:
        return redirect('posts:index')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request,user)
            return redirect('posts:index')
    else:
        form = CustomAuthenticationForm(request)
    context = {
        'form':form,
    }
    return render(request,'accounts/login.html',context)

def logout(request):
    auth_logout(request)
    return redirect('posts:index')

def user_info(request,username):
    user = User.objects.get(username=username)
    coupons = Coupon.objects.filter(user=user)
    context = {
        'user':user,
        'coupons':coupons,
    }
    return render(request,'accounts/user_info.html',context)