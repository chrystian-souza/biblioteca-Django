from django.db import models
from django.contrib.auth.models import User


class Genero(models.Model):
    nome = models.CharField(max_length=255)

    
    def __str__(self):
        return self.nome
    
    
    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Genero' 


class Livros(models.Model):

   
    nome = models.CharField(max_length=255)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, blank=True)
    # aluno = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    qtd_paginas = models.IntegerField()
    qtd_livros = models.IntegerField()
    imagem = models.ImageField(blank=False)
    autor = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    desconto = models.IntegerField()
    created_at = models.DateField()
    in_stock = models.BooleanField(default=False)

    def _str_(self):
        return self.nome 
    
    class Meta:
            verbose_name = 'Livros'
            verbose_name_plural = 'Livros'  


class Emprestimo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    livro = models.ForeignKey(Livros, on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = 'Emprestimo'
        verbose_name_plural = 'Emprestimo'
   