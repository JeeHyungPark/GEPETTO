from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = (
            'nickname',
            'password',
            'email',
            'gender',
            'age',
        )   
        widgets = {
            'nickname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'gender': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }

class LoginForm(forms.Form):
    """user login form"""

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    