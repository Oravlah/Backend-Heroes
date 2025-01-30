from rest_framework import viewsets
from .serializer import HeroSerializer
from .models import Heroes

# Create your views here.


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Heroes.objects.all() # se llama a todos los objetos de la tabla
    serializer_class = HeroSerializer   # se llama a la clase que se creo en serializer.py
