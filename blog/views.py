from django.shortcuts import render
from rest_framework import generics
from blog.serializer import UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
    })

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    The list of current users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer