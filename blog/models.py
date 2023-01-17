from django.db import models

STATUS=(
  (0, "Draft"),
  (1, "Publish")
)

# Create your models here.
class Post(models.Model):
  title=models.CharField(max_length=100, blank=False, unique=True, default='Title')
  description=models.TextField(max_length=200, blank=True, default='')
  blog=models.TextField(blank=False, default='Start Here')
  owner=models.ForeignKey('auth.User', on_delete=models.CASCADE)
  created_on=models.DateTimeField(auto_now_add=True)
  updated_on=models.DateTimeField(auto_now=True)
  status=models.IntegerField(choices=STATUS, default=0)
  class Meta:
    ordering=['-created_on']
  def _str_(self):
    return self.title