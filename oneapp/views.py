from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *

from django.contrib.auth import authenticate, login, logout 
from .forms import CreateUserForm, ProfileForm
from django.contrib.auth.decorators import login_required 

from .decorators import unauthenticated_user


def index(request):
    return render(request, 'index.html')

@unauthenticated_user
def register_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Account is created')
            return redirect('login')
        else:
            context = {'form': form}
            messages.info(request,'Invalid credentials')
            return render(request, 'register.html', context)
    context = {'form': form}
    return render(request, 'register.html', context)
    
@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')

    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')


def courses(request):
    return render(request, 'courses.html')

def trainers(request):
    return render(request, 'trainers.html')

def events(request):
    return render(request, 'events.html')

def pricing(request):
    return render(request, 'pricing.html')

def contact(request):
    return render(request, 'contact.html')




def coursedetails(request):
    return render(request, 'coursedetails.html')

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='login')
def editprofile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username= request.user.username
            messages.success(request, f'{username}, Your profile is updated')
            return redirect('profile')
    else:
        form = ProfileForm(instance = request.user.profile)
    context = {'form':form}
    return render(request, 'editprofile.html', context) 
        
    
def index1(request):
    return render(request, 'index1.html')

