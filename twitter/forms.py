from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import fields
from twitter.models import Post, Profile

class user_register_form(UserCreationForm):

    class Meta :
        model=User
        fields= ['first_name', 'username','password1', 'password2']

class post_form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control w-100',
    'id':'contentsBox','rows':'3', 'placeholder':'que estas pensando '}))

    class Meta:
        model=Post
        fields = ['content']


class user_edit(forms.ModelForm):
    class Meta :
        model=User
        fields=['first_name','username']

class profile_edit(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['img','bio']