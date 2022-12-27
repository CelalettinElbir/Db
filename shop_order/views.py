from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import *

# Create your views here.

# TODO: fişleri görüntüle
# kullancı ürünlere yorum bırakabilecek.
# satın alma sayfasında adres seçme ve kredi kartı seçme yapılacak.


class shopOrderListView(ListView):
    model = ShopOrder
    context_object_name = 'shop_orders'
    template_name = 'order/index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        person = Person.objects.get(user=self.request.user)
        context['shop_order'] = ShopOrder.objects.filter(user=person)

        return context


class shopOrderDetailView(DetailView):
    model = ShopOrder
    template_name = 'order/detail.html'
    context_object_name = 'shop_order'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total = 0
        context["shop_order_items"] = ShopOrderItems.objects.filter(shop_order = self.kwargs["pk"])
        for i in  ShopOrderItems.objects.filter(shop_order = self.kwargs["pk"]):
            total += i.price*i.quantity

        context["total"] = total

        return context



