# Generated by Django 3.2 on 2021-05-11 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20210509_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='PublishDate',
        ),
        migrations.AddField(
            model_name='posts',
            name='Photo',
            field=models.ImageField(default='/images/default.png', upload_to='', verbose_name='post_image'),
        ),
    ]
