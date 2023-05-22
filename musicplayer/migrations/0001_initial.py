# Generated by Django 3.2.18 on 2023-05-22 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='music/')),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]
