# Generated by Django 3.2.9 on 2022-07-24 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('santapp', '0007_alter_event_event_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_name',
        ),
    ]
