from django.db import models

# Create your models here.
from django.conf import settings

class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    event_id = models.CharField(
        max_length=255,
        unique=True
    )
    room_number = models.CharField(max_length=20)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.room_number}"
