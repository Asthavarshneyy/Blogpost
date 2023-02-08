from django.contrib import admin
from django.urls import path
from .views import RegisterView, loginUser, logoutUser, index, ActivateAccount

app_name = "user"

urlpatterns = [
    path('register/',RegisterView.as_view(),name = "register"),
    path('login/',loginUser,name = "login"),
    path('logout/',logoutUser,name = "logout"),
     path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
]