from django.urls import path,include
from .views import *


urlpatterns = [
    path('',userp),
    path('logout',logout,name="logout")
]