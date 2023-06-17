from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class TestHomePage(TestCase):

    def test_uses_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    
class RegistrationViewTest(TestCase):

    def test_can_register_user(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        })

        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertTrue(get_user_model().objects.filter(username='testuser').exists())


class LoginViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword',
        )

    def test_can_login_user(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword',
        })

        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertEqual(int(self.client.session['_auth_user_id']), self.user.pk)
