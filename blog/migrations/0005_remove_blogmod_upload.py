# Generated by Django 3.2.18 on 2023-05-22 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blogmod_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmod',
            name='upload',
        ),
    ]
