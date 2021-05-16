# Generated by Django 3.2 on 2021-05-13 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_auto_20210513_1654'),
        ('customuser', '0005_account_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='photo',
        ),
        migrations.AddField(
            model_name='account',
            name='approvals',
            field=models.ManyToManyField(blank=True, default='', to='backend.Approval'),
        ),
    ]
