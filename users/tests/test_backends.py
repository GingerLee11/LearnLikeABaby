from django.test import TestCase
from django.contrib.auth import get_user_model
from users.backends import EmailBackend

User = get_user_model()


class EmailBackendTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword',
        )
        self.backend = EmailBackend()

    def test_authenticate_with_username(self):
        user = self.backend.authenticate(None, username='testuser', password='testpassword')
        self.assertEqual(user, self.user)

    def test_authenticate_with_email(self):
        user = self.backend.authenticate(None, username='test@example.com', password='testpassword')
        self.assertEqual(user, self.user)

    def test_authenticate_with_wrong_password(self):
        user = self.backend.authenticate(None, username='testuser', password='wrongpassword')
        self.assertIsNone(user)

    def test_authenticate_with_nonexistent_user(self):
        user = self.backend.authenticate(None, username='nonexistent', password='testpassword')
        self.assertIsNone(user)
