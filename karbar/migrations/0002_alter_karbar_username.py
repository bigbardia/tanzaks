# Generated by Django 4.0.2 on 2022-03-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karbar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='karbar',
            name='username',
            field=models.CharField(max_length=48, unique=True),
        ),
    ]
