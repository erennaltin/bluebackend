# Generated by Django 3.2 on 2021-05-09 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20210509_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='images/default.png', help_text='Upload a post image', upload_to='images/', verbose_name='image')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_image', to='backend.posts')),
            ],
            options={
                'verbose_name': 'Post Image',
                'verbose_name_plural': 'Post Images',
            },
        ),
        migrations.DeleteModel(
            name='PostImages',
        ),
    ]
