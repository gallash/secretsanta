# Generated by Django 3.2.9 on 2022-07-24 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('santapp', '0011_event_participant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
    ]
