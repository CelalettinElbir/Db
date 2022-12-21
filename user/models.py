from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    comment_point = models.BigIntegerField(
        "point", null=True, blank=True, default=0)
    user_Adresses = models.ManyToManyField("Adress",through='Person_adresses',through_fields=('person', 'adress'),)
    def __str__(self) -> str:
        return self.user.username


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
    is_default = models.BooleanField(default=0)
