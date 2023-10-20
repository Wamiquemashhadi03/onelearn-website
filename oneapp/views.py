from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       password2 = request.POST['password2']
     
       if password == password2:
           if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exist!')
                return redirect('register')
           
           elif User.objects.filter(username=username).exists():
               messages.info(request, 'Username already exist!')
               return redirect('register')
           else:
               user = User.objects.create_user(username=username, email=email, password=password)
               user.save();
               return redirect('login')
       else:
           messages.info(request,'Password not same!')
           return redirect('register')
    else:
         return render(request, 'register.html')


def login(request):
     if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid creds')
            return redirect('login')
     else:
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


def contact(request):
    return render(request, 'contact.html')


def coursedetails(request):
    return render(request, 'coursedetails.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
