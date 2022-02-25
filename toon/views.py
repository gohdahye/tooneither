from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from toon.models import Toon


class ToonList(ListView):
    model = Toon
    ordering = '-pk'


class ToonDetail(DetailView):
    model = Toon



def monday(request):
    toons = Toon.objects.all()
    return render(
        request,
        'toon/monday.html',
        {
            'toons' : toons,
        }

    )