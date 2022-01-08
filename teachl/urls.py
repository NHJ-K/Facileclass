from django.urls import path,include
from .views import *


urlpatterns = [
    path('',teacp,name="my-view"),
    path('m/logout',logout,name="logout"),
    path('create',createclass_form),
    path('createc',createclass),
    path('m/<str:cod>/',classpass),
    path('m/<str:cod>/<str:tcod>/add',uploader),
    path('m/<str:cod>/tadder',topicadder),
    path('m/<str:cod>/addstud',addstud),
    path('callback',callback),
    path("m/<str:cod>/addstd",addstd),
    path('m/<str:cod>/peoples',peopl),
    #path('m/<str:cod>/delete',deletedrivefile),
]