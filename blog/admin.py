from django.contrib import admin
from .models import Post, Comment,Preference

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_author', 'post', 'comment_date')
    list_filter = ("comment_date",)
    search_fields = ['post', 'comment_author']

class PreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'value', 'date')
    list_filter = ("date",)
    search_fields = ['post', 'user']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Preference, PreferenceAdmin)