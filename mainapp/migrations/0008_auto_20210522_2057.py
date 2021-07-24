# Generated by Django 3.1.6 on 2021-05-22 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20210510_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='calendario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('superficie', models.CharField(choices=[('asfalto', 'asfalto'), ('trail', 'trail')], default='none', max_length=100)),
                ('region', models.CharField(choices=[('cantabria', 'Cantabria'), ('asturias', 'Asturias')], max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='tabla1',
            name='lugar',
        ),
        migrations.RemoveField(
            model_name='tabla1',
            name='mes',
        ),
        migrations.AddField(
            model_name='tabla1',
            name='fecha',
            field=models.DateField(default='2021-01-01'),
        ),
        migrations.AddField(
            model_name='tabla1',
            name='region',
            field=models.CharField(choices=[('cantabria', 'Cantabria'), ('asturias', 'Asturias')], default='none', max_length=100),
        ),
        migrations.AlterField(
            model_name='tabla1',
            name='superficie',
            field=models.CharField(choices=[('asfalto', 'asfalto'), ('trail', 'trail')], default='none', max_length=100),
        ),
    ]
