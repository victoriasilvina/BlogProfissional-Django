from django.db import models

# Create your models here.

class Pessoal(models.Model):
    nome = models.CharField(max_length=100)
    parentesco = models.CharField(max_length=20)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='media/images/', null= True, blank=True)
    
    def __str__(self):
        return self.nome

class Rotina(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='media/images/', null= True, blank=True)

    
    def __str__(self):
        return self.titulo
    
class Gostos(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    
    def __str__(self):
        return self.titulo


    