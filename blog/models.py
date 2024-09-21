from django.db import models

# Create your models here.

class Pessoal(models.Model):
    nome = models.CharField(max_length=100, null= True, blank=True)
    parentesco = models.CharField(max_length=100, null= True, blank=True)
    descricao = models.TextField(null= True,blank=True)
    imagem = models.ImageField(upload_to='media/images/', null= True,blank=True)
    
    def __str__(self):
        return self.nome or "Sem nome"

class Rotina(models.Model):
    titulo = models.CharField(max_length=100, null= True, blank=True)
    descricao = models.TextField(null= True, blank=True)
    imagem = models.ImageField(upload_to='media/images/', null= True,blank=True)

    
    def __str__(self):
        return self.titulo or "Sem titulo"
    
class Gostos(models.Model):
    titulo = models.CharField(max_length=100,null= True, blank=True)
    descricao = models.TextField(null= True, blank=True)
    imagem = models.ImageField(upload_to='media/images/',null= True, blank=True)
    
    def __str__(self):
        return self.titulo or "Sem titulo"


    