from django.urls import path
from . import views

urlpatterns = [
    path('mon/', views.ToonList.as_view(), name="mon"),
]