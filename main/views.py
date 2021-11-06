from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from main.mailsender import mailsender
from .models import *
from django.contrib import messages 
from django.contrib.messages.api import error,success
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def home(request):
    if request.session._session:
        return redirect('/login')
    return render(request,"index.html")


def login(response):
    if response.session._session:
        try:
            email = response.session['mail']
            if admin_info.objects.filter(Email=email):
                return redirect('/adminl/')
            elif teacher_info.objects.filter(Email=email):
                return redirect('/teachl/')
            elif user_info.objects.filter(Email=email):
                return redirect('/studl/')
        except KeyError:
            pass
    if response.method == 'POST':
        if response.POST.get("signin"):
            email = response.POST.get("UL_email")
            print(email)
            password = response.POST.get("UL_pass")
            if admin_info.objects.filter(Email = email).exists():
                to = admin_info.objects.get(Email=email)
                if to.passwords == password:
                    response.session['mail'] = email
                    return redirect('/adminl/')
                else:
                    messages.error(response,'Password incorrect')
                    return redirect('/')
            elif teacher_info.objects.filter(Email=email).exists():
                to = teacher_info.objects.get(Email=email)
                if to.Activate == False:
                    messages.error(response,'Account is not Activated')
                    return redirect('/')
                if to.passwords == password:
                    response.session['mail'] = email
                    return redirect('/teachl/')
                else:
                    messages.error(response,'Password Incorrect')
                    return redirect('/')
            elif user_info.objects.filter(Email=email).exists():
                to = user_info.objects.get(Email=email)
                if to.passwords == password:
                    response.session['mail'] = email
                    return redirect('/studl/')
                else:
                    messages.error(response,'Password incorrect')
            else:
                messages.error(response,'Email not found')
                return redirect('/')
    return render(response,"index.html")
    
def forgetpassmailsend(request):
    if request.method == "POST":
        print("hi")
        if request.POST.get("btnpass"):
            print("hh")
            mail = request.POST.get("U_email")
            print(mail)
            if not admin_info.objects.filter(Email=mail).exists():
                if not teacher_info.objects.filter(Email=mail).exists():
                    if not user_info.objects.filter(Email=mail).exists():
                        messages.error("Email Does not exist")
                    else:
                        tk = user_info.objects.get(Email=mail)
                        subject = "Password Reset Link"
                        text = "Follow the link to change your password"
                        message = 'Subject: {}\n\n{}'.format(subject,text)
                        mailsender(tk,mail,message)
                        messages.success("Mail sented successfully")
                        return HttpResponseRedirect('/')
                else:
                        tk = teacher_info.objects.get(Email=mail)
                        print(tk)
                        subject = "Password Reset Link"
                        text = "Follow the link to change your password"
                        message = 'Subject: {}\n\n{}'.format(subject,text)
                        mailsender(tk,mail,message)
                        messages.success("Mail sented successfully")
                        return HttpResponseRedirect('/')
            else:
                messages.error("contact developer")
    return HttpResponseRedirect('/')




def activation(request,tk):
    try:
        ls = teacher_info.objects.filter(token=tk)
        mail = ls[0].Email
        request.session['mail'] = mail
    except :
        pass
    return render(request,"mailvar.html")

def activatea(request):
    email = request.session['mail']
    if request.method == 'POST':
        name = request.POST.get("U_name1")
        passwrd = request.POST.get("U_password1")
        if user_info.objects.filter(Email=email).exists():
            user_info.objects.filter(Email=email).update(Activate=True,passwords=passwrd,Name=name)
            messages.error(request, 'Your acount is Activated')
            request.session['mail'] = email
            return redirect('/')
        elif teacher_info.objects.filter(Email=email).exists():
            teacher_info.objects.filter(Email=email).update(Activate=True,passwords=passwrd,Name=name)
            messages.error(request, 'Your acount is Activated')
            request.session['mail'] = email
            return redirect('/')
        else:
            messages.error(request, 'Email not found Contact Admin')
            return redirect('/')
    return render(request,"mailvar.html")
        


            