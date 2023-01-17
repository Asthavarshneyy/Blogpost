from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet,basename="user")

urlpatterns=[
  path('', include(router.urls)),
]