# Generated by Django 4.2.6 on 2023-10-26 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nebula_backend', '0006_remove_character_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='nebula_backend.raider'),
            preserve_default=False,
        ),
    ]
