from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-field', 'placeholder': 'Wpisz nazwę użytkownika'})
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-field', 'placeholder': 'Wpisz hasło'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-field', 'placeholder': 'Potwierdź hasło'})

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-field', 'placeholder': 'Nazwa użytkownika'})
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'form-field', 'placeholder': 'Hasło'})

    class Meta: 
        model = User
        fields = ('username', 'password')
