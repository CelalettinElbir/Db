from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    comment_point = models.BigIntegerField("point")
    user_adress = models.ManyToManyField("Adress")
    #many to many ye defoult eklenecek.
    def __str__(self) -> str:
        return self.user.username


    

class Adress(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    district = models.CharField(max_length=45)
    neighborhood = models.CharField(max_length=45, blank=True, null=True)
    adress_line = models.CharField(max_length=45, blank=True, null=True)

