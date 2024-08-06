from django.db import models
from production.models import Production

class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Location(models.Model):
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.address

class Activity(models.Model):
    production = models.ForeignKey(Production, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title

class Report(models.Model):
    REPORT_TYPE_CHOICES = [
        ('challenge', 'Challenge'),
        ('recommendation', 'Recommendation'),
        ('others', 'Others'),
    ]
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    comment = models.TextField()
    type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)
    
    def __str__(self):
        return f"Report on {self.activity}"

