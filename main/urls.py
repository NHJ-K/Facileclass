from django.urls import path,include
from .views import *
from teachl.views import *

urlpatterns = [
    path('',home),
    path('login',login),
    path('adminl/',include("adminl.urls")),
    path('teachl/',include("teachl.urls")),
    path('studl/',include("userl.urls")),
    path('acti/<str:tk>',activation),
    path('active',activatea,name="activatea"),
    path('fmail',forgetpassmailsend),
    #path('gauth/callback',CallbackV),
]
