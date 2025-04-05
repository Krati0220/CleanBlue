from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 1. CleanupEvent: Each event created by the NGO
class CleanupEvent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.title

# 2. Participation: Links users to events they joined
class Participation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(CleanupEvent, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} joined {self.event.title}"

# 3. YearlyImpact: Tracks total waste collected per year
class YearlyImpact(models.Model):
    year = models.IntegerField()
    waste_collected_kg = models.FloatField()

    def __str__(self):
        return f"{self.year} - {self.waste_collected_kg} kg"
