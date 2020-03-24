from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
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
            print(username)
            #provisório (vai enviar para a pag do usuario)
            return redirect('/') 

    context = {}
    return render(request, 'core/login.html', context)