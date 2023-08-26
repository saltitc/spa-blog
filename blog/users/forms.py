from django import forms
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.mail import send_mail

from .models import User, Feedback


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


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': "Ваше имя"
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': "Ваша почта"
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'subject',
                'placeholder': "Тема"
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control md-textarea',
                'id': 'message',
                'rows': 2,
                'placeholder': "Ваше сообщение"
            }),
        }

    def save(self, commit=True):
        data = self.cleaned_data

        # sending email
        send_mail(
            subject=f"От {data['name']}({data['email']}) | {data['subject']}",
            message=data['message'],
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        super().save(commit=True)