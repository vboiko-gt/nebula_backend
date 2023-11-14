from django.contrib import admin
from .models import LoggedAction



@admin.register(LoggedAction)
class LoggedActionAdmin(admin.ModelAdmin):
    
    list_display = ('action', 'affected', 'date', 'note', 'automatic')
