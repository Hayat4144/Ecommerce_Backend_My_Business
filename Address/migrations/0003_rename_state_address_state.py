# Generated by Django 4.1.2 on 2022-11-03 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Address', '0002_rename_user_id_address_user_alter_address_state_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='State',
            new_name='state',
        ),
    ]