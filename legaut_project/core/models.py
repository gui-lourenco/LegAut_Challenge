from django.db import models
from django.contrib.auth.models import User

SEX_CHOICES = (
    (1, ("Masculino")),
    (2, ("Feminino")))

STATUS_CHOICES = (
    (1,'Solteiro(a)'),
    (2,'Casado(a)'),
    (3,'Viúvo(a)'),
    (4,'Divorciado(a)'))

class Client(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rg = models.CharField(max_length=9)
    birth = models.DateField(null=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    sex = models.IntegerField(null=True, choices=SEX_CHOICES)
    marital_status = models.IntegerField(null=True, choices=STATUS_CHOICES)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profiles')

    def __str__(self):
        return self.name

class Contract(models.Model):
    client_cpf = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    last_modify = models.DateTimeField(null=True, auto_now=True)
    file = models.FileField(null=True, upload_to='files')

    def __str__(self):
        return f'{self.id}-{self.client_cpf}'

class Search(models.Model):
    client_cpf = models.ForeignKey(Client, on_delete=models.CASCADE)
    search_key = models.CharField(max_length=4)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.client_cpf}-{self.title}'
