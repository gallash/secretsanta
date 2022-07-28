# Generated by Django 3.2.9 on 2022-07-24 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('santapp', '0010_auto_20220724_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.TextField(default=None)),
                ('is_remote', models.BooleanField(default=False)),
                ('place', models.CharField(default=None, max_length=2042)),
                ('rules', models.TextField(default=None)),
                ('price_range', models.FloatField(default=0.0)),
                ('organizer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_organizer', models.BooleanField(default=False)),
                ('first_name', models.CharField(default=None, max_length=32)),
                ('last_name', models.CharField(default=None, max_length=32)),
                ('nickname', models.CharField(default=None, max_length=32)),
                ('email', models.EmailField(default=None, max_length=255)),
                ('wishlist', models.CharField(default=None, max_length=2042)),
                ('blacklist', models.CharField(default=None, max_length=2042)),
                ('description_of_yourself', models.TextField(default=None, max_length=2042)),
                ('address', models.CharField(default=None, max_length=2042)),
                ('has_bought', models.BooleanField(default=False)),
                ('event', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='santapp.event')),
            ],
            options={
                'ordering': ['first_name', 'last_name', 'nickname', 'email'],
            },
        ),
    ]
