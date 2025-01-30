from rest_framework import serializers
from .models import Heroes


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroes
        fields = '__all__'# esta parte es para que se muestren todos los campos de la tabla,
        # si solo se quiere mostrar algunos campos se puede hacer de la siguiente manera:
        # fields = ['fullname', 'age', 'description']