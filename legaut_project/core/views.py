from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
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
        
            return redirect('core:user') 
        
        messages.error(request, 'Usuário Inválido')

    context = {}
    return render(request, 'core/login.html', context)

def userPage(request):
    user = request.user.client
    contract_list = user.contract_set.all()
    context = {'user':user, 'contracts':contract_list}
    return render(request, 'core/user.html', context)

def managerPage(request):
    users = Client.objects.all()
    form = ContractForm()
    context = {'username':request.user, 'clients':users, 'form':form}
    
    if request.method == 'POST':
        addContract(request)
        return render(request, 'core/manager.html', context)
    
    return render(request, 'core/manager.html', context)

def logoutPage(request):
    logout(request)
    return redirect('core:home')

def userCreatePage(request):
    form = ClientForm()
    if request.method == 'POST':
        user = createUser(request.POST)
        client = createClient(user, request.POST)
        form = ClientForm(request.POST, request.FILES, instance=client)
        try:
            user.save()
            form.save()
            client.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('core:userCreate')

        except AttributeError:
            messages.error(request, 'Falha no Cadastro! Verifique se os campos foram preenchidos corretamente')
            context = {'form':form}
            return redirect('core:userCreate')
        
    context = {'form':form, "username":request.user}
    return render(request, 'core/userCreate.html', context)

def userSettingsPage(request, user):
    user = User.objects.get(username=user)
    return render(request, 'core/userSettings.html',{'user':user})

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

def downloadPage(request, file):
    contract = Contract.objects.get(pk=file)
    file = contract.file.path
    filename = os.path.basename(contract.file.path)
    return download_file(request, file, filename)