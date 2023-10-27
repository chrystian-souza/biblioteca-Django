from django.urls import path
from . import views


urlpatterns = [
    path('product-detail/<int:id>', views.product_detail, name='product-detail')

]  
