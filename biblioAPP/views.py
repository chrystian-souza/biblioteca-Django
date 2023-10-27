from django.shortcuts import render, redirect
# from .models import Products, Categorias 
from random import randint
from datetime import datetime

def product_detail(request, id):
    product = Products.objects.get(id=id)
    return render(request, 'pages/product_detail.html', {'product':product})