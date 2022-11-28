from django.db import models
import uuid
from shop.models import Product_item 

class Stock(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    productItem = models.ForeignKey(Product_item,on_delete=models.CASCADE)
    stock_quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.productItem.product_id.name
    
    def total_stock_of_item(self):
        return self.stock_quantity
