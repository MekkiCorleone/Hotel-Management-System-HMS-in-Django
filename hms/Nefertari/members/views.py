from django.shortcuts import render, redirect

def signup(request):
    return render(request, 'members/signup.html')

def login(request):
    return render(request, 'members/login.html')

