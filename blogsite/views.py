from django.views.generic import TemplateView
from django.contrib.auth import login
from django.views import generic
from django.urls import reverse_lazy

from users.forms import CustomUserCreationForm


class HomePageView(TemplateView):
    template_name = "home.html"


class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
