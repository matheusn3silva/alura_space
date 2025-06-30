from django.shortcuts import render, get_object_or_404
from galeria.models import Photograph

def index(request):
    photographs = Photograph.objects.all()
    return render(request, 'galeria/index.html', {"cards": photographs})

def imagem(request, photo_id):
    photograph = get_object_or_404(Photograph, pk=photo_id)
    return render(request, 'galeria/imagem.html', {"photograph": photograph})