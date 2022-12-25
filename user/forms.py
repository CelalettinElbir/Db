from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Adress, Person, Person_adresses, Shopping_basket_items, Credit_card


class UpdateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class updateUserPassword(forms.Form):
    password = forms.PasswordInput()
    password2 = forms.PasswordInput()


class adressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = ("id", "name", "city", "district",
                  "neighborhood", "adress_line")


class adressUpdateForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = ("id", "name", "city", "district",
                  "neighborhood", "adress_line")


class updateAdressIsDefault(forms.ModelForm):
    class Meta:
        model = Person_adresses
        fields = ("is_default",)


class CreditCardCreateForm(forms.ModelForm):
    class Meta:
        model = Credit_card
        fields = ("name", "provider", "card_number",
                  "expiration_date", "security_code", "is_default",)

        exclude = ["person"]
