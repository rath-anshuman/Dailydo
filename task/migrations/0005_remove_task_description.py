# Generated by Django 4.2.14 on 2024-07-31 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_alter_task_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
    ]