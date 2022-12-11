from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def Login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, 'Usuário ou senha inválidos')
    return render(request, 'authentication/login.html')

def Logout(request):
    logout(request)
    return redirect('/auth/')