from django.contrib import admin
from django.urls import path
from .views import register, loginUser, logoutUser

app_name = "user"

urlpatterns = [
    path('register/',register,name = "register"),
    path('login/',loginUser,name = "login"),
    path('logout/',logoutUser,name = "logout"),

]