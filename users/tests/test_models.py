from django.test import TestCase
from users.models import User


class UserModelTest(TestCase):

    def test_user_creation(self):
        User.objects.create_user('testuser', 'test@example.com', 'testpassword')
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpassword'))
