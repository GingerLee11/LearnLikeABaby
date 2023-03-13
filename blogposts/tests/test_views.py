from django.test import TestCase


class TestBlogPostListPage(TestCase):

    def test_uses_blog_post_list_template(self):
        response = self.client.get('/blogposts')
        self.assertTemplateUsed(response, 'blogposts/blogpost_list.html')

    