from django.db import models

# Create your models here.

class FormerPresident(models.Model):
    name = models.CharField(max_length=150)
    tenure = models.CharField(max_length=100, help_text="e.g., 2020-2021")
    photo = models.ImageField(upload_to='former_presidents/', blank=True, null=True)

    class Meta:
        verbose_name = 'Former President'
        verbose_name_plural = 'Former Presidents'
        ordering = ['tenure']

    def __str__(self):
        return f'{self.name} ({self.tenure})'
