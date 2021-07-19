from django.urls import path,include
from .views import *


urlpatterns = [
    path('',teacp),
    path('logout',logout,name="logout")
]