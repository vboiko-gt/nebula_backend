from django.db import models


class Raider(models.Model):

    name = models.CharField(max_length=255, unique=True)
    score = models.FloatField(default=0)
    discord_nickname = models.CharField(max_length=255, unique=True, null=False, blank=False)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.score = round(self.score, 1)
        return super().save(force_insert, force_update, using, update_fields)


class Character(models.Model):

    name = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey('Raider', on_delete=models.CASCADE)
    main = models.BooleanField(default=False)

    def __str__(self):
        return self.name

