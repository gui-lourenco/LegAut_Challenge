from django.contrib.auth.models import User
from .models import *

def createUser(args):
    user = User.objects.create_user(username=args['cpf'], 
    email=args['email'], password=args['password1'])
    user.first_name = args['name'].split(' ')[0]
    user.last_name = args['name'].split(' ')[-1]
    return user

def createClient(user, args):
    client = Client(user=user, name=args['name'], cpf=args['cpf'], 
    rg=args['rg'], birth=args['birth'], address=args['end'], 
    phone=args['tel'], email=args['email'], sex=args['sex'], 
    marital_status=args['status'])
    return client