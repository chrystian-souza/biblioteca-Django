from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', views.index, name='home'),
    path('search-product/', views.search_product, name='search_product'),
    path('add-livro/', views.add_livro, name='add_livro'),
    path('rent-product/<int:id>/', views.rent_product, name='rent_product'),
    path('return-product/<int:id>/', views.return_product, name='return_product'),
    path('livros_detail/<int:id>', views.livros_detail, name='livros-detail'),
    path('teste/', views.emprestimo, name='teste'),
    path('sucesso/<int:livro_id>/', views.alugar_livro, name='sucesso'),
    path('logout/',  LogoutView.as_view(), name='logout'),
    path('livros_detail/', views.index, name='voltar')
    # path('delete-product/<int:id>/', views.delete_product, name='delete-product')


]  
