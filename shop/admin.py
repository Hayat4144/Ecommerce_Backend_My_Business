from django.contrib import admin
from django.db import models
from .models import Varients,Product ,Category,size,colour,material, Product_item 

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
    model = Product_item 
    list_filter = ('price',)
    list_display = ('id','product_id','size_id','colour_id','price')

# class Shopping_cartAdmin(admin.ModelAdmin):
#     model = shopping_cart
#     list_display = ('id','user_id')


# class Shopping_Cart_itemAdmin(admin.ModelAdmin):
#     model= shopping_cart_item
#     list_display = ('product_item','quantity')
#     list_filter = ('product_item',)

# class Whishlist_Admin(admin.ModelAdmin):
#     class Meta:
#         model =Whishlist
#         list_display=('user',)
#         list_filter=('user',)

# class Whishlist_item_Admin(admin.ModelAdmin):
#     class Meta:
#         models = Whishlist_item
#         list_display= ('whishlist','product_item')
#         list_filter= ('whish_list','product_item')

# admin.site.register(Whishlist_item,Whishlist_item_Admin)
# admin.site.register(Whishlist,Whishlist_Admin)
admin.site.register(Product_item,Product_itemAdmin)
admin.site.register(Product,CustomProductAmdin)
admin.site.register(Varients)
admin.site.register(Category,CustomeCategoryAdmin)
admin.site.register(size,SizeAdmin)
admin.site.register(colour,ColourAdmin)
admin.site.register(material,materialAdmin)
# admin.site.register(shopping_cart,Shopping_cartAdmin)
# admin.site.register(shopping_cart_item,Shopping_Cart_itemAdmin)
