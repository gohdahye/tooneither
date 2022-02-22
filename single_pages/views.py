from django.shortcuts import render

# Create your views here.


# main page
def home(request):
    return render(
        request,
        'single_pages/landing.html'
    )
