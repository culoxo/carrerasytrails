# Generated by Django 3.1.6 on 2021-04-21 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='publicado',
        ),
        migrations.AddField(
            model_name='article',
            name='lugar',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
