from django.shortcuts import render, get_object_or_404, redirect
from .models import Livros, Genero, Emprestimo
from random import randint
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.utils import timezone
from email.message import EmailMessage
import smtplib


@login_required(redirect_field_name='login')
def index(request):

    livros = Livros.objects.all()
    # print(livros)
    return render(request, 'pages/index.html', {'livros':livros})

def livros_detail(request, id):
    livro = Livros.objects.get(id=id)
    return render(request, 'pages/livros_detail.html', {'livro':livro})

def search_product(request):
    q = request.GET.get('q')
    livros = Livros.objects.filter(name__icontains=q) 
    return render(request, 'pages/index.html', {'livros':livros})


# def delete_product(request, id):
#     product = Products.objects.get(id=id)
#     product.delete()
#     return redirect('home')

def rent_product(request, id):
    livro = Livros.objects.get(id=id)
    livro.qtd_livros -= 1
    livro.save()
    return redirect('home')

def return_product(request, id):
    livro = Livros.objects.get(id=id)
    livro.qtd_livros += 1
    livro.save()
    return redirect('home')

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
    

def emprestimo(request):

    emprestimos = Emprestimo.objects.all()
    
    return render(request, 'pages/teste.html', {'emprestimos': emprestimos})


def alugar_livro(request, livro_id):
    livro = get_object_or_404(Livros, id=livro_id)

    if livro.qtd_livros > 0:
       
        emprestimo = Emprestimo.objects.create(usuario=request.user, livro=livro)

        data_emprestimo = emprestimo.data_emprestimo
        prazo_devolucao = 7
        data_devolucao = data_emprestimo + timezone.timedelta(days=prazo_devolucao)

        emprestimo.data_devolucao = data_devolucao

        livro.qtd_livros -= 1
        livro.save()

        EMAIL = 'chrystian.souza.silveira@gmail.com'
        PASSWORD = 'qcfbvamhgqeiqunx'

        msg = EmailMessage()
        msg['Subject'] = 'Confirmação de Empréstimo'
        msg['From'] = EMAIL
        msg['To'] = request.user.email 
        msg.set_content(f'Você alugou o livro "{livro.nome}" em {data_emprestimo}. A data de devolução é {data_devolucao}.')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL, PASSWORD)
            smtp.send_message(msg)

        
        return render(request, 'pages/sucesso.html', {'livro': livro, 'data_emprestimo': data_emprestimo, 'data_devolucao': data_devolucao})
        render()
    else:
        return render(request, 'pages/fracasso.html', {'livro': livro})

