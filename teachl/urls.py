from django.urls import path,include
from .views import *


urlpatterns = [
    path('',teacp),
    path('m/logout',logout,name="logout"),
    path('create',createclass_form),
    path('createc',createclass),
    path('m/<str:cod>',topicv),
    path('gauth',googleauth),
    path('gauth/callback',CallbackV),
]