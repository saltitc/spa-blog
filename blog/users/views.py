from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView

from .forms import FeedbackForm, UserLoginForm, UserRegistrationForm
from .models import User


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    title = "Авторизация"


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "users/registration.html"
    success_url = reverse_lazy("users:login")
    success_message = "Вы успешно зарегистрированы!"
    title = "Регистрация"


class FeedbackFormView(FormView):
    """
    Feedback form template

    In GET: Returns a template with a feedback web form
    IN POST: Creates a Feedback object in the database, sends an email with feedback to the host's email
             and shows a message about the successful receipt of the user's feedback

    Template: feedback.html
    """

    form_class = FeedbackForm
    template_name = "users/feedback.html"
    success_url = reverse_lazy("users:feedback")

    def form_valid(self, form):
        # shows a message about the successful receipt of the user's feedback
        messages.success(self.request, f'{self.request.POST["name"]}, спасибо за оставленное вами обращение.')

        # creates a Feedback object
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Написать мне"
        return context
