from django.contrib import admin
from .models import Stock

# Register your models here.
class StockItemAdmin(admin.ModelAdmin):
    class Meta:
        model = Stock
        list_display= ('productItem','stock_quantity')
        list_filter = ('productItem','stock_quantity')

admin.site.register(Stock,StockItemAdmin)
