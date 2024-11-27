from django.shortcuts import render

# Create your views here.
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_detail/blog_list.html', {'blogs': blogs})

def blog_detail_view(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blog_detail/blog_detail.html', {'blog': blog})

