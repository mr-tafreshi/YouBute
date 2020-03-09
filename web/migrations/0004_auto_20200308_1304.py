# Generated by Django 3.0.4 on 2020-03-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_activity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='publish',
            new_name='activity_pubdate',
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_path',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_url',
            field=models.URLField(default=''),
        ),
    ]
