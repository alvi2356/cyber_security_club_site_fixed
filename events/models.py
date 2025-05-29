from django.db import models
from django.conf import settings

class Event(models.Model):
    EVENT_TYPES = [
        ('seminar', 'Seminar'),
        ('workshop', 'Workshop'),
        ('ctf', 'CTF'),
        ('contest', 'Contest'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to="events/", blank=True, null=True)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES, default='seminar')

    def __str__(self):
        return self.title

class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='event_gallery/')

    def __str__(self):
        return f"Image for {self.event.title}"

class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="registrations")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("event", "user")
        verbose_name = "Event Registration"
        verbose_name_plural = "Event Registrations"

    def __str__(self):
        return f"{self.user} registered for {self.event}"
