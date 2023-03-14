from django.test import TestCase
from django.urls import reverse

from datetime import timedelta

from blogposts.models import BlogPost
from blogposts.views import BlogPostListView


class BlogPostListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 2 blog posts for testing
        cls.blogpost1 = BlogPost.objects.create(
            title='Test Blog Post 1',
            content='Test Content 1'
        )
        cls.blogpost2 = BlogPost.objects.create(
            title='Test Blog Post 2',
            content='Test Content 2'
        )

    def test_blogpost_list_view_status_code(self):
        response = self.client.get(reverse('blogpost-list'))
        self.assertEqual(response.status_code, 200)

    def test_blogpost_list_view_template_name(self):
        response = self.client.get(reverse('blogpost-list'))
        self.assertTemplateUsed(response, 'blogposts/blogpost_list.html')

    def test_blogpost_list_view_pagination(self):
        # Create 8 additional blog posts
        for i in range(8):
            BlogPost.objects.create(
                title=f'Test Blog Post {i+3}',
                content=f'Test Content {i+3}'
            )
        response = self.client.get(reverse('blogpost-list'))
        self.assertEqual(len(response.context['object_list']), 10)

    def test_blogpost_list_view_ordering(self):
        BlogPost.objects.all().delete()
        # Create 3 blog posts with different dates
        blogpost1 = BlogPost.objects.create(
            title='Test Blog Post 1',
            content='Test Content 1'
        )
        blogpost2 = BlogPost.objects.create(
            title='Test Blog Post 2',
            content='Test Content 2'
        )
        blogpost3 = BlogPost.objects.create(
            title='Test Blog Post 3',
            content='Test Content 3'
        )
        blogpost3.date_published = blogpost1.date_published + timedelta(days=1)
        blogpost3.save()
        blogpost2.date_published = blogpost1.date_published - timedelta(days=1)
        blogpost2.save()

        response = self.client.get(reverse('blogpost-list'))

        self.assertQuerysetEqual(
            response.context['object_list'],
            [blogpost3, blogpost1, blogpost2]
        )



class BlogPostDetailViewTestCase(TestCase):
    def setUp(self):
        self.blogpost = BlogPost.objects.create(
            title='Test BlogPost',
            content='This is a test blogpost'
        )
        self.url = reverse('blogpost-detail', kwargs={'pk': self.blogpost.pk})

    def test_blogpost_detail_view_should_return_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_blogpost_detail_view_should_use_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'blogposts/blogpost_detail.html')

    def test_blogpost_detail_view_should_contain_blogpost(self):
        response = self.client.get(self.url)
        self.assertEqual(response.context['blogpost'], self.blogpost)

    def test_blogpost_detail_view_should_return_404_for_invalid_pk(self):
        url = reverse('blogpost-detail', kwargs={'pk': self.blogpost.pk + 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

