from django.db import models

# Create your models here.
# Reference Model
class Airport(models.Model):
    code = models.CharField(max_length=5)
    city = models.CharField(max_length=72)
    
    def __str__(self):
        return f"{self.city} ({self.code})"


# Related Model
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        """string for representing the flight information within a query set"""
        return f"Flight HHF{self.id} : {self.origin} To {self.destination}, {self.duration} minutes"