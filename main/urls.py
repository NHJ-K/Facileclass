from django.urls import path,include
from .views import *


urlpatterns = [
    path('',home),
    path('login',login),
    path('adminl/',include("adminl.urls")),
    path('teachl/',include("teachl.urls")),
    path('studl/',include("userl.urls")),
    path('activate',actrender),
    path('activetea',activate),
]
