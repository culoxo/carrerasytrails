# Generated by Django 3.1.6 on 2021-05-22 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20210522_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendario',
            name='region',
            field=models.CharField(choices=[('cantabria', 'Cantabria'), ('asturias', 'Asturias')], default='none', max_length=100),
        ),
        migrations.AlterField(
            model_name='tabla1',
            name='fecha',
            field=models.DateField(),
        ),
    ]
