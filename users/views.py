from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied

from .models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        """ Retrieve the user object, and check if it matches the current user. """
        obj = super().get_object(queryset=queryset)
        if obj != self.request.user:
            raise PermissionDenied()
        return obj
