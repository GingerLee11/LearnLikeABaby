from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustUserManager


class User(AbstractUser):
    """
    Create a custom user so that an email can be used in place of a username
    and/or other customizations can take place with the users.
    """
    email = models.EmailField(_('Email Address'), unique=True)
    email_verified = models.BooleanField(_('Email Verified'), default=False)
    username = models.CharField(_("Username"), max_length=150, unique=True)

    objects = CustUserManager()
    
    def __str__(self):
        return f"{self.username}"
    
