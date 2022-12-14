# Generated by Django 4.1.3 on 2022-11-28 09:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0025_remove_shopping_cart_item_product_item_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.PositiveBigIntegerField(default=10, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(200)])),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cart.usercart')),
                ('productItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product_item')),
            ],
        ),
    ]
