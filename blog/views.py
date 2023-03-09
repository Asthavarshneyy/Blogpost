from django.views import generic
from .models import Post, Comment, Preference
from user.models import Profile
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404,reverse
from .forms import PostForm
from django.contrib import messages
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required

@login_required(login_url = "user:login")
def posts(request):
    keyword = request.GET.get("keyword")
    if keyword:
        posts = Post.objects.filter(title__icontains=keyword, status=1)
        return render(request,"posts.html",{"posts":posts})
    posts = Post.objects.filter(status=1)

    return render(request,"posts.html",{"posts":posts})



@login_required(login_url = "user:login")
def postpreference(request, slug, userpreference):
        
        if request.method == "POST":
                post= get_object_or_404(Post, slug=slug)

                obj=''

                valueobj=''

                try:
                        obj= Preference.objects.get(user= request.user, post= post)

                        valueobj= obj.value #value of userpreference


                        valueobj= int(valueobj)

                        userpreference= int(userpreference)
                
                        if valueobj != userpreference:
                                obj.delete()


                                upref= Preference()
                                upref.user= request.user

                                upref.post= post

                                upref.value= userpreference


                                if userpreference == 1 and valueobj != 1:
                                        post.likes += 1
                                        post.dislikes -=1
                                elif userpreference == 2 and valueobj != 2:
                                        post.dislikes += 1
                                        post.likes -= 1
                                

                                upref.save()

                                post.save()
                                return redirect(reverse("post:post_detail",kwargs={"slug":slug}))

                        elif valueobj == userpreference:
                                obj.delete()
                        
                                if userpreference == 1:
                                        post.likes -= 1
                                elif userpreference == 2:
                                        post.dislikes -= 1

                                post.save()
                                return redirect(reverse("post:post_detail",kwargs={"slug":slug}))
                
                except Preference.DoesNotExist:
                        upref= Preference()

                        upref.user= request.user

                        upref.post= post

                        upref.value= userpreference

                        userpreference= int(userpreference)

                        if userpreference == 1:
                                post.likes += 1
                        elif userpreference == 2:
                                post.dislikes +=1

                        upref.save()

                        post.save()                            
                        return redirect(reverse("post:post_detail",kwargs={"slug":slug}))


        else:
                post= get_object_or_404(Post, slug=slug)
                return redirect(reverse("post:post_detail",kwargs={"slug":slug}))
        

        
@login_required(login_url = "user:login")
def dashboard(request):
    posts = Post.objects.filter(author = request.user)
    context = {
        "posts":posts
    }
    return render(request,"dashboard.html",context)

@login_required(login_url = "user:login")
def addPost(request):
    form = PostForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.slug = slugify(post.title)
        post.author = request.user
        post.save()

        messages.success(request,"Post added successfully")
        return redirect("post:dashboard")
    return render(request,"addpost.html",{"form":form})

def post_detail(request,slug):  
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    return render(request,"post_detail.html",{"post":post,"comments":comments })

@login_required(login_url = "user:login")
def updatePost(request, slug):

    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None,request.FILES or None,instance = post)
    if form.is_valid():
        post = form.save(commit=False)
        
        post.author = request.user
        post.save()

        messages.success(request,"Post updated successfully")
        return redirect("post:dashboard")


    return render(request,"update.html",{"form":form})

@login_required(login_url = "user:login")
def deletePost(request,slug):
    post = get_object_or_404(Post,slug=slug)

    post.delete()

    messages.success(request,"Post deleted successfully")

    return redirect("post:dashboard")

@login_required(login_url = "user:login")
def addComment(request,slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = request.user, comment_content = comment_content)

        newComment.post = post

        newComment.save()
        messages.success(request, "Comment added successfully")

    return redirect(reverse("post:post_detail",kwargs={"slug":slug}))

# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'
