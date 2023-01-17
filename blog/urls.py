from django.urls import path, include
from blog import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet,basename="user")
router.register(r'posts', views.PostViewSet, basename="post")

urlpatterns=[
  path('', include(router.urls)),
]