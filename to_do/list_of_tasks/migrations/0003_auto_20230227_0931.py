# Generated by Django 2.2.19 on 2023-02-27 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list_of_tasks', '0002_auto_20230227_0913'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('-name',)},
        ),
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
    ]