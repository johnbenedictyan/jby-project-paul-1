from django.db import models
from datetime import date
from pyuploadcare.dj.models import ImageField

# Create your models here.
class fault(models.Model):
    name = models.CharField(
        blank=False,
        max_length = 255
    )
    email = models.EmailField(
        blank=False
    )
    phone_number = models.IntegerField(
        blank=False
    )
    contacted_on_updates = models.BooleanField(
        blank=True
    )
    description = models.TextField(
        blank=False
    )
    photo = ImageField(
        blank=False
    )
    agree_to_clauses = models.BooleanField(
        blank=False
    )
    followed_up = models.BooleanField(
        blank=True,
        default=False
    )
    date_of_creation = models.DateField(
        blank=True,
        default=date.today
    )
    def __str__(self):  
        return self.name