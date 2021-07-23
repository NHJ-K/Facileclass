from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
import string
from main.models import teacher_info
from teachl.models import *

# Create your views here.

def teacp(response):
    email = response.session['mail']
    print(email)
    pi = teacher_info.objects.filter(Email=email)
    ls = roominfo.objects.filter(Email=email)
    print(ls)
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