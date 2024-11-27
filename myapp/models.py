from django.db import models

class WangUser(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=128)  # To store hashed passwords
    email = models.EmailField(unique=True)  # For email validation

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)  # Product category
    color = models.CharField(max_length=50)  # Product color

    def __str__(self):
        return self.name


class FileUpload(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="files/")  # For general files
    image = models.ImageField(upload_to="images/")  # Optional image uploads
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
