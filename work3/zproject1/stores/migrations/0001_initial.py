# Generated by Django 3.2.7 on 2021-10-05 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('store_type', models.CharField(choices=[('Com', 'Computer'), ('Mob', 'Mobile'), ('Grs', 'Grocessory'), ('Tex', 'Textile'), ('Fod', 'Food'), ('Oth', 'Other')], default='Non', max_length=3)),
                ('image', models.ImageField(blank=True, upload_to='stores/')),
            ],
        ),
        migrations.CreateModel(
            name='StoreItems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('discription', models.TextField()),
                ('discount', models.FloatField()),
                ('price', models.FloatField()),
                ('No_of_items', models.IntegerField()),
                ('item_image', models.ImageField(blank=True, upload_to='storeItems/')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.store')),
            ],
        ),
    ]
