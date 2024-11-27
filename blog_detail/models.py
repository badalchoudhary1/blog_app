from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    def __str__(self):
        return self.title

class BlogDetail(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE, related_name='detail')
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    tags = models.CharField(max_length=100)

    def __str__(self):
        return f"Details for {self.blog.title}"
