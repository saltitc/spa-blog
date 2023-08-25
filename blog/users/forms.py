from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


from .models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Введите имя пользователя"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control mt-2',
        'placeholder': "Введите пароль"}))


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'gender', 'email', 'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control mt-2',
                'placeholder': "Введите имя"}),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control mt-2',
                'placeholder': "Введите фамилию"}),
            'username': forms.TextInput(attrs={
                'class': 'form-control mt-2',
                'placeholder': "Введите имя пользователя"}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control mt-2',
                'placeholder': "Введите адрес эл. почты"}),
            'gender': forms.Select(choices=User.GENDER_CHOICES, attrs={
                'class': 'form-control mt-2'}),
        }

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control mt-2',
        'placeholder': "Введите пароль"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control mt-2',
        'placeholder': "Подтвердите пароль"}))

