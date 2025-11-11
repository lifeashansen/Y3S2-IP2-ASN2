from django.db import models

# Create your models here.
class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
