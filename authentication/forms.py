from django.forms import ModelForm
# importing default user registration form
from django.contrib.auth.forms import UserCreationForm
# importing built-in user model
from django.contrib.auth.forms import User
from django import forms
from ads.models import Author

from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',  
        'name': 'username', 
        'placeholder': 'Имя пользователя'
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control',  
        'name': 'password1', 
        'placeholder': 'Пароль'
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control',  
        'name': 'password2', 
        'placeholder': 'Повторите пароль'
    }))
    
    email = forms.EmailField(required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type': 'email',
        'class': 'form-control',  
        'placeholder': 'Электронная почта'
    }))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        duplicate_email = User.objects.filter(email=email).exists()
        if duplicate_email:
            raise forms.ValidationError("Этот адрес электронной почты уже используется.")
        return email


class EmailValidationOnForgotPassword(PasswordResetForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={
        'type': 'email',
        'class': 'form-control',  
        'placeholder': 'Электронная почта'
    }))

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise forms.ValidationError("Пользователь с указанным адресом электронной почты не зарегистрирован.")

        return email


class EmailSetPassword(SetPasswordForm):
    new_password1 = forms.CharField(label="", widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control',  
        'name': 'new_password1', 
        'placeholder': 'Пароль'
    }))

    new_password2 = forms.CharField(label="", widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control',  
        'name': 'new_password2', 
        'placeholder': 'Повторите пароль'
    }))


class UserUpdateForm(ModelForm):
    first_name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',  
        'name': 'first_name',
        'placeholder': 'Имя'
    }))

    last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',  
        'name': 'last_name', 
        'placeholder': 'Фамилия'
    }))

    email = forms.EmailField(label="Почта", widget=forms.TextInput(attrs={
        'type': 'email',
        'class': 'form-control',  
        'placeholder': 'Электронная почта'
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        # exclude = ['user']


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Author
        fields = ['profile_pic']