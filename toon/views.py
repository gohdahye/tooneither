from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from toon.models import Toon


class ToonList(ListView):
    model = Toon
    ordering = '-pk'
