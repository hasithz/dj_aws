# Generated by Django 3.2.7 on 2021-12-05 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_advetiesments'),
    ]

    operations = [
        migrations.AddField(
            model_name='advetiesments',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
