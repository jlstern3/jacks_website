from django.shortcuts import render, redirect


def index(request):
    return render(request, 'login.html')

def login(request):
    #need to put in code to only allow user to go to route if properly logged in 
    # if request.method == "POST":
    return redirect('/home')

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def programs(request):
    return render(request, 'programs.html')

def contact(request):
    return render(request, 'contact.html')
