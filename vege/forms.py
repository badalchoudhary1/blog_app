from django import forms
from django.contrib.auth.models import User
from .models import UserProfile,Post

# Form for creating a new user
class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

# Form for creating or updating a user profile
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']  # Add fields you want for the profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']