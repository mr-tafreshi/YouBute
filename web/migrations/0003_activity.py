# Generated by Django 3.0.4 on 2020-03-08 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('web', '0002_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('activity_id', models.AutoField(primary_key=True, serialize=False)),
                ('publish', models.DateField(auto_now=True)),
            ],
        ),
    ]
