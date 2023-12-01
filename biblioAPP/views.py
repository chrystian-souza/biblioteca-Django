from django.shortcuts import render, redirect
from .models import Livros, Genero
from random import randint
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')
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
        genero = request.POST.get('genero')
        imagem = request.FILES.get('imagem')
        preco = request.POST.get('preco')
        qtd_paginas = request.POST.get('qtd_paginas')
        qtd_livros = request.POST.get('qtd_livros')
        desconto = request.POST.get('desconto')
        criado_em  = datetime.now()
        em_estoque= True

        Livros.objects.create(
           
            nome=nome, genero_id=genero, imagem=imagem,
            preco=preco, qtd_paginas=qtd_paginas,qtd_livros=qtd_livros, desconto=desconto,
            created_at=criado_em, in_stock=em_estoque
        )

        return redirect('home')

    else:

        genero = Genero.objects.all()
        return render(request, 'pages/add_livro.html', {'generos': genero})
    

# def emprestimo(request):

