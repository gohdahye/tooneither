from django.urls import path
from . import views

urlpatterns = [
    path('create_toon/', views.ToonCreate.as_view(), name="create"),
    path('<str:slug>/', views.days_page),
    path('<str:slug>/<int:pk>/', views.ToonDetail.as_view()),
    path('', views.ToonList.as_view(), name="home"),
]