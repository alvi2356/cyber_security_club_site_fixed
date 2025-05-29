from django.contrib import admin
from .models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'position')
    list_filter = ('position',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'position', 'order')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Social Links', {
            'fields': ('github_url', 'facebook_url', 'linkedin_url'),
            'classes': ('collapse',)
        }),
    )
