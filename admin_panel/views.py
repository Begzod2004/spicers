from unicodedata import *
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import  render
from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'dashboard/index.html')
        
def index1(request):
    return render(request, 'dashboard/index-1.html')    