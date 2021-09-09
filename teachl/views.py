from django.db.models.fields import NullBooleanField
from django.shortcuts import render,redirect 
from django.http import HttpResponse, HttpResponseRedirect 
import string
from main.models import teacher_info
from teachl.models import *
#import google_apis_oauth
import os
from .form import DocumentForm
from main.models import teacher_info
from django.contrib import messages 
from django.contrib.messages.api import error
from django.shortcuts import redirect, render
from pyasn1.type.univ import Null
from main.models import teacher_info,user_info
from teachl.models import *
from .drive import drivedelete, driveuploader
#from us.models import studentroominfo
from django.http import HttpResponseRedirect
import string
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
# Create your views here.
gauth=GoogleAuth()
def teacp(response):
    email = response.session['mail']
    pi = teacher_info.objects.filter(Email=email)
    ls = roominfo.objects.filter(Email=email)
    context = {
        'ls':ls
    }
    return render(response,"teacher.html",{'context' : context})
    
  
    
def logout(response):   
    response.session.flush()
    return HttpResponseRedirect('/')

def gencode():
    n=10
    while True:
        code = ''.join(secrets.choice(string.ascii_letters) for x in range(n))
        if not roominfo.objects.filter(roomcode=code).exists() :
            return code

def createclass_form(request):
    return render(request,"crclass.html")

def createclass(request):
    mail = request.session['mail']
    if request.method == 'POST':
        if request.POST.get('add'):
            classname = request.POST.get('clsname')
            descr = request.POST.get('desc')
            to = roominfo(Email=mail,roomname=classname,roomdesc=descr)
            to.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def classpass(respones,cod):
     tk = respones.session['mail']
     if teacher_info.objects.filter(Email=tk).exists():
          if roominfo.objects.filter(roomcode=cod).exists():
               if not code.objects.filter(RoomCode=cod).exists():
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
               else:
                    global link
                    link=None
                    context={
                         "pdf":contends.objects.filter(RoomCode=cod),
                         "ls":code.objects.filter(RoomCode=cod),
                         "yt":youtubelink.objects.filter(RoomCode=cod),
                         "link":otherlink.objects.filter(RoomCode=cod)
                         }
                    print(context['ls'])
                    return render(respones, "innerdata.html",{'context':context})



def topicadder(responce,cod):
     if responce.method == 'POST':
          if responce.POST.get("tpadd"):
               Tpoicname=responce.POST.get("topicname")
               Tpoicdisc=responce.POST.get("description")
               p=genaratecode()
               if code.objects.filter(Tpoicname=Tpoicname).exists():
                    return HttpResponseRedirect(responce.META.get('HTTP_REFERER'))
               print(code)
               ls=code(RoomCode=cod,Tpoicname=Tpoicname,Tpoicdescrip=Tpoicdisc,UniqCode=p)
               ls.save()
               return HttpResponseRedirect(responce.META.get('HTTP_REFERER'))


def uploader(respnce,cod,tcod):
     if respnce.method == 'POST':
          if respnce.POST.get('pdfupload'):
               pdffiles=respnce.FILES.getlist('pdffiles')
               for f in pdffiles:
                    drivepassway=tempuploader(uploadfile=f,tcode=tcod)

               url=Gauthcheck(respnce)
               link=url
               context={
                         "pdf":contends.objects.filter(RoomCode=cod),
                         "ls":code.objects.filter(RoomCode=cod),
                         "yt":youtubelink.objects.filter(RoomCode=cod),
                         "link":otherlink.objects.filter(RoomCode=cod),
                         "Glink":link
                    }
               return HttpResponseRedirect(respnce.META.get('HTTP_REFERER'))
               for f in pdffiles:
                    drivepassway=tempuploader(uploadfile=f)
                    drivepassway.save()
                    ls=code.objects.get(UniqCode=tcod)

                    driveuploader(ls,drivepassway.uploadfile.path,f.name)

                    pdf= tempuploader.objects.all()
                    for pd in pdf:
                        pd.delete()
               return HttpResponseRedirect(respnce.META.get('HTTP_REFERER'))
         
          if respnce.POST.get('addlinksubmit'):
               savelink=respnce.POST.get('addlink')
               ls= code.objects.get(UniqCode=tcod)
               linksave=otherlink(RoomCode=ls.RoomCode,UniqCode=ls.UniqCode,link=savelink)
               linksave.save()
               context={
                         "pdf":contends.objects.filter(RoomCode=cod),
                         "ls":code.objects.filter(RoomCode=cod),
                         "yt":youtubelink.objects.filter(RoomCode=cod),
                         "link":otherlink.objects.filter(RoomCode=cod)
                    }
                    #del Tpoicname,Tpoicdisc,pdffiles,p
               return HttpResponseRedirect(respnce.META.get('HTTP_REFERER'))
          if respnce.POST.get('youtubelink'):
               savelink=respnce.POST.get('youtubevediolink')
               starthour=int(respnce.POST.get('starthour'))
               startminit=int(respnce.POST.get('startminit'))
               startsecond=int(respnce.POST.get('startsecond'))
               stophoure=int(respnce.POST.get('stophoure'))
               stopminite=int(respnce.POST.get('stopminite'))
               stopsecond=int(respnce.POST.get('stopsecond'))
               startin=(starthour*360)+(startminit*60)+(startsecond)
               stopin=(stophoure*360)+(stopminite*60)+(stopsecond)
               res = savelink.partition("spl_word")[2]
               if "watch?v=" in savelink:
                    res = savelink.partition("watch?v=")[2]
                    vediocode= res[0:11]
                    vedifinallink="https://www.youtube.com/embed/"+str(vediocode)+"?version=3&start="+str(startin)+"&end="+str(stopin)+"&autoplay=0&controls=0&rel=0&loop=1"

               if "youtu.be/" in savelink:
                    res = savelink.partition("youtu.be/")[2]
                    vediocode= res[0:11]
                    vedifinallink="https://www.youtube.com/embed/"+vediocode+"?version=3&start="+startin+"&end="+stopin+"&autoplay=0&controls=0&rel=0&loop=1"
               ls= code.objects.get(UniqCode=tcod)
               linksave=youtubelink(RoomCode=ls.RoomCode,UniqCode=ls.UniqCode,link=vedifinallink)
               linksave.save()
               context={
                         "pdf":contends.objects.filter(RoomCode=cod),
                         "ls":code.objects.filter(RoomCode=cod),
                         "yt":youtubelink.objects.filter(RoomCode=cod),
                         "link":otherlink.objects.filter(RoomCode=cod)
                    }
                    #del Tpoicname,Tpoicdisc,pdffiles,p
               return HttpResponseRedirect(respnce.META.get('HTTP_REFERER'))

          
          #resher with fail message





def Gauthcheck(respnce):
     url=gauth.GetAuthUrl()
     print(url)
     return url

def callback(request):
    if request.method == 'GET':
        code = request.GET.get('code')
        print(code)
        gauth.Auth(code)
        gauth.SaveCredentialsFile('creds.json')
        #pathfile= file
        #print('pass')
        ##parernt_id=folderspcifing(ls)
        #gfile = drive.CreateFile({'parents': [{'id': parernt_id}]})
        #gfile.SetContentFile(pathfile)
        #gfile.Upload() 
        #con=contends(RoomCode=ls.RoomCode,UniqCode=ls.UniqCode,pdf=gfile.get('id'),name=filename)
        #con.save()
        #def driveuploader(ls,file,filename):
        drive = GoogleDrive(gauth) 
        pdffiles=tempuploader.objects.all()
        for f in pdffiles:
                    ls=code.objects.get(UniqCode=f.tcode)
                    parernt_id=folderspcifing(ls,drive)
                    pathfile= f.uploadfile.path
                    gfile = drive.CreateFile({'parents': [{'id': parernt_id}]})
                    gfile.SetContentFile(pathfile)
                    gfile.Upload() 
                    con=contends(RoomCode=ls.RoomCode,UniqCode=ls.UniqCode,pdf=gfile.get('id'),name=f.name)
                    con.save()      
        pdf= tempuploader.objects.all()
        for pd in pdf:
           pd.delete()
        return redirect('/callback')   
        return render(request,"Teacher/test.html")

     
def folderspcifing(ls,drive):
    foder_title="WEBCLASSROOM"
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    folder_id=None
    folder_id_in=None
    for file in file_list:
        if(file['title']==foder_title):
            folder_id=file['id']
            break
    if folder_id==None:
        folder_id=createmainfolder(drive)
    children = drive.ListFile({'q': "'" + folder_id + "' in parents"}).GetList()
    for file in children:    
        if(file['title']==ls.RoomCode):
            folder_id_in=file['id']
            break
    if folder_id_in==None:
        folder_id_in=classroomfolder(ls,folder_id,drive)
    return folder_id_in
    

def createmainfolder(drive):
    folder_name="WEBCLASSROOM"
    folder=drive.CreateFile({'title':folder_name,'mimeType' : 'application/vnd.google-apps.folder'})
    folder.Upload()
    return folder.get('id')

def classroomfolder(ls,folder_id,drive):
    folder_name=ls.RoomCode
    folder=drive.CreateFile({'title':folder_name,'parents' :  [{"id": folder_id, "kind": "drive#childList"}],'mimeType' : 'application/vnd.google-apps.folder'})
    folder.Upload()
    return folder.get('id')

def genaratecode():
     n=10
     while True:
          code1=''.join(secrets.choice(string.ascii_letters) for x in range(n))
          if code.objects.filter(UniqCode=code1).count() == 0:
               return code1
