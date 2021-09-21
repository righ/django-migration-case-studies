from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class User(AbstractBaseUser):
    USERNAME_FIELD = 'email'
    
    email = models.EmailField(max_length=255, unique=True)
    nickname = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
