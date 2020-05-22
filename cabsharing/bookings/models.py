from django.db import models
from django.contrib.auth.models import User
from django.utils import  timezone
from django.shortcuts import redirect


GENDER = [
    ('all', 'all'),
    ('girls only', 'girls only'),
    ('boys only', 'boys only')
]


class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users', null=True)
    creator = models.CharField(max_length=30, blank=False)
    time = models.TimeField(blank=False, auto_now=False, auto_now_add=False, default='00:00 AM')
    date = models.DateField(blank=False, auto_now=False, auto_now_add=False, default='2019-6-14')
    start_position = models.CharField(max_length=30, blank=False)
    destination = models.CharField(max_length=30, blank=False)
    max_members = models.PositiveIntegerField(default=4, blank=False, help_text='maximum number of members includes you as well.')
    gender = models.CharField(default='both', max_length=20, choices=GENDER)
    description = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return self.creator + '-' + self.destination + '-' + self.time + '-' + self.date


    def get_absolute_url(self):
        return redirect('index')
