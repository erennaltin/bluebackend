# Generated by Django 3.2 on 2021-05-17 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0018_account_approvals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='photo',
            field=models.ImageField(default='userdefault.png', upload_to='', verbose_name='user_image'),
        ),
    ]
