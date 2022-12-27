from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(ShopOrder)
admin.site.register(ShopOrderItems)
admin.site.register(OrderStatus)