from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from posts.models import *

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20)
    birthday = models.DateField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
