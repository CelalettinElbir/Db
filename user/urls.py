from django.urls import path
from django.conf.urls.static import static
from .views import register_request, user_login, logout_request, user_profile, reset_password,delete_user

urlpatterns = [
    path("register/", register_request, name="register"),
    path("login/", user_login, name="login"),
    path("logout", logout_request, name="logout"),
    path("profile", user_profile, name="user_profile"),
    path("reset-password", reset_password, name="password-reset"),
    path("delete-user", delete_user, name="delete-user"),

]