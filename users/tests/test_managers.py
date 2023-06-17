from django.test import TestCase
from users.models import User


class UserManagerTest(TestCase):

    def test_create_user(self):
        user = User.objects.create_user('test@example.com', 'testpassword')
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpassword'))

    def test_create_superuser(self):
        user = User.objects.create_superuser('test@example.com', 'testpassword')
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpassword'))
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
