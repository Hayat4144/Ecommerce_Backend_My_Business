# Generated by Django 4.1.3 on 2022-11-30 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_attribute_attribute_option_product_attribute_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Varients',
        ),
        migrations.RemoveField(
            model_name='product_item',
            name='colour_id',
        ),
        migrations.RemoveField(
            model_name='product_item',
            name='material_id',
        ),
        migrations.RemoveField(
            model_name='product_item',
            name='size_id',
        ),
        migrations.DeleteModel(
            name='colour',
        ),
        migrations.DeleteModel(
            name='material',
        ),
        migrations.DeleteModel(
            name='size',
        ),
    ]
