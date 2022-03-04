from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView

from toon.forms import ToonForm
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
    form_class = ToonForm
    template_name = 'toon/toon_form.html'

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(ToonCreate, self).form_valid(form)
        else:
            return redirect('/')


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