from django.shortcuts import render, redirect
from .models import Livros
from random import randint
from datetime import datetime
from django.contrib.auth.decorators import login_required


def index(request):

    livros = Livros.objects.all()
    print(livros)
    return render(request, 'pages/index.html', {'livros':livros})

def livros_detail(request, id):
    livros = Livros.objects.get(id=id)
    return render(request, 'pages/livros_detail.html', {'livros':livros})