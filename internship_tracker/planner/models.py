from django.db import models
from django.contrib.auth.models import User, Group
from products.models import Product
from datetime import timedelta

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Week(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def save(self, *args, **kwargs):
        self.end_date = self.start_date + timedelta(days=7)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Unit(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title

class Instruction(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    intern = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    team = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"Instruction for {self.product.name} in {self.week.title}"

