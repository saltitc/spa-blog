from django.core.validators import MinLengthValidator, EmailValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = [
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    ]
    gender = models.CharField(max_length=2, verbose_name='Пол', choices=GENDER_CHOICES, default=MALE)
    email = models.EmailField(unique=True, verbose_name='Эл. почта', error_messages={
        'unique': "Аккаунт с данной электронной почтой уже существует.",
    })
    is_verified_email = models.BooleanField(default=False)


class Feedback(models.Model):
    name = models.CharField(
        max_length=30, verbose_name='Имя', validators=[MinLengthValidator(
            limit_value=2, message='Убедитесь, что поле имени содержит не менее 2 символов.'
        )])
    email = models.EmailField(
        max_length=30, verbose_name='Эл. почта', validators=[EmailValidator(
            message='Введите корректный адрес электронной почты.'
        )])
    subject = models.CharField(
        max_length=200, verbose_name='Тема', validators=[MinLengthValidator(
            limit_value=4, message='Убедитесь, что поле темы содержит не менее 4 символов.'
        )])
    message = models.TextField(
        verbose_name='Сообщение', validators=[MinLengthValidator(
            limit_value=5, message='Убедитесь, что поле с сообщением содержит не менее 5 символов.'
        )])
