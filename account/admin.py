from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User ,Token


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('full_name','email', 'is_staff', 'is_active','mobile_no',)
    list_filter = ('email', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'full_name','mobile_no')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class TokenAdmin(admin.ModelAdmin):
    model = Token
    list_display= ('user','token_value')
    list_filter = ('user',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Token,TokenAdmin)
