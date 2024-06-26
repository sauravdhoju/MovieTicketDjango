# Generated by Django 5.0.4 on 2024-04-16 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_wactor_movietodirector_director_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movietoactor',
            name='actor',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movietoactor',
            name='movie',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movietodirector',
            name='director',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movietodirector',
            name='movie',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movietogenre',
            name='genre',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movietogenre',
            name='movie',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movietolanguage',
            name='language',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movietolanguage',
            name='movie',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movietowriter',
            name='movie',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movietowriter',
            name='writer',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='writer',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
