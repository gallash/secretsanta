# Generated by Django 3.2.9 on 2022-07-24 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('santapp', '0009_event_event_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='event',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Participant',
        ),
    ]
