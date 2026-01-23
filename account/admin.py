from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['is_staff','is_superuser','is_active']
    list_filter = ['username','email']
    search_fields = ('username',)
    ordering = ('create_date',)
    """
    to show and edit fields my customuser in admin 
    """
    fieldsets = (
        ('Authentication',{
            'fields':('username','email','password'),
        }),
        ('permissions',{
            'fields':('is_staff','is_superuser','is_active'),
        }),
        ('group_permissions',{
            'fields':('groups','user_permissions'),
        }),
        ('important_dates',{
            'fields':('last_login',),
        }),

    )
    """
    to show the fields when start create new user in admin
    """
    add_fieldsets = (
        ('create_user',{
            'classes':('wide',),
            'fields':('username','email','password1','password2','is_staff','is_superuser','is_active')
        }),
    )
admin.site.register(User,CustomUserAdmin)