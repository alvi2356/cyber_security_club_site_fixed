from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, ContactMessage

class CustomUserAdmin(UserAdmin):
    admin.site.site_header = "Admin Panel"
    admin.site.site_title = "My Admin Portal"
    admin.site.index_title = "Management"
    model = CustomUser
    fieldsets = UserAdmin.fieldsets

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact_number', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'contact_number', 'subject', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    actions = ['mark_as_read', 'mark_as_unread']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"

    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Mark selected messages as unread"

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
