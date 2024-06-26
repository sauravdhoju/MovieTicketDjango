# Generated by Django 5.0.4 on 2024-04-16 05:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_actor_director_writer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Poster',
        ),
        migrations.AddField(
            model_name='movie',
            name='released_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='movie',
            name='length',
            field=models.TextField(default='0 min'),
        ),
        migrations.CreateModel(
            name='MovieToLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.movie')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.language')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.URLField(blank=True, null=True),
        ),
    ]
