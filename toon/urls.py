from django.urls import path
from . import views

urlpatterns = [
    path('mon/', views.mon, name="mon" ),
    path('', views.home, name="home" ),
]