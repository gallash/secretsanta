# Generated by Django 3.2.9 on 2022-07-26 01:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('santapp', '0014_auto_20220724_2105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='participant',
            options={},
        ),
        migrations.AddField(
            model_name='event',
            name='online_meeting_link',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='gives_to',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='password',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='receives_from',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='user',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='participant',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='blacklist',
            field=models.CharField(blank=True, default=None, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='description_of_yourself',
            field=models.TextField(blank=True, default=None, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='has_bought',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='nickname',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='wishlist',
            field=models.CharField(blank=True, default=None, max_length=2048, null=True),
        ),
    ]
