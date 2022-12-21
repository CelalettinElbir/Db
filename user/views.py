from django.shortcuts import render, redirect
from django.contrib import messages
from user.forms import adressForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout
from .forms import UpdateUser
# from .models import Person, Adress
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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
        print("get")

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
            form.save()
            
            # print(Person.objects.get(user= request.user.id).user_adress.add(form))
            messages.success(request, "adress başarıyla Eklendi")
        else:
            messages.error(request, "adress eklenemedi")
    else:
        form = adressForm()
        # deneme = deneme = Person.objects.filter(user__id  = request.user.id).first().user_adress.add(form.auto_id)
    context = {
        "form": form,
        # "adresses": Person.objects.filter(
        #     user__id=request.user.id).first(),
            }

    return render(request, template_name="registration/adresses.html", context=context)
