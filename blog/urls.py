
from django.urls import path, re_path
from . import views
app_name = "post"

urlpatterns = [
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('addpost/',views.addPost,name = "addpost"),
    path('post/<slug:slug>/',views.post_detail,name = "post_detail"),
    path('update/<slug:slug>',views.updatePost,name = "update"),
    path('delete/<slug:slug>',views.deletePost,name = "delete"),
    path('',views.posts,name = "posts"),
    path('comment/<slug:slug>',views.addComment,name = "comment"),
    path('post/<slug:slug>/preference/<int:userpreference>', views.postpreference, name='preference')
   ]

