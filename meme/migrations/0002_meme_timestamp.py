# Generated by Django 4.0.2 on 2022-03-15 14:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meme',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]