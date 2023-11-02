"""blogsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views
from users.forms import CustomAuthenticationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(
        template_name="registration/login.html",
        authentication_form=CustomAuthenticationForm), 
        name='login'
        ),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', views.HomePageView.as_view(), name='home'),
    path('japanese/', views.JapaneseHomeView.as_view(), name='japanese-home'),
    path('japanese/baby/', views.JapaneseBabyView.as_view(), name='japanese-baby'),
    path('japanese/resources/', views.JapaneseResourcesView.as_view(), name='japanese-resources'),
    path('blog/', include('blogposts.urls')),
    path('users/', include('users.urls')),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    