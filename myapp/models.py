from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)  # Updated field
    color = models.CharField(max_length=50)  # New field for color
    

    def __str__(self):
        return self.name


