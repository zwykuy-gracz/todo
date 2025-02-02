from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import Task, User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["task", "deadline", "comment", "status", "duration_lvl"]

    deadline = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"})
    )


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(_("The given email is already registered."))
        return email

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError(
                _("This username is already taken. Please choose another one.")
            )
        return username

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email"]
