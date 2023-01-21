from blog.views import PostDetail, PostList
from django.urls import path

urlpatterns=[
  path('<int:id>/', PostDetail.as_view(), name='post-detail'),
  path('', PostList.as_view(), name='post-list')
]