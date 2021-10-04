from django.views.generic import TemplateView, RedirectView,CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.http import request, HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_control
from django.contrib.auth import login as auth_login, authenticate,logout as auth_logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.

# class HomePageView(TemplateView):
#     template_name = 'shopping/index.html'

# class LoginPageView(LoginView):
#     template_name = 'shopping/login.html'
def passHome(request):
    return redirect('shopping:home')

@login_required(login_url='shopping:login')
def home(request):
    print('home request placed*******')
    return render(request,'shopping/index.html')


def login(request):
    print(request.method)
    if request.user.is_authenticated:
        return redirect('shopping:home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password = password)
        if user is None:
            messages.error(request, 'Invalid Username or Password')
            print('authentication fails')
            return redirect('shopping:login')
        else:
            auth_login(request,user)
            request.session.set_expiry(300)
            request.session['my_car'] = 'mini'
            return redirect('shopping:home')
    return render(request,'shopping/login.html')

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        print('logout and redirecting to home page***********')
        return redirect('shopping:home')
    return redirect('shopping:login')

def register(request):
    if request.user.is_authenticated:
        auth_logout(request)
    if request.method == 'POST':
        username = request.POST['username']
        if User.objects.filter(username = username).exists():
            messages.error(request, 'Username alredy taken.')
            print('username exist!')
            print(username)
        else:
            firstname = request.POST['firstname']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.create_user(username=username,first_name=firstname,email=email,password=password)
            user.save()
            user = authenticate(request,username=username,password = password)
            auth_login(request,user)
            print('user created')
            return redirect('shopping:login')
    return render(request,'shopping/register.html')