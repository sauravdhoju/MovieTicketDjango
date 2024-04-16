# Generated by Django 5.0.4 on 2024-04-16 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_language_remove_movie_poster_movie_released_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='released_date',
        ),
        migrations.AlterField(
            model_name='movie',
            name='average_rating',
            field=models.TextField(default=0),
        ),
    ]
