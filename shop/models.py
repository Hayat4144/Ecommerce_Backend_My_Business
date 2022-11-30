
from django.db import models
import uuid
from django.utils.html import escape
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField
from account.models import User 
from django.core.validators import MaxValueValidator, MinValueValidator 

def validation_html(value):
    return escape(value)



class Product(models.Model):
    id = models.UUIDField(validators=[validation_html],primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(validators=[validation_html],max_length=50, blank=False)
    descriptions = models.CharField(validators=[validation_html],max_length=100)
    limited = models.BooleanField(validators=[validation_html],default =False)
    regular_price = models.IntegerField(validators=[validation_html], blank=False)
    image = CloudinaryField('image',folder='Ecommerce/product')
    categories = models.ForeignKey('Category', related_name="cate", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    updated_at = models.DateTimeField(auto_now=True, blank=True, help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    deleted_at = models.DateField(auto_now_add=True, blank=True, help_text="Please use the following format: <em>YYYY-MM-DD</em>.")

    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.UUIDField(validators=[validation_html],primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(validators=[validation_html],max_length=50, blank=True ,null=True)
    description = models.CharField(validators=[validation_html],max_length=100,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    updated_at = models.DateTimeField(auto_now=True, blank=True, help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    deleted_at = models.DateField(auto_now_add=True, blank=True, help_text="Please use the following format: <em>YYYY-MM-DD</em>.")

    def __str__(self):
        return self.name
    


class Product_item(models.Model):
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    sku = models.CharField(max_length = 250)
    price = models.IntegerField()

    def __str__(self):
        return self.product_id.name 


class attribute(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    attribute_name = models.CharField(max_length=50 ,null=False)
    attribute_value = models.CharField(max_length=50 , null=False, default="")

    def __str__(self):
        return self.attribute_value


class product_attribute(models.Model):
    id = models.UUIDField(default = uuid.uuid4, editable =False, primary_key = True)
    attribute =models.ForeignKey(attribute , on_delete = models.CASCADE )
    productItem = models.ForeignKey(Product_item, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.productItem.product_id.name
