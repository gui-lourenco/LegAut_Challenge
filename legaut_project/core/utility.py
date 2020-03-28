from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, render
from .models import *
from .forms import *
import mimetypes

def userDelete(user):
    user = User.objects.get(username=user)
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