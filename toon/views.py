from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView

from toon.models import Toon, Days


class ToonList(ListView):
    model = Toon
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(ToonList, self).get_context_data()
        context['days'] = Days.objects.all()

        return context


class ToonDetail(DetailView):
    model = Toon
    def get_context_data(self, **kwargs):
        context = super(ToonDetail, self).get_context_data()
        context['days'] = Days.objects.all()

        return context


class ToonCreate(CreateView):
    model = Toon
    fields = ['title', 'file_image', 'day']


def days_page(request, slug):
    try:
        day = Days.objects.get(slug=slug)
    except Days.DoesNotExist:
        day = None

    return render(
        request,
        'toon/days.html',
        {
            'toon_list': Toon.objects.filter(day=day),
            'days': Days.objects.all(),
            'day':day,
        }

    )