from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from .models import *
from .forms import *
import mimetypes

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

def userDelete(user):
    user = User.objects.get(username=user)
    user.delete()

def addContract(request):
    form = ContractForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()

def download_file(request, file, filename):
    # fill these variables with real values
    
    with open(file, 'rb+') as download:
        mime_type, _ = mimetypes.guess_type(file)
        response = HttpResponse(download, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response