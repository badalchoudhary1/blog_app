from django.contrib import admin
# Register your models here.
from .models import Blog, BlogDetail

admin.site.register(Blog)
admin.site.register(BlogDetail)
