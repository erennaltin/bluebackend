# Generated by Django 3.2 on 2021-05-13 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0018_remove_approval_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='Approvals',
        ),
        migrations.AddField(
            model_name='approval',
            name='post',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='backend.posts'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='approval',
            name='user',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='customuser.account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='approval',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
