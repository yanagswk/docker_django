# Generated by Django 2.2.2 on 2020-04-05 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reply',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
