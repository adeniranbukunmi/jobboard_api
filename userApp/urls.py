
from django.urls import path, include
from . import views as vw



urlpatterns = [
    path("list_create/", vw.creatListUser, name="list_create"),
    path("login/", vw.login, name="login"),
]
