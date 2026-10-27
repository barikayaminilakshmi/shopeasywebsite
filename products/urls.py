from django.urls import path
from . import views

urlpatterns = [

    path('', views.product_list, name="products"),

    path(
        'category/<str:category_name>/',
        views.category_products,
        name="category_products"
    ),

]