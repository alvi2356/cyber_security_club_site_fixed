from django.contrib import admin
from .models import FormerPresident

@admin.register(FormerPresident)
class FormerPresidentAdmin(admin.ModelAdmin):
    list_display = ('name', 'tenure')
    search_fields = ('name', 'tenure')
    list_filter = ('tenure',)
