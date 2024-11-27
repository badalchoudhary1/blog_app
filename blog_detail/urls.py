# blog_detail/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('blog/<int:blog_id>/', views.blog_detail_view, name='blog_detail'),
]
