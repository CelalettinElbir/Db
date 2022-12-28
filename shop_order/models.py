from django.db import models

# Create your models here.

# Todo: her kullanıcının birden fazla şiparişi var


class ShopOrder(models.Model):
    user = models.ForeignKey("user.Person", models.DO_NOTHING)
    order_date = models.DateField(auto_now_add=True,blank=True,null=True)
    address = models.ForeignKey("user.Adress", models.DO_NOTHING)
    order_total = models.IntegerField(blank=True, null=True)
    order_status = models.ForeignKey("OrderStatus", models.DO_NOTHING,blank=True,null=True)


class OrderStatus(models.Model):
    choices = (('Received', 'Received'),
               ('Scheduled', 'Scheduled'),
               ('Shipped', 'Shipped'),
               ('In Progress', 'In Progress'),
               )
    status = models.CharField(
        max_length=45, choices=choices, blank=True, null=True, default="In Progress")


class ShopOrderItems(models.Model):
    shop_order = models.ForeignKey(ShopOrder, models.DO_NOTHING,related_name="items")
    product_item = models.ForeignKey("product.Item", models.DO_NOTHING)
    price = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True,default=1)



