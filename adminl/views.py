from django.shortcuts import render,redirect
from main.models import *
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect 
from main.mailsender import *
# Create your views here.

def adminp(response):
    try:
        mail = response.session['mail']
        ls=teacher_info.objects.all()
        return render(response,"admin.html",{'ls':ls})
    except KeyError:
        return HttpResponseRedirect('/')

def logout(response):   
    response.session.flush()
    return HttpResponseRedirect('/')

def gencode():
    n=60
    while True:
        code=''.join(secrets.choice(string.ascii_letters) for x in range(n))
        if not teacher_info.objects.filter(token=code).exists():
            if not user_info.objects.filter(token=code).exists():
                if not admin_info.objects.filter(token=code).exists():
                    return code

def addteach(request):
    if request.method=='POST':
        if request.POST.get('add'):
            T_mail = request.POST.get('emailadd')
            if not admin_info.objects.filter(Email=T_mail).exists():
                if not teacher_info.objects.filter(Email=T_mail).exists():
                    if not user_info.objects.filter(Email=T_mail).exists():
                        ps = teacher_info(Email=T_mail,token=gencode())
                        ps.save()
                        SUBJECT = "Activate your Account"
                        TEXT = "Follow the link to activate your Account "
                        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
                        l = mailsender(ps.token,T_mail,message)
                        messages.error(request,"Updated")
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                    else:
                        messages.error(request,"Email already exists")
                        ls = teacher_info.objects.all()
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.error(request,"Email already exists")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request,"Email already exists")
                ls = teacher_info.objects.all()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
