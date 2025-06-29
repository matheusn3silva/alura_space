from django.shortcuts import render
from galeria.models import Photograph

def index(request):
    photographs = Photograph.objects.all()
    return render(request, 'galeria/index.html', {"cards": photographs})

def imagem(request):
    
    return render(request, 'galeria/imagem.html')