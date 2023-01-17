from django.contrib import admin
from blog.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
  list_display=('title', 'status', 'created_on', 'updated_on')
  list_filter=('status',)
  search_fields=['title']

admin.site.register(Post, PostAdmin)