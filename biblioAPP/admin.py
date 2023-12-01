from django.contrib import admin
from .models import Livros, Genero, Emprestimo

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id','nome', 'genero','in_stock']
    list_filter = ['in_stock']
    # list_editable = ['size']
    search_fields = ['name']


admin.site.register(Livros, ProductsAdmin)
admin.site.register(Genero)
admin.site.register(Emprestimo)

                    

# Register your models here.
