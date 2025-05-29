from django.db import models

# Create your models here.

class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('convenor', 'Convenor'),
        ('main_committee', 'Main Committee'),
        ('representative', 'Representative'),
    ]
    
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    sub_role = models.CharField(max_length=100, blank=True, null=True) # e.g., President, Secretary
    image = models.ImageField(upload_to='team_members/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Order in which member appears")

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"
