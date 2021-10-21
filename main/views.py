from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages 
from django.contrib.messages.api import error
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
def forgetpass(response):
    pass

def forgetpassmailsend(respnes):
    pass

def activation(request,tk):
    return render(request,"mailvar.html")

def activatea(request):
    print('activate')
    if request.method == 'POST':
        email = request.POST.get("U_email")
        name = request.POST.get("U_name1")
        passwrd = request.POST.get("U_password1")
        if user_info.objects.filter(Email=email).exists():
            user_info.objects.filter(Email=email).update(Activate=True,passwords=passwrd,Name=name)
            messages.error(request, 'Your acount is Activated')
            request.session['mail'] = email
            return redirect('studl/')
        elif teacher_info.objects.filter(Email=email).exists():
            teacher_info.objects.filter(Email=email).update(Activate=True,passwords=passwrd,Name=name)
            messages.error(request, 'Your acount is Activated')
            request.session['mail'] = email
            return redirect('teachl/')
        else:
            messages.error(request, 'Email not found Contact Admin')
            return redirect('/')
    return render(request,"mailvar.html")
        


            