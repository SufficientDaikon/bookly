from django.db import models

# Create your models here.


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)