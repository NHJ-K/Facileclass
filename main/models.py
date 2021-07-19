from django.db import models
from datetime import datetime
# Create your models here.

class admin_info(models.Model):
    Name = models.CharField(max_length=50,unique=False,blank=False)
    Email = models.CharField(max_length=100,unique=True,blank=False,editable=True)
    passwords = models.CharField(max_length=50,unique=False,blank=False,editable=True)
    

class teacher_info(models.Model):
    Name = models.CharField(max_length=50,unique=False,blank=False)
    Email = models.CharField(max_length=100,unique=True,blank=False,editable=True)
    passwords = models.CharField(max_length=100,unique=False,blank=False,editable=True)
    Activate = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)


class user_info(models.Model):
    Name=models.CharField(max_length=50,unique=False,blank=False)
    Email=models.CharField(max_length=100,unique=True,blank=False,editable=True)
    passwords=models.CharField(max_length=50,unique=False,blank=False,editable=True)
    Activate=models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)