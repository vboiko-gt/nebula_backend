from django.db import models


class LoggedAction(models.Model):

    action = models.CharField(max_length=255, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    affected = models.CharField(max_length=2048)
    automatic = models.BooleanField()
    note = models.CharField(max_length=1024)

