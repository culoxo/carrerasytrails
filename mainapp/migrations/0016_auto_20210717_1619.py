# Generated by Django 3.1.6 on 2021-07-17 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20210711_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendario',
            name='distancia',
            field=models.CharField(choices=[('1milla', '1milla'), ('5km', '5km'), ('10km', '10km'), ('15km', '15km'), ('21.096km', '21.096km'), ('42.192km', '42.192km')], default='none', max_length=100),
        ),
        migrations.AlterField(
            model_name='calendario',
            name='region',
            field=models.CharField(choices=[('Cantabria', 'Cantabria'), ('Asturias', 'Asturias'), ('País Vasco', 'País Vasco')], default='none', max_length=100),
        ),
    ]
