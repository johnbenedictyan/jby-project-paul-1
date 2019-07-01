from django.db import models

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
    photo = models.FileField(
        upload_to='uploads/',
        blank=False
    )
    agree_to_clauses = models.BooleanField(
        blank=False
    )
    followed_up = models.BooleanField(
        blank=True,
        default=False
    )
    def __str__(self):  
        return self.name