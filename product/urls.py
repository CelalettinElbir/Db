from django.contrib import admin
from django.urls import path
from .views import index, category_products, product_detail


urlpatterns = [
    path("", index,name= "home"),
    path("product/<slug:slug>-<int:id>", product_detail, name="product_detail"),

    path('category/<int:id>',
         category_products, name='category_products'),
]
