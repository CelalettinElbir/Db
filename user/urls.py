from django.urls import path
from django.conf.urls.static import static
from .views import register_request, user_login, logout_request,user_favorite,user_basket,remove_favorite,add_favorite, user_profile, reset_password, delete_user, add_adress, update_adress,delete_adress


urlpatterns = [
    path("register/", register_request, name="register"),
    path("login/", user_login, name="login"),
    path("logout", logout_request, name="logout"),
    path("profile", user_profile, name="user_profile"),
    path("reset-password", reset_password, name="password-reset"),
    path("delete-user", delete_user, name="delete-user"),
    path("adresses", add_adress, name="user-adresses"),
    path("update-adress/<int:id>", update_adress, name="update_adress"),
    path("delete_adress/<int:id>",delete_adress,name = "delete_adress"),
    path("favorites",user_favorite,name = "user_favorites"),
    path("favorite/<int:id>/delete",remove_favorite,name = "remove_favorite"),
    path("favorite/add/<int:id>",add_favorite,name = "add_favorite"),
    path("basket",user_basket,name= "user_basket")

]
