from django.contrib import admin
from .models import Person,Adress,Person_adresses


admin.site.register(Person)
admin.site.register(Adress)
admin.site.register(Person_adresses)