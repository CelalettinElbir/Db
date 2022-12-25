from django.db import models
from user.models import *
# Create your models here.

# Todo: her kullanıcının birden fazla şiparişi var 




class ShopOrder(models.Model):
    user = models.ForeignKey(Person, models.DO_NOTHING)
    order_date = models.DateField(blank=True, null=True)
    address = models.ForeignKey(Adress, models.DO_NOTHING)
    order_total = models.IntegerField(blank=True, null=True)


class OrderStatus(models.Model):
    choices = (('Received', 'Received'),
               ('Scheduled', 'Scheduled'),
               ('Shipped', 'Shipped'),
               ('In Progress', 'In Progress'),
               )
    shop_order = models.ForeignKey(ShopOrder, models.DO_NOTHING)
    status = models.Choices(
        max_length=45, choices=choices, blank=True, null=True)



class ShopOrderItems(models.Model):
    shop_order = models.ForeignKey(ShopOrder, models.DO_NOTHING)
    product_item = models.ForeignKey(Item, models.DO_NOTHING)
    price = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

