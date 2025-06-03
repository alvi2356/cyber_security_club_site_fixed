from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class RecruitmentDrive(models.Model):
    name = models.CharField(max_length=100, unique=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=False, verbose_name='Currently Active')

    def clean(self):
        # Ensure only one instance is active at a time
        if self.is_active:
            if RecruitmentDrive.objects.filter(is_active=True).exclude(pk=self.pk).exists():
                raise ValidationError('Only one recruitment drive can be active at a time.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class RecruitmentApplication(models.Model):
    SEMESTER_CHOICES = [
        ('1-1', '1-1'),
        ('1-2', '1-2'),
        ('2-1', '2-1'),
        ('2-2', '2-2'),
        ('3-1', '3-1'),
        ('3-2', '3-2'),
        ('4-1', '4-1'),
        ('4-2', '4-2'),
    ]

    POSITION_CHOICES = [
        ('media_publication', 'Media and Publication'),
        ('executive', 'Executive'),
        ('representative', 'Representative'),
        ('graphics_designer', 'Graphics Designer'),
    ]

    drive = models.ForeignKey(RecruitmentDrive, on_delete=models.CASCADE, related_name='applications', null=True, blank=True)
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, verbose_name='ID')
    semester = models.CharField(max_length=5, choices=SEMESTER_CHOICES)
    contact = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)  # <- this line was likely misindented
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    anchoring_skills = models.TextField(blank=True, null=True, verbose_name='Anchoring Skills')
    why_join = models.TextField(verbose_name='Why do you want to join this club?')
    graphics_design_link = models.URLField(blank=True, null=True, verbose_name='Graphics Design Sample (Google Drive Link)')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.position} ({self.drive.name if self.drive else 'No Drive'})"


class RecruitmentSetting(models.Model):
    is_active = models.BooleanField(default=True, verbose_name='Recruitment is Active')

    def clean(self):
        # Ensure only one instance of this model exists
        if RecruitmentSetting.objects.exists() and not self.pk:
            raise ValidationError('You can only have one recruitment setting.')

    def save(self, *args, **kwargs):
        # Enforce the single instance rule on save
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Recruitment Setting'

    class Meta:
        verbose_name = 'Recruitment Setting'
        verbose_name_plural = 'Recruitment Settings'
