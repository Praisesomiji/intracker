from django.db import models

class Detail(models.Model):
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.date} at {self.time} - {self.venue}"

class Workshop(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField()
    detail = models.ManyToManyField(Detail, related_name="workshops")

    def __str__(self):
        return self.title
