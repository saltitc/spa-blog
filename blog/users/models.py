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