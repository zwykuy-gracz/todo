# Generated by Django 5.1.4 on 2025-02-25 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter',
            name='number_of_visitations',
            field=models.IntegerField(default=0),
        ),
    ]
