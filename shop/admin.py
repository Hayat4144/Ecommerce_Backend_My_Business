from django.contrib import admin
from django.db import models
from .models import Product ,Category,size,colour,material, Produt_item

class CustomProductAmdin(admin.ModelAdmin):
    model = Product
    list_display = ('name','descriptions','regular_price','categories')
    list_filter = ('name','regular_price')
    
class CustomeCategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display= ('name','description')
    list_filter = ('name',)

class SizeAdmin(admin.ModelAdmin):
    model = size
    list_display = ('id','value')
    list_filter = ('value',)

class ColourAdmin(admin.ModelAdmin):
    model = colour
    list_filter =('value',)
    list_display = ('id','value')

class materialAdmin(admin.ModelAdmin):
    model = material
    list_display =('id','value')
    list_filter = ('value',)

class Product_itemAdmin(admin.ModelAdmin):
    model = Produt_item 
    list_filter = ('price',)
    list_display = ('product_id','size_id','colour_id','price')

    
admin.site.register(Produt_item,Product_itemAdmin)
admin.site.register(Product,CustomProductAmdin)
admin.site.register(Category,CustomeCategoryAdmin)
admin.site.register(size,SizeAdmin)
admin.site.register(colour,ColourAdmin)
admin.site.register(material,materialAdmin)
