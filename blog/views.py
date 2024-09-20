from django.shortcuts import render
from .models import Pessoal, Rotina, Gostos

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def rotina(request):
    return render(request, 'blog/rotina.html')

def gostos(request):
    return render(request, 'blog/gostos.html')

def familia(request):
    familia = Pessoal.objects.all()
    contexto = {
        'familia': familia,
    }
    return render(request, 'blog/familia.html', contexto)
