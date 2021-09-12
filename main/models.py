from django.db import models
from datetime import datetime
import secrets
import string

from pytz import timezone
# Create your models here.

def gencode():
    n=60
    while True:
        code=''.join(secrets.choice(string.ascii_letters) for x in range(n))
        if not teacher_info.objects.filter(token=code).exists():
            if not user_info.objects.filter(token=code).exists():
                if not admin_info.objects.filter(token=code).exists():
                    return code

    

class admin_info(models.Model):

    Name = models.CharField(max_length=50,unique=False,blank=False)
    Email = models.CharField(max_length=100,unique=True,blank=False,editable=True)
    passwords = models.CharField(max_length=50,unique=False,blank=False,editable=True)
    token=models.CharField(max_length=70,default=None)





class teacher_info(models.Model):
    Name = models.CharField(max_length=50,unique=False,blank=False)
    Email = models.CharField(max_length=100,unique=True,blank=False,editable=True)
    passwords = models.CharField(max_length=100,unique=False,blank=False,editable=True)
    Activate = models.BooleanField(default=False)
    token=models.CharField(max_length=70,default=None)
    created_at = models.DateTimeField(default=datetime.now())
    

class user_info(models.Model):
    Name=models.CharField(max_length=50,unique=False,blank=False)
    Email=models.CharField(max_length=100,unique=True,blank=False,editable=True)
    passwords=models.CharField(max_length=50,unique=False,blank=False,editable=True)
    token=models.CharField(max_length=70,default=None)
    Activate=models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now())
    




