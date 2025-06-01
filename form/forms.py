# form/forms.py
from django import forms
from .models import Application

class ApplicationFormModelForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['student_id', 'name', 'department', 'email', 'motivation', 'spec']
