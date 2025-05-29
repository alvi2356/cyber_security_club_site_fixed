
from django import forms
from .models import Member

class MemberPhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ("position", "photo")
