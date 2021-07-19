from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
# Create your views here.

def userp(response):
    return render(response,"userp.html")
    
  
    
def logout(response):   
    print("hi")
    response.session.flush()
    return HttpResponseRedirect('/')

