from django.db import models

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    achieved_on = models.DateField()

    def __str__(self):
        return self.title

# New Model for Former Presidents
class FormerPresident(models.Model):
    name = models.CharField(max_length=150)
    tenure = models.CharField(max_length=100, help_text="e.g., 2020-2021")
    image = models.ImageField(upload_to='former_presidents/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Order in which president appears")

    class Meta:
        ordering = ['order', 'tenure', 'name']

    def __str__(self):
        return f'{self.name} ({self.tenure})'
