from django.db import models
from django.contrib.auth.models import (AbstractBaseUser , BaseUserManager , PermissionsMixin)
from django.utils.translation import gettext_lazy as _






class UserManager(BaseUserManager):
    def create_user (self,username,password,**extra_field):
        if not username:
            raise ValueError (_('the username must be set'))
        user = self.model(username=username,**extra_field)
        user.set_password(password)
        user.save()
        return user
    def create_superuser (self,username,password,**extra_field):
        extra_field.setdefault('is_superuser',True)
        extra_field.setdefault('is_staff',True)
        extra_field.setdefault('is_active',True)
        if extra_field.get('is_staff') is not True:
            raise ValueError(_('superuser must have is_staff=True'))
        if extra_field.get('is_superuser') is not True:
            raise ValueError(_('superuser must have is_superuser=True'))
        if extra_field.get('is_active') is not True:
            raise ValueError(_('superuser must have is_active=True'))
        return self.create_user(username,password,**extra_field)


class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True , null=True)
    username = models.CharField(max_length=100,unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.username
    
    def save(self,*args ,**kwargs):
        if self.email:
            self.email = self.email.lower().strip()
        super().save(*args,**kwargs)

