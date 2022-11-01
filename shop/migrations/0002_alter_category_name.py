# Generated by Django 4.1.2 on 2022-10-29 13:44

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_drop_all_all_tables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[shop.models.validation_html]),
        ),
    ]
