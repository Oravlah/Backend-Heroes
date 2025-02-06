from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializer import UsersSerializer
from .models import Users

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def get_permissions(self):
        if self.action in ['create', 'list']:  # Permitir creación y listado sin autenticación
            return [AllowAny()]
        return [IsAuthenticated()]
