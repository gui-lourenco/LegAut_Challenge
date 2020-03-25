from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import *
# from django.contrib.auth.form import UserCreationForm

def homePage(request):
    return render(request, 'core/home.html')

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('core:manager') 
            #provisório (vai enviar para a pag do usuario)
            return redirect('core:user') 

    context = {}
    return render(request, 'core/login.html', context)

def userPage(request):
    user = get_object_or_404(Client, cpf=request.user)
    contract_list = user.contract_set.all()
    context = {'username':request.user, 'contracts':contract_list}
    return render(request, 'core/user.html', context)

def managerPage(request):
    context = {'username':request.user}
    return render(request, 'core/manager.html', context)

def logoutPage(request):
    logout(request)
    return redirect('core:home')