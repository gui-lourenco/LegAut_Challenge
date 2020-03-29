from .models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'birth': forms.DateInput(format='%d/%m/%Y')
        }

class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'