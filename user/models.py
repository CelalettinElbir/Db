from django.db import models
from django.contrib.auth.models import User
from product.models import Item
from django.core.exceptions import ValidationError
# Create your models here.


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    comment_point = models.BigIntegerField(
        "point", null=True, blank=True, default=0)
    user_adress = models.ManyToManyField(
        "Adress", through='Person_adresses', through_fields=('person', 'adress'),)
    user_favorites = models.ManyToManyField(Item)
    
    def __str__(self) -> str:
        return self.user.username
    # user_favorites = models.ManyToManyField("Item")


class Adress(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    district = models.CharField(max_length=45)
    neighborhood = models.CharField(max_length=45, blank=True, null=True)
    adress_line = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Person_adresses(models.Model):
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    adress = models.ForeignKey("Adress", on_delete=models.CASCADE)
    is_default = models.BooleanField(default=False)

    def clean(self):
        # # Get all the instances of MyModel that have is_default set to True
        default_instances = Person_adresses.objects.filter(
            is_default=True, person=self.person)
        # default_instances = Person_adresses.objects.filter(is_default=True)
        # # If there are any other instances with is_default set to True, and this instance
        # # is being set to True as well, raise a validation error
        if default_instances.exclude(pk=self.pk).exists() and self.is_default:
            raise ValidationError("sadece bir tane varsayılan ayarlanabilir.")


class Credit_card(models.Model):
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=45)
    provider = models.CharField(max_length=20)
    card_number = models.CharField(max_length=16)
    expiration_date = models.DateField()
    security_code = models.CharField(max_length=3)
    is_default = models.BooleanField(blank=True)

    def clean(self):
        # # Get all the instances of MyModel that have is_default set to True
        default_instances = Credit_card.objects.filter(
            is_default=True, person=self.person)
        # # If there are any other instances with is_default set to True, and this instance
        # # is being set to True as well, raise a validation error
        if default_instances.exclude(pk=self.pk).exists() and self.is_default:
            raise ValidationError("sadece bir tane varsayılan ayarlanabilir.")



class Shopping_cart(models.Model):
    user = models.OneToOneField(Person, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item,through="Shopping_card_items",through_fields=('Shopping_cart', 'item'))
    def __str__(self) -> str:
        return self.user.user.username




class Shopping_card_items(models.Model):
    Shopping_cart = models.ForeignKey("Shopping_cart", on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    