from django.contrib import admin
from .models import UserCart, CartItem

# Register your models here.
class CartItemAdmin(admin.ModelAdmin):
    model = CartItem
    list_display = ("cart", "productItem", "quantity")


admin.site.register(UserCart)
admin.site.register(CartItem, CartItemAdmin)
