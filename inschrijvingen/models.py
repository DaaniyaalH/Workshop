from django.db import models
from django.contrib.auth.models import User

class Workshop(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Inschrijving(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # User is nu optioneel
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    naam = models.CharField(max_length=100)  # Naam van de gebruiker
    email = models.EmailField()  # Email van de gebruiker
    datum = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'workshop'], name='unique_inschrijving')
        ]

    def __str__(self):
        return f"{self.naam} - {self.workshop.title}"
