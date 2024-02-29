from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import User


def get_widget(placeholder):
    return forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": _(placeholder)
        }
    )


class BasicUserForm:
    password1 = forms.CharField(
        label=_("Password"),
        widget=get_widget("Password"),
        help_text=_("Your password must be at least 3 characters long"),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=get_widget("Password confirmation"),
        help_text=_("To confirm, please enter your password again"),
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
        )


class RegisterUserForm(UserCreationForm, BasicUserForm):
    pass


class UpdateUserForm(UserChangeForm, BasicUserForm):
    password = None

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords don't match"))
        return password2
