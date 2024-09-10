from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    ]
    number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo = models.ImageField(upload_to='room_photos/')

    def __str__(self):
        return self.room_type

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    users = models.ManyToManyField(User, related_name='bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f'бронь номера {self.room.number} с {self.check_in_date} по {self.check_out_date}'
