from django.test import TestCase


class TestHomePage(TestCase):

    def test_uses_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    