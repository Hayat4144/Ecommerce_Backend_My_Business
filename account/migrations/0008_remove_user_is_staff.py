# Generated by Django 4.1.2 on 2022-10-27 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_user_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
