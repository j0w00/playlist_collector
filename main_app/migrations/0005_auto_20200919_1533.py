# Generated by Django 3.1.1 on 2020-09-19 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_playlist_songs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(blank=True, to='main_app.Song'),
        ),
    ]