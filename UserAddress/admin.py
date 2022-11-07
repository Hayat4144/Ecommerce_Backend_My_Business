from django.contrib import admin
from .models import address, user_address, Country
# Register your models here.


class AddressAdmin(admin.ModelAdmin):
    model  = address
    list_filter = ('city','State')
    list_display = ('city','State','address_line')


class CountryAdmin(admin.ModelAdmin):
    model = Country
    list_display =('id','country_name')
    list_filter = ('country_name',)

class user_address_admin(admin.ModelAdmin):
    model = user_address
    list_filter=('user_id',)
    list_display = ('user_id','address_id')

admin.site.register(address,AddressAdmin)
admin.site.register(user_address,user_address_admin)
admin.site.register(Country,CountryAdmin)

