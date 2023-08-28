# Generated by Django 4.2.4 on 2023-08-26 11:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "name",
                    models.CharField(
                        max_length=30,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                limit_value=2, message="Убедитесь, что поле имени содержит не менее 2 символов."
                            )
                        ],
                        verbose_name="Имя",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=30,
                        validators=[
                            django.core.validators.EmailValidator(
                                message="Введите корректный адрес электронной почты."
                            )
                        ],
                        verbose_name="Эл. почта",
                    ),
                ),
                (
                    "subject",
                    models.CharField(
                        max_length=200,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                limit_value=4, message="Убедитесь, что поле темы содержит не менее 4 символов."
                            )
                        ],
                        verbose_name="Тема",
                    ),
                ),
                (
                    "message",
                    models.TextField(
                        validators=[
                            django.core.validators.MinLengthValidator(
                                limit_value=5, message="Убедитесь, что поле с сообщением содержит не менее 5 символов."
                            )
                        ],
                        verbose_name="Сообщение",
                    ),
                ),
            ],
        ),
    ]
