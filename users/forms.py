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
        fields = ("username", "email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].label = "Email address"

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')

        if User.objects.filter(email=email).exists():
            self.add_error('email', 'This email is already registered.')
    
        if User.objects.filter(username=username).exists():
            self.add_error('username', 'This username is already registered.')

        return cleaned_data


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email",)
