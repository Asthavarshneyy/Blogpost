from .models import Post, Author
from django.views import generic
from django.shortcuts import render
# Create your views here.

def HomeView(request, *args, **kwargs):
    featured=Post.objects.filter(featured=True, status=1)
    latest=Post.objects.filter(status=1).order_by('-created_on')
    context={
        'object_list': featured,
        'latest': latest,
    }
    return render(request, 'home_view.html', context)

class PostDetail(generic.DetailView):
    model=Post
    template_name='post_detail.html'

class PostList(generic.ListView):
    queryset=Post.objects.filter(status=1).order_by('-created_on')
    template_name='index.html'

def AboutView(request):
    return render(request, 'about_view.html')


