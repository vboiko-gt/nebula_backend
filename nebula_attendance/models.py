import datetime
import requests
from django.db import models
from nebula_backend.models import Raider


class Event(models.Model):

    raid_helper_json = models.TextField()
    mrt_roster_export = models.TextField(blank=True)
    title = models.CharField(max_length=255, blank=True)
    date = models.DateField(null=True, blank=True, default=None)
    points_applied = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def save(self) -> None:
        if self.raid_helper_json and not self.pk:
            json_data = requests.get(self.raid_helper_json).json()
            self.date = datetime.date(*list(map(int, json_data['date'].split('-')[::-1])))
            self.title = json_data.get('title', 'null')
        return super().save()

    def __str__(self) -> str:
        return f'{self.title} ({self.date.day}.{self.date.month}.{self.date.year})'


class Attendee(models.Model):

    INTIME_CHOICES = (
        ('A', 'INTIME'),
        ('B', 'SLIGHT DELAY'),
        ('C', 'LONG DELAY'),
    )

    raider = models.ForeignKey(Raider, on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    intime = models.CharField(max_length=1, choices=INTIME_CHOICES)


class Warning(models.Model):

    text = models.CharField(max_length=1024)
    resolved = models.BooleanField(default=False)
