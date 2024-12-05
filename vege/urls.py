from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('add-profile/', views.add_profile, name='add_profile'),  # Form to create user and profile
    path('profiles/', views.user_profiles, name='user_profiles'), 
    path('blogs/', views.all_user_blogs, name='all_user_blogs'), 
    path('profile/', views.user_profile_detail, name='user_profile_detail'),  # User profile with posts
    path('create-post/', views.create_post, name='create_post'), 

]