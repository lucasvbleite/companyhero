from django.db import models

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
class Usuario(models.Model):
    username = models.CharField(max_length=50)
    empresas = models.ManyToManyField("api.Empresa", related_name='usuarios')
    
    def __str__(self):
        return self.username
    