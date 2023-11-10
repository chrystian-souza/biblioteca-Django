from django.urls import path
from . import views


urlpatterns = [
     path('', views.index, name='home'),
    path('livros_detail/<int:id>', views.livros_detail, name='livros-detail')

]  
