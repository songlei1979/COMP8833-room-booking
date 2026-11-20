from django.db import models

# Create your models here.
from django.conf import settings


from django.db import models


class Room(models.Model):
    room_number = models.CharField(
        max_length=20,
        unique=True
    )
    capacity = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    has_projector = models.BooleanField(default=False)

    def __str__(self):
        return self.room_number


class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    event_id = models.CharField(
        max_length=255,
        unique=True
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.room_number}"
