# Generated by Django 3.2 on 2021-05-29 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0031_posts_objections'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='Photo',
            field=models.TextField(default='', max_length=3000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='approval',
            name='name',
            field=models.CharField(default='', max_length=2200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(default='', max_length=2200),
        ),
        migrations.AlterField(
            model_name='decline',
            name='name',
            field=models.CharField(default='', max_length=2200),
        ),
        migrations.AlterField(
            model_name='posts',
            name='Category',
            field=models.CharField(max_length=309),
        ),
        migrations.AlterField(
            model_name='posts',
            name='Tags',
            field=models.TextField(max_length=620),
        ),
        migrations.AlterField(
            model_name='posts',
            name='Title',
            field=models.TextField(max_length=3000),
        ),
    ]
