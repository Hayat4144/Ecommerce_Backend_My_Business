# Generated by Django 4.1.2 on 2022-10-27 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_user_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mom',
            field=models.CharField(default='hello', max_length=50),
        ),
    ]
