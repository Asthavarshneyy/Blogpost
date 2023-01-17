from blog.serializers import UserSerializer, PostSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, action
from blog.models import Post
from rest_framework import permissions, renderers
from blog.permissions import IsOwnerOrReadOnly
# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format)
    })

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    The list of current users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    List of all the posts
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)