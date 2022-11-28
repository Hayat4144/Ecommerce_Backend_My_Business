from django.db import models
import uuid
from shop.models import Product_item
from account.models import User

# Create your models here.
class UserWhishlist(models.Model):
    id= models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.full_name

class WhishlistItem(models.Model):
    id= models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    whishlist = models.ForeignKey(UserWhishlist,on_delete=models.CASCADE)
    productItem = models.ForeignKey(Product_item,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.productItem.product_id.name