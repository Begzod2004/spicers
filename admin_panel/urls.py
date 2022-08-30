from django.urls import *
from .views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',index, name='dashboard'),
    path('dashboard1/', index, name='dashboard1'),
    path('dashboard2/', index1, name='dashboard2'),
    ] 
