from django.db import models
from planner.models import Instruction

class Production(models.Model):
    instruction = models.ForeignKey(Instruction, on_delete=models.CASCADE)
    description = models.TextField()
    deadline = models.DateField()
    submitted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.deadline = self.instruction.week.end_date
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Production related to {self.instruction}"

class Feedback(models.Model):
    SWOT_CHOICES = [
        ('strength', 'Strength'),
        ('weakness', 'Weakness'),
        ('opportunity', 'Opportunity'),
        ('threat', 'Threat'),
    ]
    production = models.ForeignKey(Production, on_delete=models.CASCADE)
    comment = models.TextField()
    swot = models.CharField(max_length=11, choices=SWOT_CHOICES)
    
    def __str__(self):
        return f"Feedback on {self.production}"

