
from django.urls import path, include
from . import views as vw



urlpatterns = [
    path("list_create/", vw.list_create_user, name="register_user"),
    path("login/", vw.login_user, name="login"),
    path("edit_profile/<int:pk>", vw.update_profile, name="edit_profile")
]
