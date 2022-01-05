from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# from .managers import CustomUserManager


from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser 




class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=200, unique=True)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    

    def __str__(self):
        return self.email