from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'your.email@uap-bd.edu'}))
    first_name = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}))
    last_name = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}))
    student_id = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'e.g., 20-12345-1'}))
    academic_year = forms.ChoiceField(label="Semester", choices=[
        ('', 'Select your semester'),
        ('1-1', '1-1'),
        ('1-2', '1-2'),
        ('2-1', '2-1'),
        ('2-2', '2-2'),
        ('3-1', '3-1'),
        ('3-2', '3-2'),
        ('4-1', '4-1'),
        ('4-2', '4-2'),
    ], required=True)
    department = forms.ChoiceField(choices=[
        ('', 'Select your department'),
        ('CSE', 'CSE'),
        ('EEE', 'EEE'),
        ('BBA', 'BBA'),
        ('CIVIL', 'CIVIL'),
        ('PHARMACY', 'PHARMACY'),
        ('ENGLISH', 'ENGLISH'),
        ('ARCH', 'ARCH'),
        ('L&HR', 'L&HR'),
        ], required=True)
    password1 = forms.CharField(
        label="Password",
        widget=PasswordInput(attrs={'placeholder': 'Create a password'}),
        help_text="Your password must contain at least 8 characters."
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=PasswordInput(attrs={'placeholder': 'Confirm your password'}),
        help_text="Enter the same password as before, for verification."
    )
    username = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'student_id', 'academic_year', 'department', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']  # Use email as username
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.student_id = self.cleaned_data['student_id']
        user.academic_year = self.cleaned_data['academic_year']
        user.department = self.cleaned_data['department']
        if commit:
            user.save()
        return user

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'your.email@example.com'}))
    contact_number = forms.CharField(max_length=15, required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your contact number (optional)'}))
    subject = forms.CharField(max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'What\'s this about?'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Tell us more about your inquiry...'}))
