from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes=models.IntegerField(default=0)
    dislikes=models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        return super(Post, self).save(*args, **kwargs)
    
VALUE= (
    (1,"Like"),
    (2,"Dislike")
)

class Preference(models.Model):
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    post= models.ForeignKey(Post, on_delete= models.CASCADE)
    value= models.IntegerField(choices=VALUE) #1: like 2: dislike
    date= models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return str(self.user) + ':' + str(self.post) +':' + str(self.value)

    class Meta:
       unique_together = ("user", "post", "value")     


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete = models.CASCADE,related_name="comments")
    comment_author = models.ForeignKey(User, on_delete= models.CASCADE)
    comment_content = models.CharField(max_length = 200)
    comment_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']
