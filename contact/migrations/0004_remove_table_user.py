# Generated by Django 3.1 on 2020-08-16 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_table_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='user',
        ),
    ]
