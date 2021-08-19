from django.shortcuts import render,redirect 
from django.http import HttpResponse, HttpResponseRedirect 
import string
from main.models import teacher_info
from teachl.models import *
import google_apis_oauth
import os
from main.models import teacher_info
from django.contrib import messages 
from django.contrib.messages.api import error

# Create your views here.

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

def crclass(request):
    if request.method == 'POST':
        if response.POST.get("addclass"):
            pass

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
            return redirect('/teachl')


def topicv(request,cod):
    mail = request.session['mail']
    if teacher_info.objects.filter(Email=mail).exists():
        if roominfo.objects.filter(roomcode=cod).exists():
            return render(request,"roomp.html")

def googleauth(request):
    REDIRECT_URI = "http://127.0.0.1:8000/gauth/callback"
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    JSON_FILEPATH = os.path.join(os.getcwd(), 'client_id.json')
    oauth_url = google_apis_oauth.get_authorization_url(JSON_FILEPATH, SCOPES, REDIRECT_URI)
    return HttpResponseRedirect(oauth_url)

def CallbackV(request):
    teacher_info.isAuthenticated = True
    messages.error(request, "Authenticated")
    return redirect('/')