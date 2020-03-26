from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9)
    birth = models.DateField(null=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=150)
    sex = models.CharField(max_length=1, null=True)
    marital_status = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Contract(models.Model):
    client_cpf = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    last_modify = models.DateTimeField(null=True)
    # file = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}-{self.client_cpf}'

class Search(models.Model):
    client_cpf = models.ForeignKey(Client, on_delete=models.CASCADE)
    search_key = models.CharField(max_length=4)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.client_cpf}-{self.title}'
