# Generated by Django 4.1.3 on 2022-11-30 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0031_remove_attribute_option_attribute_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attribute_option',
            name='attribute',
        ),
    ]
