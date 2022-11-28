from django.core.validators import MaxValueValidator, MinValueValidator 
from django.db import models
from shop.models import Product_item
from account.models import User
import uuid

# Create your models here.

class UserCart(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.full_name
    

class CartItem(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    cart = models.ForeignKey(UserCart,on_delete=models.CASCADE)
    productItem = models.ForeignKey(Product_item,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default = 10,validators=[MinValueValidator(10),MaxValueValidator(200)])

    def __str__(self):
        return self.productItem.product_id.name 
    
    def total_price_of_product_item(self):
        return self.productItem.price * self.quantity

