# Generated by Django 4.1.2 on 2022-10-31 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_remove_attribute_attribute_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='attribute_name',
            field=models.CharField(choices=[('size', 'size')], default='size', max_length=10),
        ),
    ]