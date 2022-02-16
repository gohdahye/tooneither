from django.shortcuts import render

# Create your views here.


def home(request):
    return render(
        request,
        'toon/home.html'
    )

def mon(request):
    return render(
        request,
        'toon/mon.html'
    )