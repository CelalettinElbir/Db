from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from user.forms import adressForm, adressUpdateForm, updateAdressIsDefault
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout
from .forms import UpdateUser
from .models import Person, Adress, Person_adresses
from product.models import Item
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
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
                print("Girdi")

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
    context = {
        "person": person
    }
    return render(request, template_name="registration/favorites.html", context=context)


def remove_favorite(request, id):
    if request.method == "POST":
        deleted_favorite = Person.objects.get(
            user__id=request.user.id).user_favorites.get(id = id)
        Person.objects.get(
            user__id=request.user.id).user_favorites.remove(deleted_favorite)

        messages.success(request, "başarıyla silindi!")
        return redirect("user_favorites")
    else:
        messages.success(request, "başarıyla silindi!")
        return redirect("user_favorites")


def add_favorite(request,id):
    if request.method == "POST":
        added_product = Item.objects.get(id = id)
        Person.objects.get(user__id = request.user.id ).user_favorites.add(added_product) 
        messages.success(request,"başaıryla favorilere eklendi")
        return redirect("home")
    else:
        messages.success(request,"favorilere eklenemedi")




def user_basket(request):

    return render(request, template_name="registration/basket.html")
