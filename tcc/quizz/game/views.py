from random import random

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator, EmptyPage, InvalidPage

lst = []
anslist = []
answers = Pergunta.objects.all()
for i in answers:
    anslist.append(i.resposta)

def index(request):
    return render(request, 'inicio.html')

def quizz(request):
    return render(request, 'form.html')

def create(request):
    req = request
    nome = req.GET['name']
    email = req.GET['email']
    try:
        usuario = Usuario(nome=nome, email=email, score=0)
        usuario.save()

        return render(request, 'start.html')
    except ValueError as e:
        raise ValueError(e)

def game(request):
    obj = Pergunta.objects.all()
    paginator = Paginator(obj, 1)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        perguntas = paginator.page(page)
    except(EmptyPage, InvalidPage):
        perguntas = paginator.page(paginator.num_pages)
    return render(request, 'questions.html', {"obj": obj, "perguntas": perguntas})

def responde(request):
    score = 0
    for i in range(len(lst)):
        if lst[i] == anslist[i]:
            score += 1
    return render(request, 'result.html', {"score": score})

def saveans(request):
    ans = request.GET['ans']
    lst.append(ans)