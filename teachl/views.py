from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 

# Create your views here.

def teacp(response):
    email = response.session['mail']
    
    return render(response,"teacher.html")
    
  
    
def logout(response):   
    print("hi")
    response.session.flush()
    return HttpResponseRedirect('/')