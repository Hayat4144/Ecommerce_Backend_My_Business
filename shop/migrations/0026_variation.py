# Generated by Django 4.1.3 on 2022-11-30 06:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_remove_shopping_cart_item_product_item_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='variation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('variation_name', models.CharField(max_length=50)),
            ],
        ),
    ]
