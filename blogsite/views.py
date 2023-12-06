from django.views.generic import TemplateView
from django.contrib.auth import login
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render

from users.forms import CustomUserCreationForm


class HomePageView(TemplateView):
    template_name = "home.html"

# Japanese views:

class JapaneseHomeView(TemplateView):
    template_name = "japanese/japanese_home.html"


class JapaneseBabyView(TemplateView):
    template_name = "japanese/japanese_baby.html"


# Block partial views:

def japanese_eating_block(request):
    return render(request, 'japanese/partials/eating_block.html')


class JapaneseResourcesView(TemplateView):
    template_name = "japanese/japanese_resources.html"


class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
