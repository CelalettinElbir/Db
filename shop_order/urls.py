from django.contrib import admin
from django.urls import path
from .views import shopOrderListView, shopOrderDetailView


urlpatterns = [
    path('', shopOrderListView.as_view(), name="orders"),
    path('<int:pk>', shopOrderDetailView.as_view(), name="order-detail"),

]
