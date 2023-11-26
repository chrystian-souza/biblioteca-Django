from django.shortcuts import render, redirect
from .models import Livros, Genero
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

def search_product(request):
    q = request.GET.get('q')
    livros = Livros.objects.filter(name__icontains=q) 
    return render(request, 'pages/index.html', {'livros':livros})

# def delete_product(request, id):
#     product = Products.objects.get(id=id)
#     product.delete()
#     return redirect('home')

# def sell_product(request, id):
#     product = Products.objects.get(id=id)
#     product.qtd -= 1
#     product.save()
#     return redirect('product-detail', id)

def add_livro(request):

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cod = randint(100, 10000)
        genero = request.POST.get('genero')
        imagem = request.FILES.get('imagem')
        preco = request.POST.get('preco')
        descricao = request.POST.get('descricao')
        qtd_paginas = request.POST.get('qtd_paginas')
        qtd_livros = request.POST.get('qtd_livros')
        desconto = request.POST.get('desconto')
        criado_em  = datetime.now()
        em_estoque= True

        Livros.objects.create(
            user_id=request.user.id,
            name=nome, cod=cod, genero_id=genero, imagem=imagem,
            preco=preco, descricao=descricao, qtd_paginas=qtd_paginas,qtd_livros=qtd_livros, desconto=desconto,
            criado_em=criado_em, em_estoque=em_estoque
        )

        return redirect('home')

    else:

        genero = Genero.objects.all()
        return render(request, 'pages/add_livro.html', {'genero': genero})