from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput

from .models import Property

# Register a User (Model Form)
class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

# Authenticate a User (Model Form)
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Password'})
    )

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            "name", "apartment_number", "building_name", "street_one", "street_two",
            "city", "municipality", "country", "post_code"
            ]