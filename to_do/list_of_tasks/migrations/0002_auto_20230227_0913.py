# Generated by Django 2.2.19 on 2023-02-27 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_of_tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
