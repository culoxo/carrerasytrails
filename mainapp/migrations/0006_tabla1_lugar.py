# Generated by Django 3.1.6 on 2021-05-01 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210501_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabla1',
            name='lugar',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
