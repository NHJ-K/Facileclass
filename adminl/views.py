from django.shortcuts import render,redirect
from main.models import *
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect 
from main.sendmail import *
# Create your views here.

def adminp(response):
    ls=teacher_info.objects.all()
    return render(response,"admin.html",{'ls':ls})
    
  
    
def logout(response):   
    response.session.flush()
    return HttpResponseRedirect('/')

def addteach(request):
    if request.method=='POST':
        if request.POST.get('add'):
            T_mail = request.POST.get('emailadd')
            if not admin_info.objects.filter(Email=T_mail).exists():
                if not teacher_info.objects.filter(Email=T_mail).exists():
                    if not user_info.objects.filter(Email=T_mail).exists():
                        ps = teacher_info(Email=T_mail)
                        ps.save()
                        SUBJECT = "Activate your Account"
                        TEXT = "Follow the link to activate your Account"
                        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
                        l = mailsender(T_mail,message)
                        ls = teacher_info.objects.all()
                        return HttpResponseRedirect('/adminl')
                    else:
                        messages.error(request,"Email already exists")
                        ls = teacher_info.objects.all()
                        return render(request,"admin.html",{'ls':ls})
                else:
                    messages.error(request,"Email already exists")
                    ls = teacher_info.objects.all()
                    return render(request,"admin.html",{'ls':ls})
            else:
                messages.error(request,"Email already exists")
                ls = teacher_info.objects.all()
                return render(request,"admin.html",{'ls':ls})
