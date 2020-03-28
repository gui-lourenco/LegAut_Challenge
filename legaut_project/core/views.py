from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *
from .utility import *
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import os

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
        
            return redirect('core:user', username) 
        
        messages.error(request, 'Usuário Inválido')

    context = {}
    return render(request, 'core/login.html', context)

@login_required(login_url='core:login')
def userPage(request, user):
    user = User.objects.get(username=user)
    client = user.client
    contract_list = client.contract_set.all()
    context = {'client':client, 'contracts':contract_list}
    return render(request, 'core/user.html', context)

@login_required(login_url='core:login')
def managerPage(request):
    users = Client.objects.all()
    form = ContractForm()
    context = {'username':request.user, 'clients':users, 'form':form}
    
    if request.method == 'POST':
        addContract(request)
        return render(request, 'core/manager.html', context)
    
    return render(request, 'core/manager.html', context)

@login_required(login_url='core:login')
def logoutPage(request):
    logout(request)
    return redirect('core:home')

@login_required(login_url='core:login')
def userCreatePage(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            return redirect('core:clientCreate', username=user.username, password=user.password)

        else:
            messages.error(request, form.errors)
            return redirect('core:userCreate')

    form = UserForm()
    context = {'form':form, "username":request.user}
    return render(request, 'core/userCreate.html', context)

@login_required(login_url='core:login')
def clientCreatePage(request, username, password):
    if request.method == 'POST':
        new_user = User(username=username, password=password)
        client = Client(user=new_user)
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            new_user.save()
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('core:manager')

        else:
            messages.error(request, form.errors)
            return redirect('core:clientCreate', username=username, password=password)

    form = ClientForm()
    context = {'form':form, "username":request.user}
    return render(request, 'core/clientCreate.html', context)

@login_required(login_url='core:login')
def userSettingsPage(request, user, info):
    user = User.objects.get(username=user)
    if info == 'user':
        form = UserForm(instance=user)
        if request.method == 'POST':
            form = UserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('core:user', user.username)

        context = {'user':user, 'form':form}
        return render(request, 'core/userSettings.html', context)

    elif info == 'client':
        form = ClientForm(instance=user)
        if request.method == 'POST':
            form = ClientForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                return redirect('core:user', user.username)

        context = {'user':user, 'form':form}
        return render(request, 'core/userSettings.html', context)

@login_required(login_url='core:login')
def managerSettingsPage(request, user, info):
    user = User.objects.get(username=user)
    if info == 'user':
        form = UserForm(instance=user)
        if request.method == 'POST':
            form = UserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('core:manager')

        context = {'user':user, 'form':form}
        return render(request, 'core/managerUserSetting.html', context)

    elif info == 'client':
        form = ClientForm(instance=user.client)
        if request.method == 'POST':
            form = ClientForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                return redirect('core:manager')

        context = {'user':user, 'form':form}
        return render(request, 'core/managerUserSetting.html', context)

@login_required(login_url='core:login')
def userDetailPage(request, user):
    if request.method == 'POST':
        if request.POST.get('del'):
            userDelete(user)
            return redirect('core:manager')

    user = User.objects.get(username=user)
    contracts = user.client.contract_set.all()
    searchs = user.client.search_set.all()
    context = {'user':user, 'contracts':contracts, 
    'n_cont': len(contracts), 'searchs':searchs}
    return render(request, 'core/userDetail.html', context)

@login_required(login_url='core:login')
def downloadPage(request, file):
    contract = Contract.objects.get(pk=file)
    file = contract.file.path
    filename = os.path.basename(contract.file.path)
    return download_file(request, file, filename)

@login_required(login_url='core:login')
def searchPage(request, user, key):
    user = User.objects.get(username=user)
    search(user.id, key)
    return redirect('core:userDetail', user=user)