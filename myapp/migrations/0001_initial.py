# Generated by Django 4.1.5 on 2023-01-05 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busname', models.CharField(max_length=100)),
                ('numPass', models.IntegerField(max_length=100)),
                ('eta', models.IntegerField(max_length=200)),
            ],
        ),
    ]