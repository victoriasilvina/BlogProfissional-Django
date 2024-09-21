from django.shortcuts import render
from .models import Pessoal, Rotina, Gostos

# Create your views here.
def index(request):
    familia = Pessoal.objects.all()
    gostos = Gostos.objects.all()
    rotina = Rotina.objects.all()
    
    contexto = {
        'familia': familia,
        'gostos': gostos,
        'rotina': rotina,
    }
    return render(request, 'blog/index.html', contexto)

def rotina(request):
    rotina = Rotina.objects.all()
    contexto = {
        'rotina': rotina,
    }
    return render(request, 'blog/rotina.html', contexto)

def gostos(request):
    gostos = Gostos.objects.all()
    contexto = {
        'gostos': gostos,
    }
    return render(request, 'blog/gostos.html', contexto)

def familia(request):
    familia = Pessoal.objects.all()
    contexto = {
        'familia': familia,
    }
    return render(request, 'blog/familia.html', contexto)
