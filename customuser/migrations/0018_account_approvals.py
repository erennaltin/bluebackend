# Generated by Django 3.2 on 2021-05-17 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0026_auto_20210514_1718'),
        ('customuser', '0017_account_approvals'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='Approvals',
            field=models.ManyToManyField(blank=True, to='backend.Approval'),
        ),
    ]
