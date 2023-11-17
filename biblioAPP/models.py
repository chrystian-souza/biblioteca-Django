from django.db import models


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
    qtd_paginas = models.IntegerField()
    qtd_livros = models.IntegerField()
    imagem = models.ImageField(blank=False)
    autor = models.CharField(max_length=255)
    created_at = models.DateField()
    in_stock = models.BooleanField(default=False)

    def _str_(self):
        return self.nome 
    
    class Meta:
            verbose_name = 'Livros'
            verbose_name_plural = 'Livros'  