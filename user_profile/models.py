from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager # Assuming you have a CustomUserManager defined in a managers.py file
# Create your models here.



class User(AbstractBaseUser, PermissionsMixin):

    username= models.CharField(max_length=255, unique=True)
    password= models.CharField(max_length=255)
    email= models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone= models.CharField(max_length=10, blank=True, null=True, unique=True)


    # required fields

    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

