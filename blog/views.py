from django.shortcuts import render
from .models import Pessoal, Rotina, Gostos

# Create your views here.
def index(request):
    return render(request, 'index.html')

def rotina(request):
    return render(request, 'rotina.html')

def gostos(request):
    return render(request, 'gostos.html')

def familia(request):
    familia = Pessoal.objects.all()
    contexto = {
        'familia': familia,
    }
    return render(request, 'familia.html', contexto)
