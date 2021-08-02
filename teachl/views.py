from django.shortcuts import render,redirect 
from django.http import HttpResponse, HttpResponseRedirect 
import string
from main.models import teacher_info
from teachl.models import *

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
    