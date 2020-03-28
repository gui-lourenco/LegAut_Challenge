from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, render
from background_task import background
from .models import *
from .forms import *
import mimetypes
from .crawler import *
import os

def userDelete(user):
    user = User.objects.get(username=user)
    os.remove(user.client.profile_pic.path)
    for cont in user.client.contract_set.all():
        os.remove(cont.file.path)

    user.delete()

def addContract(request):
    form = ContractForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()

def download_file(request, file, filename):
    with open(file, 'rb+') as download:
        mime_type, _ = mimetypes.guess_type(file)
        response = HttpResponse(download, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response

@background(schedule=60)
def search(user_id, key):
    user = User.objects.get(id=user_id)
    if key == 'nome':
        results = get_google_first_page(user.client.name)
        for res in results:
            Search(client_cpf=user.client, search_key='nome', 
            title=res[0], link=res[1]).save()

    elif key == 'cpf':
        results = get_google_first_page(user.username)
        for res in results:
            Search(client_cpf=user.client, search_key='cpf', 
            title=res[0], link=res[1]).save()