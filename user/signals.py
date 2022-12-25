from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Person,Shopping_basket


@receiver(post_save, sender=User)
def create_person(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_person(sender, instance, **kwargs):
    instance.person.save()





@receiver(post_save, sender=Person)
def create_basket(sender, instance, created, **kwargs):
    if created:
        Shopping_basket.objects.create(user=instance)


@receiver(post_save, sender=Person)
def save_basket(sender, instance, **kwargs):
    instance.shopping_basket.save()







# @receiver(post_save, sender=User)
# def create_basket(sender, instance, created, **kwargs):
#     if created:
#         Shopping_basket.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_basket(sender, instance, **kwargs):
#     instance.shopping_basket.save()
