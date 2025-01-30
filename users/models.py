import uuid
from django.db import models
from django.core.validators import RegexValidator

class Users(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    fullname = models.CharField(max_length=20, validators=[RegexValidator(r'^[a-zA-Z ]*$')])
    username = models.CharField(max_length=20, validators=[RegexValidator(r'^[a-zA-Z ]*$')])
    email = models.EmailField(unique=True, validators=[RegexValidator(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')])
    password = models.CharField(max_length=20, validators=[RegexValidator(r'^[a-zA-Z0-9!@#$%^&*()_+]*$')])
    confirmpassword = models.CharField(max_length=20, validators=[RegexValidator(r'^[a-zA-Z0-9!@#$%^&*()_+]*$')])
    age = models.PositiveSmallIntegerField()


#1-validacion para el campo fullname, para que solo se puenda ingresar letras
#2-validacion para el campo username, para que solo se puenda ingresar letras
#3-validacion para el campo email, para que sea un email valido
#4-validacion para el campo password, para que solo se puenda ingresar letras, numeros y los siguientes caracteres !@#$%^&*()_+, ademas de que debe coincidir con el campo confirmpassword
#5-validacion para el campo confirmpassword, para que solo se puenda ingresar letras, numeros y los siguientes caracteres !@#$%^&*()_+, ademas de que debe coincidir con el campo password

