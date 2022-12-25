from django.contrib import admin
from .models import Person, Adress, Person_adresses, Credit_card,Shopping_basket,Shopping_basket_items


admin.site.register(Person)
admin.site.register(Adress)
admin.site.register(Credit_card)
admin.site.register(Shopping_basket)
admin.site.register(Shopping_basket_items)


class Person_adresses_admin(admin.ModelAdmin):
    list_display = ["person", "adress","is_default"]
    list_filter  =["person","is_default"]


admin.site.register(Person_adresses,Person_adresses_admin)
