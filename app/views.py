from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from app.models import *

class Herolist(ListView):
    model=Heros
    context_object_name='hero'
    #ordering=['name']
    