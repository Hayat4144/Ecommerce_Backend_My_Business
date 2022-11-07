from django.contrib import admin
from .models import address

class AddressAdmin(admin.ModelAdmin):
    model = address
    list_display = ('country_name','user','address_line')
    list_filter = ('country_name','user','postal_code')


admin.site.register(address,AddressAdmin)
