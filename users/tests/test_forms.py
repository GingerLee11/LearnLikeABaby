from django.test import TestCase
from django.contrib.auth import get_user_model

from users.forms import CustomUserCreationForm, CustomAuthenticationForm

User = get_user_model()


class CustomUserCreationFormTest(TestCase):

    def test_form_has_fields(self):
        form = CustomUserCreationForm()
        self.assertIn('email', form.fields)
        self.assertIn('password1', form.fields)
        self.assertIn('password2', form.fields)

    def test_user_creation_form_valid(self):
        form = CustomUserCreationForm(data={
            'username': 'admin',
            'email': 'example@test.com',
            'password1': 'supertest',
            'password2': 'supertest',
        })
        self.assertTrue(form.is_valid())

    def test_user_creation_form_duplicate_email(self):
        User.objects.create_user(username='testuser', email='example@test.com', password='supertest')
        form = CustomUserCreationForm(data={
            'username': 'testuser2',
            'email': 'example@test.com',
            'password1': 'supertest',
            'password2': 'supertest',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_user_creation_form_duplicate_username(self):
        User.objects.create_user(username='testuser', email='example@test.com', password='supertest')
        form = CustomUserCreationForm(data={
            'username': 'testuser',
            'email': 'example@test1.com',
            'password1': 'supertest',
            'password2': 'supertest',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)


class CustomAuthenticationFormTest(TestCase):

    def setUp(self):
        User.objects.create_user(email='example@test.com', password='supertest')

    def test_form_has_fields(self):
        form = CustomAuthenticationForm()
        self.assertIn('username', form.fields)
        self.assertIn('password', form.fields)

    def test_user_authentication_form_valid(self):
        form = CustomAuthenticationForm(data={
            'username': 'example@test.com',
            'password': 'supertest',
        })
        self.assertTrue(form.is_valid())
