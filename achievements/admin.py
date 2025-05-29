from django.contrib import admin
from .models import Achievement

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'achieved_on')
    list_filter = ('achieved_on',)
    search_fields = ('title',)
