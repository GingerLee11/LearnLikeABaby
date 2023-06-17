from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class LoginView(TemplateView):
    pass


class RegisterView(TemplateView):
    pass
