from django.db import models
from django.conf import settings

class Member(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="team/")
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.full_name or self.user.username} ({self.position})"

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='team_members/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Order in which member appears")
    github_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.position})"
