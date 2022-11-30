from django.contrib import admin
from django.db import models
from .models import Product ,Category, Product_item  ,product_attribute , attribute
class CustomProductAmdin(admin.ModelAdmin):
    model = Product
    list_display = ('name','descriptions','regular_price','categories')
    list_filter = ('name','regular_price')
    
class CustomeCategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display= ('name','description')
    list_filter = ('name',)


class Product_itemAdmin(admin.ModelAdmin):
    model = Product_item 
    list_filter = ('price',)
    list_display = ('id','product_id','price')


class product_attribute_Admin(admin.ModelAdmin):
    model = product_attribute
    list_display = ('attribute','productItem')


class AttributeAdmin(admin.ModelAdmin):
    model = attribute
    list_display = ('attribute_name','attribute_value')


admin.site.register(Product_item,Product_itemAdmin)
admin.site.register(Product,CustomProductAmdin)
admin.site.register(Category,CustomeCategoryAdmin)
admin.site.register(product_attribute ,product_attribute_Admin)
admin.site.register(attribute,AttributeAdmin)

