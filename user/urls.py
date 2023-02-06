from django.contrib import admin
from django.urls import path
from .views import register, loginUser, logoutUser, index, activate

app_name = "user"

urlpatterns = [
    path('register/',register,name = "register"),
    path('login/',loginUser,name = "login"),
    path('logout/',logoutUser,name = "logout"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',  
        activate, name='activate'), 
    # path('activate/<uidb64>/<token>/',  activate, name='activate'), 

]