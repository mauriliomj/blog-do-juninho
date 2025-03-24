from django import forms
from src.infrastructure.models import UserModel
from .models import PostModel
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email']

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ["title", "content"]
