from django.db import models
from django.contrib.auth.models import User

STATUS=(
  (0, "Draft"),
  (1, "Publish")
)

# Create your models here.
class Post(models.Model):
  title=models.CharField(max_length=100, blank=False, unique=True, default='Title')
  description=models.TextField(max_length=200, blank=True, default='')
  blog=models.TextField(blank=False, default='Start Here')
  author=models.ForeignKey(User, on_delete=models.CASCADE)
  created_on=models.DateTimeField(auto_now_add=True)
  updated_on=models.DateTimeField(auto_now=True)
  status=models.IntegerField(choices=STATUS, default=0)
  featured=models.BooleanField()
  class Meta:
    ordering=['-created_on']
  def _str_(self):
    return self.title

class Author(models.Model):
  user=models.OneToOneField(User, on_delete=models.CASCADE)
  profile_picture=models.ImageField(blank=True)
  def _str_(self):
    return self.user.username