from django.db import models

class Client(models.Model):
    cpf = models.CharField(max_length=11)
    name = models.CharField(max_length=100)
    rg = models.CharField(max_length=9)
    adress = models.CharField(max_length=200)
    contact = models.CharField(max_length=11)
    email = models.CharField(max_length=150)
    # photo = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Contract(models.Model):
    client_cpf = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
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
