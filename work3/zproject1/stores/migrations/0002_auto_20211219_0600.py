# Generated by Django 3.2.7 on 2021-12-19 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='image',
        ),
        migrations.RemoveField(
            model_name='store',
            name='store_type',
        ),
    ]
