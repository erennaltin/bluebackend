# Generated by Django 3.2 on 2021-05-13 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_posts_approvals'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approval',
            name='uuid',
        ),
        migrations.AddField(
            model_name='approval',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
