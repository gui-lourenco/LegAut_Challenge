from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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
    # user = get_object_or_404(Client, cpf=request.user)
    user = request.user.client
    contract_list = user.contract_set.all()
    context = {'user':user, 'contracts':contract_list}
    return render(request, 'core/user.html', context)

def managerPage(request):
    users = Client.objects.all()
    context = {'username':request.user, 'clients':users}
    return render(request, 'core/manager.html', context)

def logoutPage(request):
    logout(request)
    return redirect('core:home')

def userCreatePage(request):
    return render(request, 'core/userCreate.html')

def userSettingsPage(request, user):
    user = User.objects.get(username=user)
    return render(request, 'core/userSettings.html',{'user':user})

def userDetailPage(request, user):
    if request.method == 'POST':
        return redirect('core:userDelete', user=user)

    user = User.objects.get(username=user)
    contracts = user.client.contract_set.all()
    context = {'user':user, 'contracts':contracts, 'n_cont': len(contracts)}
    return render(request, 'core/userDetail.html', context)

def userDeletePage(request, user):
    if request.POST.get('del') is None:
        user = User.objects.get(username=user)
        user.delete()

    return redirect('core:manager')