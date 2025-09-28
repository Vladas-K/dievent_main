from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = [
        'username', 
        'email', 
        'first_name', 
        'last_name', 
        'role', 
        'phone',
        'is_staff', 
        'is_active',
        'date_joined'
    ]
    
    list_filter = [
        'role', 
        'is_staff', 
        'is_active', 
        'date_joined'
    ]
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
            'fields': (
                'first_name', 'last_name', 'email',
                'role', 'phone', 'company', 'avatar', 'bio',
                'telegram_messenger', 'whatsapp_messenger', 'max_messenger',
                'email_verified', 'phone_verified'
            )
        }),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            ),
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined', 'last_activity'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['last_login', 'date_joined', 'last_activity']
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email'),
        }),
        ('Дополнительная информация', {
            'fields': (
                'role', 'phone', 'company',
                'email_verified', 'phone_verified'
            ),
        }),
    )
    
    search_fields = ['username', 'email', 'first_name', 'last_name', 'phone']
    ordering = ['-date_joined']
