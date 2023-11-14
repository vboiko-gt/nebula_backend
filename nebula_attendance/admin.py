from django.contrib import admin
from .models import Event, Attendee, Warning


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'date', 'points_applied')


@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):

    list_display = ('event', 'raider', 'intime')


@admin.register(Warning)
class WarningAdmin(admin.ModelAdmin):

    list_display = ('text', 'resolved')
