from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
  class Meta:
    model=Author
    fields=('bio', 'instagram', 'linkedin')
  

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'blog', 'status', 'featured')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            'blog': forms.Textarea(),
            'description':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Description of the Blog'}),
            'status':forms.IntegerField(),
            'featured':forms.BooleanField(),
        }