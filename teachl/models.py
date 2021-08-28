from django.db import models
import string
import secrets

# Create your models here.

def gencode():
    n=7
    while True:
        code = ''.join(secrets.choice(string.ascii_letters) for x in range(n))
        if not roominfo.objects.filter(roomcode=code).exists() :
            return code

class roominfo(models.Model):
    Email=models.CharField(max_length=50)
    roomcode=models.CharField(default=gencode,max_length=7,primary_key=True)
    roomname=models.CharField(max_length=100)
    roomdesc=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)


class googlecreds(models.Model):
    pass

class Document(models.Model):
    roomcode=models.CharField(default=gencode,max_length=7)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')