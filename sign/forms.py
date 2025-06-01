from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['student_id', 'name', 'email', 'password']

class LoginForm(forms.Form):
    student_id = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
