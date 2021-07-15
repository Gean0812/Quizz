from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quizz/', views.quizz, name='quizz'),
    path('create/', views.create, name='create'),
    path('game/', views.game, name='game'),
    path('responde/', views.responde, name='responde'),
    path('saveans/', views.saveans, name='save'),
]