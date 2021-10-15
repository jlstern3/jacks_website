from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')

def login(request):
    # if request.method == "POST":
    return redirect('/home')

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def programs(request):
    return render(request, 'programs.html')