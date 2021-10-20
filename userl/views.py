from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
# Create your views here.

def userp(response):
    try:
        mail = response.session['mail']
        return render(response,"userp.html")
    except KeyError:
        return HttpResponseRedirect('/')    
  
    
def logout(response):   
    print("hi")
    response.session.flush()
    return HttpResponseRedirect('/')

