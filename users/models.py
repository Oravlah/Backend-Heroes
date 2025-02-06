from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.core.validators import RegexValidator
import uuid

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class Users(AbstractBaseUser):
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

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'fullname', 'age']

    def __str__(self):
        return self.email
