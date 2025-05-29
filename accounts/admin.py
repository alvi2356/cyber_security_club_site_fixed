
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    admin.site.site_header = "Admin Panel"
    admin.site.site_title = "My Admin Portal"
    admin.site.index_title = "Management"
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("full_name",)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
