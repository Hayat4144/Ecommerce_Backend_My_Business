# Generated by Django 4.1.3 on 2022-11-30 06:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_variation_option'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_item_configuration',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.variation')),
                ('variation_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.variation_option')),
            ],
        ),
    ]
