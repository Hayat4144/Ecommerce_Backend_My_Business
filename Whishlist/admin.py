from django.contrib import admin
from .models import UserWhishlist ,WhishlistItem

# Register your models here.


admin.site.register(UserWhishlist)
admin.site.register(WhishlistItem)