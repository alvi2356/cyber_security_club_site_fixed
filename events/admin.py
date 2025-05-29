from django.contrib import admin
from .models import Event, EventRegistration, EventImage

class EventRegistrationInline(admin.TabularInline):
    model = EventRegistration
    extra = 0
    readonly_fields = ("user", "timestamp")

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1 # Start with one empty form
    fields = ('image',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "event_type", "date", "location")
    list_filter = ("event_type", "date")
    inlines = [EventRegistrationInline, EventImageInline]
