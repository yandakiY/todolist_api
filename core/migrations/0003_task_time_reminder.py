# Generated by Django 5.0 on 2023-12-28 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_owner_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time_reminder',
            field=models.DateTimeField(blank=True, default=None, help_text='Time reminder for create a notification', null=True),
        ),
    ]