from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager # Assuming you have a CustomUserManager defined in a managers.py file
from datetime import datetime
# Create your models here.


class CustomManager(models.Manager):
    def get_queryset(self):
        return super(__class__, self).get_queryset().filter(is_deleted=False)


class BaseAbstractStructure(models.Model):
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey('user_profile.User', on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    updated_by = models.ForeignKey('user_profile.User', on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    cmobjects = CustomManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        super(__class__, self).save(*args, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom User Model """
    user_type = (
        ('employee', 'Employee'),
        ('customer', 'Customer')
    )

    username= models.CharField(max_length=255, unique=True)
    password= models.CharField(max_length=255)
    email= models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone= models.CharField(max_length=10, blank=True, null=True, unique=True)
    user_type = models.CharField(max_length=100, choices=user_type, blank=True, null=True, default="employee")
    
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
    


class Role(BaseAbstractStructure):
    """ Role Model """
    designation = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.designation


    

class EmployeeProfile(BaseAbstractStructure):
    """ Employee Profile Model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)
    emp_code = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    email= models.EmailField(max_length=200, unique=True)
    phone= models.CharField(max_length=10, blank=True, null=True, unique=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    




