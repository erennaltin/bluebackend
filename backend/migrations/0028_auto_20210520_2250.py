# Generated by Django 3.2 on 2021-05-20 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0027_alter_posts_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='Photo',
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]
