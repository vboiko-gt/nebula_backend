from django.contrib import admin
from django.db import transaction

from manage import main
from .models import Raider, Character
from nebula_logging.models import LoggedAction
from django.contrib import messages
from django.utils.translation import ngettext


class CharacterInline(admin.TabularInline):
    model = Character


@admin.register(Raider)
class RaiderAdmin(admin.ModelAdmin):
   
    list_display = ('name', 'score', 'note')
    actions = ('apply_decay', 'add_3_points', 'add_2_points', 'add_1_point', 'subtract_1_point', 'subtract_2_points', 'subtract_3_points')
    inlines = (
        CharacterInline,
    )

    @admin.action(description='Apply Decay')
    def apply_decay(self, request, queryset):
        with transaction.atomic():
            if queryset.count() != Raider.objects.all().count():
                self.message_user(
                        request,
                        ngettext(
                            'Decay can only be applied to all raiders',
                            'Decay can only be applied to all raiders',
                            0
                        ),
                        messages.ERROR
                )
                return

            affected_raiders = []

            for raider in queryset:
                if raider.score > 0:
                    raider.score = raider.score / 2
                    if raider.score < 1:
                        raider.score = 1
                    raider.save()
                    affected_raiders.append(raider.name)

            LoggedAction.objects.create(
               action='Decay',
               affected=', '.join(affected_raiders),
               note=f'Applied by {request.user.username}',
               automatic=False
            )

            self.message_user(
                request,
                ngettext(
                    f'Decay has been applied to following raiders: {", ".join(affected_raiders)}',
                    f'Decay has been applied to following raiders: {", ".join(affected_raiders)}',
                    queryset.count()
                ),
                messages.SUCCESS,
            )

    @admin.action(description='+3 points')
    def add_3_points(self, request, queryset):
        self._apply_points_change(
            request, queryset, 3, 
            'Following raider was awarded with 3 points: ', 
            'Following raiders were awarded with 3 points: '
        )
    
    @admin.action(description='+2 points')
    def add_2_points(self, request, queryset):
         self._apply_points_change(
            request, queryset, 2, 
            'Following raider was awarded with 2 points: ', 
            'Following raiders were awarded with 2 points: '
        )

    @admin.action(description='+1 point')
    def add_1_point(self, request, queryset):
        self._apply_points_change(
            request, queryset, 1, 
            'Following raider was awarded with 1 point: ', 
            'Following raiders were awarded with 1 point: '
        )

    @admin.action(description='-1 point')
    def subtract_1_point(self, request, queryset):
         self._apply_points_change(
            request, queryset, -1, 
            '1 point was removed from following raider: ', 
            '1 point was removed from following raiders: '
        )

    @admin.action(description='-2 points')
    def subtract_2_points(self, request, queryset):
        self._apply_points_change(
            request, queryset, -2, 
            '2 points were removed from following raider: ', 
            '2 point were removed from following raiders: '
        )

    @admin.action(description='-3 points')
    def subtract_3_points(self, request, queryset):
        self._apply_points_change(
            request, queryset, -3, 
            '3 points were removed from following raider: ', 
            '3 points were removed from following raiders: '
        )

    def _apply_points_change(self, request, queryset, points, msg_s, msg_p):
        with transaction.atomic():
            affected_raiders = []
            for raider in queryset:
                raider.score += points
                raider.save()
                affected_raiders.append(raider.name)

            msg_r = ', '.join(affected_raiders)

            LoggedAction.objects.create(
                action=f'{f"+{points}" if points >= 0 else f"{points}"} points',
                affected=msg_r,
                note=f'Applied by {request.user.username}',
                automatic=False
            )

            self.message_user(
                request, 
                ngettext(
                    msg_s + msg_r,
                    msg_p + msg_r,
                    queryset.count()
                ), 
                messages.SUCCESS
            )


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
   
    list_display = ('name', 'owner')

