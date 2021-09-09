from datetime import date
from django.core.files import storage
from django.db import models
import string
import secrets
from django.db.models.base import Model
# Create your models here.
from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()

class Map(models.Model):
    id = models.AutoField( primary_key=True)
    map_name = models.CharField(max_length=200)
    map_data = models.FileField(upload_to='maps', storage=gd_storage)

def gencode():
    n=7
    while True:
        code=''.join(secrets.choice(string.ascii_letters) for x in range(n))
        if roominfo.objects.filter(roomcode=code).count() == 0:
            return code
#room details
class roominfo(models.Model):
    Email=models.CharField(max_length=50)
    roomcode=models.CharField(default=gencode,max_length=7,primary_key=True)
    roomname=models.CharField(max_length=100)
    roomdesc=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)

#topic specific code
class code(models.Model):
    RoomCode=models.CharField(max_length=7)
    Tpoicname=models.CharField(max_length=100)
    Tpoicdescrip=models.CharField(max_length=2000)
    UniqCode=models.CharField(max_length=10)
    date=models.DateTimeField(auto_now_add=True)

#topic condent pdf
class contends(models.Model):
    RoomCode=models.CharField(max_length=7)
    UniqCode=models.CharField(max_length=10)
    pdf = models.CharField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=200)
#temp pdf file
class tempuploader(models.Model):
    uploadfile=models.FileField(upload_to='media')
    tcode=models.CharField(max_length=20)
    def delete(self,*args, **kwargs):
        self.uploadfile.delete()
        super().delete(*args,**kwargs)
#topic condent youtube link
class youtubelink(models.Model):
    RoomCode=models.CharField(max_length=7)
    UniqCode=models.CharField(max_length=10)
    link = models.CharField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)

#topic condent other driev,site link
class otherlink(models.Model):
    RoomCode=models.CharField(max_length=7)
    UniqCode=models.CharField(max_length=10)
    link = models.CharField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)