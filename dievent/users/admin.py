# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    
    list_display = [
        'username', 
        'email', 
        'first_name', 
        'last_name', 
        'role', 
        'phone',
        'is_staff', 
        'is_active',
        'date_joined',
        'last_activity'
    ]
    
    list_filter = [
        'role', 
        'is_staff', 
        'is_active', 
        'date_joined',
        'last_activity'
    ]
    
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {
            'fields': (
                'role', 
                'phone', 
                'company', 
                'avatar', 
                'bio',
                'telegram_messenger', 
                'whatsapp_messenger',
                'email_verified',
                'phone_verified',
                'last_activity'
            )
        }),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Дополнительная информация', {
            'fields': (
                'role', 
                'phone', 
                'company',
                'email_verified',
                'phone_verified',
                'last_activity',
                'last_activity'
            )
        }),
    )

    readonly_fields = ['last_activity']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'phone']
    ordering = ['-date_joined']