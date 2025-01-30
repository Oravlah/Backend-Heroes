from rest_framework import viewsets
from .serializer import UsersSerializer
from .models import Users

# Create your views here.


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all() # se llama a todos los objetos de la tabla
    serializer_class = UsersSerializer  # se llama a la clase que se creo en serializer.py