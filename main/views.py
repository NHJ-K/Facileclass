from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages 
from django.contrib.messages.api import error

# Create your views here.
def home(request):
    if request.session._session:
        return redirect('/login')
    return render(request,"home.html")


def login(response):
    if response.session._session:
        try:
            email = response.session['mail']
            if admin_info.objects.filter(Email=email):
                return redirect('/adminl')
            elif teacher_info.objects.filter(Email=email):
                return redirect('/teachl')
            elif user_info.objects.filter(Email=email):
                return redirect('studl')
        except KeyError:
            pass
    if response.method == 'POST':
        if response.POST.get("signin"):
            email = response.POST.get("UL_email")
            password = response.POST.get("UL_pass")
            if admin_info.objects.filter(Email = email).exists():
                to = admin_info.objects.get(Email=email)
                response.session['mail'] = email
                if to.passwords == password:
                    return redirect('/adminl')
                else:
                    messages.error(response,'Password incorrect')
                    return redirect('/')
            elif teacher_info.objects.filter(Email=email).exists():
                to = teacher_info.objects.get(Email=email)
                response.session['mail'] = email
                if to.Activate == False:
                    messages.error(response,'Account is not Activated')
                    return redirect('/')
                if to.passwords == password:
                    return redirect('/teachl')
                else:
                    messages.error(response,'Password Incorrect')
                    return redirected('/')
            elif user_info.objects.filter(Email=email).exists():
                to = user_info.objects.get(Email=email)
                if to.passwords == password:
                    return redirect('/studl')
                else:
                    messages.error(response,'Password incorrect')
            else:
                messages.error(response,'Email not found')
                return redirect('/')
    return render(response,"home.html")

def actrender(request):
    return render(request,"mailvar.html")

def activate(request):
    if request.method == 'POST':
        mail = request.POST.get("U_email")
        if request.POST.get("teachersubmit"):
            if teacher_info.objects.filter(Email=mail).exists():
                name = request.POST.get("U_name1")
                password = request.POST.get("U_password1")
                teacher_info.objects.filter(Email=mail).update(Name=name,passwords=password,Activate=True)
                messages.success(request,"Activated")
                return redirect('/')
            else:
                messages.error(request, "Email not Found contact site administrator")
    return redirect('/')