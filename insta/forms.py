from django import forms
from  .models import Profile,Comments,Image
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from urllib import request
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image','image_name','image_caption']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image','name','bio','email']
        
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']