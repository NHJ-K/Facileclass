from django.urls import path,include
from .views import *


urlpatterns = [
    path('',adminp),
    path('logout',logout,name="logout"),
    path('tadder',addteach),
]