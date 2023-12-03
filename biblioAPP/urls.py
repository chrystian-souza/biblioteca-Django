from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', views.index, name='home'),
    path('search-product/', views.search_product, name='search-product'),
    path('add-livro/', views.add_livro, name='add_livro'),
    # path('sell-product/<int:id>/', views.sell_product, name='sell-product'),
    path('livros_detail/<int:id>', views.livros_detail, name='livros-detail'),
    path('teste/', views.emprestimo, name='teste'),
    path('logout/',  LogoutView.as_view(), name='logout'),
    # path('delete-product/<int:id>/', views.delete_product, name='delete-product')


]  
