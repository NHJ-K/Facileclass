from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
# Create your views here.

def adminp(response):
    return render(response,"admin.html")
    
  
    
def logout(response):   
    print("hi")
    response.session.flush()
    return HttpResponseRedirect('/')

