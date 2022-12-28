from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from user.forms import adressForm, adressUpdateForm, updateAdressIsDefault, CreditCardCreateForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout
from .forms import UpdateUser
from .models import Person, Adress, Person_adresses, Shopping_basket_items, Shopping_basket, Credit_card
from product.models import Item
from django.contrib.auth.decorators import login_required
from shop_order.models import *

# Create your views here.


def register_request(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        print("post methdo")
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print("form kaaydedildi")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(
                    request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
    else:

        form = AuthenticationForm()

    return render(request=request, template_name="registration/login.html", context={"login_form": form})


@login_required
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")


@login_required
def user_profile(request):

    form = UpdateUser(instance=request.user)
    if request.method == "POST":
        form = UpdateUser(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, "Kullanıcı başarıyla güncellendi ")
            return redirect("home")
    return render(request=request, template_name="registration/profile.html", context={"form": form})


@login_required
def reset_password(request):
    form = SetPasswordForm(request.user, request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "şifre başarıyla güncellendi")
    else:
        messages.error(request, "şifre güncellenemedi")

    return render(request, template_name="registration/reset-password.html", context={"form": form})


@login_required
def delete_user(request):
    request.user.delete()


# @login_required
def add_adress(request):
    if request.method == 'POST':
        form = adressForm(request.POST)
        if form.is_valid():
            created_adress = form.save()
            Person.objects.filter(user__id=request.user.id).first(
            ).user_adress.add(created_adress)
            messages.success(request, "adress başarıyla Eklendi")
            return redirect("home")
        else:
            messages.error(request, "adress eklenemedi")
    else:
        form = adressForm()
    context = {
        "form": form,
        "adresses": Person.objects.filter(
            user__id=request.user.id).first(),
    }

    return render(request, template_name="registration/adresses.html", context=context)


def update_adress(request, id):
    if request.method == 'POST':
        form = adressUpdateForm(
            request.POST, instance=Adress.objects.get(pk=id))
        is_default_form = updateAdressIsDefault(request.POST,
                                                instance=Person_adresses.objects.get(adress__id=id))

        if is_default_form.is_valid() and form.is_valid():
            form.save()
            is_default_form.save()

            messages.success(request, "adress başarıyla güncellendi")
            return redirect("home")
        # else:
        #     messages.error(request, "adress güncellenemedi")
    else:
        form = adressUpdateForm(instance=Adress.objects.get(pk=id))
        is_default_form = updateAdressIsDefault(
            instance=Person_adresses.objects.get(adress__id=id))
    context = {
        "form": form,
        "is_default_form": is_default_form,
        "adresses": Person.objects.filter(
            user__id=request.user.id).first(),
    }

    return render(request, template_name="registration/update_adress.html", context=context)


def delete_adress(request, id):
    obj = get_object_or_404(Adress, pk=id)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Adress başarıyla silindi!!")
        return redirect("user-adresses")
    else:
        messages.error(request, "Adress silemedi")

        return redirect("home")


def user_favorite(request):
    person = Person.objects.get(user__id=request.user.id)
    items_in_basket = Shopping_basket_items.objects.filter(
        Shopping_basket__user__user=request.user)
    context = {
        "person": person,
        "items_in_basket": items_in_basket
    }
    return render(request, template_name="registration/favorites.html", context=context)


def remove_favorite(request, id):
    if request.method == "POST":
        deleted_favorite = Person.objects.get(
            user__id=request.user.id).user_favorites.get(id=id)
        Person.objects.get(
            user__id=request.user.id).user_favorites.remove(deleted_favorite)

        messages.success(request, "başarıyla silindi!")
        return redirect("user_favorites")
    else:
        messages.success(request, "başarıyla silindi!")
        return redirect("user_favorites")


def add_favorite(request, id):
    if request.method == "POST":
        added_product = Item.objects.get(id=id)
        Person.objects.get(
            user__id=request.user.id).user_favorites.add(added_product)
        messages.success(request, "başaıryla favorilere eklendi")
        return redirect("home")
    else:
        messages.success(request, "favorilere eklenemedi")


def user_basket(request):
    if request.method == "POST":
        basket_value = request.POST["basket_value"]
        item_sku = request.POST["item_sku"]
        if basket_value and item_sku:
            updated_item = Shopping_basket_items.objects.filter(
                Shopping_basket__user__user__id=request.user.id, item__sku=item_sku)
            updated_item.update(quantity=basket_value)
            messages.success(
                request, f"{updated_item.first().item.product.name} başarıyla gübcellendi")

            return redirect("user_basket")
        else:
            return redirect("user_basket")

    person_basket_items = Shopping_basket_items.objects.filter(
        Shopping_basket__user__user__id=request.user.id)

    total_price = 0
    for item in person_basket_items:
        total_price += item.item.price * item.quantity

    context = {
        "person_basket_items": person_basket_items,
        "total_price": total_price

    }
    return render(request, template_name="registration/basket.html", context=context)


def delete_basket_item(request, id):
    if request.method == "POST":
        deleted_item = Item.objects.get(id=id)
        print("deneme")
        basket = Shopping_basket.objects.get(user__user=request.user)
        basket_items = basket.items.remove(deleted_item)
        messages.success(request, "başarıyla silindi")
        return redirect("user_basket")

    else:
        messages.error(request, "silinemedi")
        return redirect("user_basket")


def add_basket_item(request, id):

    if request.method == "POST":
        added_item = Item.objects.get(id=id)
        person_basket = Shopping_basket.objects.get(
            user__user__id=request.user.id)
        Shopping_basket_items.objects.create(
            Shopping_basket=person_basket, item=added_item, quantity=1)
        messages.success(request, "başarıyla eklendi")
        return redirect("user_basket")
    else:
        messages.error(request, "silinemedi")
        return redirect("home")


def user_credit_cards(request):
    if request.method == "POST":
        form = CreditCardCreateForm(request.POST)
        if form.is_valid():
            deneme = form.save(commit=False)
            deneme.person = Person.objects.get(user=request.user)
            form.save()
            messages.success(request, "card is saved successfully")
            return redirect("user_credit_cards")
        else:
            messages.error(request, "card can't be saved!!")
            return redirect("user_credit_cards")

    else:
        form = CreditCardCreateForm()
    user_cards = Credit_card.objects.filter(person__user=request.user)
    context = {
        "credit_cards": user_cards,
        "CreditCardCreateForm": form

    }
    return render(request, template_name="registration/credit-card.html", context=context)


def delete_credit_card(request, id):
    if request.method == "POST":
        Credit_card.objects.get(id=id).delete()
        messages.success(request, "başarıyla silindi")
        return redirect("home")


def update_credit_card(request, id):
    updated_credit_card = Credit_card.objects.get(id=id)

    if request.method == "POST":
        form = CreditCardCreateForm(
            data=request.POST, instance=updated_credit_card)
        if form.is_valid():
            form.save()
            messages.success(request, "başarıyla güncelledi")
            return redirect("user_credit_cards")

        else:
            messages.error(request, "bilgiler yanlış")

    else:
        form = CreditCardCreateForm(instance=updated_credit_card)

    context = {
        "CreditCardCreateForm": form

    }

    return render(request, template_name="registration/update-credit-card.html", context=context)


def buy_basket(request):
    if request.method == "POST":
        person = Person.objects.get(user=request.user)
        order_total_price = float(request.POST["order-total"])
        credit_card_id = int(request.POST["credit_card_id"])
        order_adress_id = int(request.POST["adress_id"])
        order_adress = Adress.objects.get(id=order_adress_id)
        credit_card_ = Credit_card.objects.get(id=credit_card_id)
        person_basket_items = Shopping_basket_items.objects.filter(
            Shopping_basket__user=person)

        # order'ı oluşturdum
        shop_order = ShopOrder.objects.create(
            user=person, address=order_adress, order_total=order_total_price)
        # basketi temizle
        for basket_item in person_basket_items:
            ShopOrderItems.objects.create(
                shop_order=shop_order, product_item=basket_item.item, price=basket_item.item.price, quantity=basket_item.quantity)
            basket_item.delete()
        messages.success(request, "şiparış başarıyla oluşturuldu.")
        return redirect("home")

    person = Person.objects.get(user=request.user)
    person_default_adress = Person_adresses.objects.filter(
        person=person, is_default=True)

    person_default_credit_card = Credit_card.objects.filter(
        person=person, is_default=True)

    person_basket_items = Shopping_basket_items.objects.filter(
        Shopping_basket__user=person)

    total_price = 0
    for item in person_basket_items:
        total_price += item.item.price * item.quantity

    context = {
        'person': person,
        "person_default_adress": person_default_adress,
        "person_default_credit_card": person_default_credit_card,
        "person_basket_items": person_basket_items,
        "total_price": total_price

    }

    return render(request, template_name="registration/buy-product.html", context=context)


