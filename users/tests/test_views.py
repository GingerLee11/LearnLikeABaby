from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class UserDetailViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword',
        )
        self.client.login(username='testuser', password='testpassword')

    def test_user_detail_view(self):
        response = self.client.get(reverse('user-detail', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
        self.assertContains(response, 'test@example.com')
        self.assertTemplateUsed(response, 'users/user_detail.html')
