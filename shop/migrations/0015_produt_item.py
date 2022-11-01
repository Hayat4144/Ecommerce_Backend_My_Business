# Generated by Django 4.1.2 on 2022-10-31 13:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_remove_product_available_colors_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produt_item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sku', models.CharField(max_length=250)),
                ('stock', models.ImageField(max_length=10, upload_to='')),
                ('price', models.IntegerField()),
                ('colour_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.colour')),
                ('material_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.material')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('size_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.size')),
            ],
        ),
    ]
