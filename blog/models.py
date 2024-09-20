from django.db import models

# Create your models here.

class Pessoal(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='/images/', blank=True)
    
    def __str__(self):
        return self.titulo

class Rotina(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='/images/', blank=True)
    
    def __str__(self):
        return self.titulo
    
class Gostos(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='/images/', blank=True)
    
    def __str__(self):
        return self.titulo


    