from .models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['profile_pic']

class ClientAlterForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
