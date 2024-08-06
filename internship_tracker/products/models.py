from django.db import models

class Product(models.Model):
    CLASS_CHOICES = [
        ('crop', 'Crop'),
        ('livestock', 'Livestock'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    class_type = models.CharField(max_length=10, choices=CLASS_CHOICES)
    
    def __str__(self):
        return self.name

