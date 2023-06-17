from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm

from .models import User


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Email address / Username"
        self.fields["username"].widget.attrs.update({"id": "id_email"})


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].label = "Email address"


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email",)
