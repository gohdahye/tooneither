from django.urls import path
from . import views

urlpatterns = [
    path('mon/', views.monday, name="mon"),
    path('<int:pk>/', views.ToonDetail.as_view()),
    path('', views.ToonList.as_view(), name="every"),
]