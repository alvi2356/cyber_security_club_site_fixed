# Generated by Django 4.2.21 on 2025-05-28 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_eventimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('seminar', 'Seminar'), ('workshop', 'Workshop'), ('ctf', 'CTF'), ('contest', 'Contest')], default='seminar', max_length=20),
        ),
    ]
