from main.models import user_info
from teachl.models import *
from .models import *
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.messages.api import error
from django.contrib import messages 


def userp(response):
    email = response.session['mail']
    ls = sroominfo.objects.filter(Email=email)
    context = {
        'ls':ls
    }
    return render(response,"upage.html",{'context':context})
    

    
def logout(response):
    response.session.flush()
    return HttpResponseRedirect('/')
    
def createclass_form(request):
    return render(request,"addpage.html")


def createclass(request):
    mail = request.session['mail']
    if request.method == 'POST':
        if request.POST.get('add'):
            classname = request.POST.get('clsname')
            if roominfo.objects.filter(Roomcode=classname).exists():
                ls=roominfo.objects.get(Roomcode=classname)
                to = sroominfo(Email=mail,Roomcode=ls.Roomcode,roomname=ls.roomname,url=ls.url,roomdesc=ls.roomdesc)
                to.save()
            else:
                messages.error(request,'Incorrept code')
        
            return redirect('/')
        return redirect('/')
    return redirect('/')



def classpass(respones,cod):
     tk = respones.session['mail']
     if user_info.objects.filter(Email=tk).exists():
          if sroominfo.objects.filter(url=cod).exists():
               context={
                         "pdf":contends.objects.filter(RoomCode=cod),
                         "ls":code.objects.filter(RoomCode=cod),
                         "yt":youtubelink.objects.filter(RoomCode=cod),
                         "link":otherlink.objects.filter(RoomCode=cod)
                         }
               return render(respones, "innerdatas.html",{'context':context})

            

