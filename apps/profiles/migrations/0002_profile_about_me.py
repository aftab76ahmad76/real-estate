# Generated by Django 3.2.7 on 2022-10-22 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_me',
            field=models.TextField(default='Say something about yourself', verbose_name='About Me'),
        ),
    ]
