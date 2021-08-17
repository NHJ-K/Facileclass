from django.urls import path,include
from .views import *


urlpatterns = [
    path('',teacp),
    path('logout',logout,name="logout"),
    path('create',createclass_form),
    path('createc',createclass),
    path('m/<str:cod>',topicv),
]