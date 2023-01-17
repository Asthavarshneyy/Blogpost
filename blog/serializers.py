from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
  owner=serializers.ReadOnlyField(source='owner.username')
  class Meta:
    model=Post
    fields=['url', 'id', 'title', 'description', 'owner', 'created_on', 'updated_on']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username']