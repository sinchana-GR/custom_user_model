from django.db import models

# Create your models here.
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin

class Userprofilemanager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('user must have value error')
        ne=self.normalize_email(email)
        upo=self.model(email=ne,first_name=first_name,last_name=last_name)
        upo.set_password(password)
        upo.save()
        return upo
    def create_superuser(self,email,first_name,last_name,password):
        upo=self.create_user(email,first_name,last_name,password)
        upo.is_staff=True
        upo.is_superuser=True
        upo.save()



class Userprofile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=100,primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    objects=Userprofilemanager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']