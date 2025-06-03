from django import forms
from .models import RecruitmentApplication

class RecruitmentApplicationForm(forms.ModelForm):
    class Meta:
        model = RecruitmentApplication
        fields = ['name', 'student_id', 'semester', 'contact', 'position', 'anchoring_skills', 'why_join', 'graphics_design_link', 'email']
        widgets = {
            'semester': forms.Select(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'anchoring_skills': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'why_join': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'graphics_design_link': forms.URLInput(attrs={'placeholder': 'e.g., https://drive.google.com/drive/folders/...', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your.email@example.com', 'class': 'form-control'}),
        }
        labels = {
            'student_id': 'ID',
            'why_join': 'Why do you want to join this club?',
            'graphics_design_link': 'Graphics Design Sample (Google Drive Link)',
            'email': 'Email Address',
        } 