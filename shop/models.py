
from django.db import models
import uuid
from django.utils.html import escape
# Create your models here.
from django.core.exceptions import ValidationError
#from .serializers import VarientsSerializer 



def validation_html(value):
    return escape(value)



class Product(models.Model):
    id = models.UUIDField(validators=[validation_html],primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(validators=[validation_html],max_length=50, blank=False)
    descriptions = models.CharField(validators=[validation_html],max_length=100)
    limited = models.BooleanField(validators=[validation_html],default =False)
    regular_price = models.IntegerField(validators=[validation_html], blank=False)
    image = models.ImageField(blank=False,upload_to='upload/image')
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
    

class Varients(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True,validators=[validation_html], editable=False)
    varients_name = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.varients_name 


class size(models.Model):
    id = models.UUIDField(default= uuid.uuid4, primary_key = True, editable = False)
    value= models.CharField(max_length=20)
    

    def __str__(self):
        return self.value

class material(models.Model):
    id = models.UUIDField(default = uuid.uuid4, primary_key =True,editable=False)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.value


class colour(models.Model):
    id = models.UUIDField(default = uuid.uuid4 ,primary_key = True,editable = False)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.value


class Produt_item(models.Model):
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    size_id = models.ForeignKey(size,on_delete = models.CASCADE)
    colour_id = models.ForeignKey(colour, on_delete = models.CASCADE)
    material_id = models.ForeignKey(material, on_delete = models.CASCADE)
    sku = models.CharField(max_length = 250)
    stock = models.IntegerField()
    price = models.IntegerField()


    def __str__(self):
        return self.product_id.name 

