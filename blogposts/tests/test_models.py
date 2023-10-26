from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from blogposts.models import BlogPost, Category, Language

User = get_user_model()


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Test Category')

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Category Name')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_object_name_is_name(self):
        category = Category.objects.get(id=1)
        expected_object_name = f'{category.name}'
        self.assertEqual(expected_object_name, str(category))


class LanguageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Language.objects.create(name='Test Language')

    def test_name_label(self):
        language = Language.objects.get(id=1)
        field_label = language._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Language Name')

    def test_name_max_length(self):
        language = Language.objects.get(id=1)
        max_length = language._meta.get_field('name').max_length
        self.assertEqual(max_length, 150)

    def test_object_name_is_name(self):
        language = Language.objects.get(id=1)
        expected_object_name = f'{language.name}'
        self.assertEqual(expected_object_name, str(language))


class BlogPostTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            email='test@user.com', password='testpass'
        )
        cls.category1 = Category.objects.create(name='Category 1')
        cls.category2 = Category.objects.create(name='Category 2')
        cls.language1 = Language.objects.create(name='English')
        cls.language2 = Language.objects.create(name='French')

        cls.blogpost1 = BlogPost.objects.create(
            title='Test Blog Post 1',
            sub_title='Test Sub-title 1',
            author=cls.user,
            content='Test Content 1'
        )
        cls.blogpost1.category.add(cls.category1)
        cls.blogpost1.category.add(cls.category2)
        cls.blogpost1.language.add(cls.language1)
        cls.blogpost1.language.add(cls.language2)

        cls.blogpost2 = BlogPost.objects.create(
            title='Test Blog Post 2',
            sub_title='Test Sub-title 2',
            author=cls.user,
            content='Test Content 2'
        )
        cls.blogpost2.category.add(cls.category2)
        cls.blogpost2.language.add(cls.language2)

        cls.blogpost3 = BlogPost.objects.create(
            title='Test Blog Post 3',
            sub_title='Test Sub-title 3',
            author=cls.user,
            content='Test Content 3'
        )
        cls.blogpost3.category.add(cls.category1, cls.category2)
        cls.blogpost3.language.add(cls.language1, cls.language2)

    
    def test_title_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'Title')

    def test_title_max_length(self):
        blogpost = BlogPost.objects.get(id=1)
        max_length = blogpost._meta.get_field('title').max_length
        self.assertEqual(max_length, 150)

    def test_sub_title_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field('sub_title').verbose_name
        self.assertEqual(field_label, 'Sub-title')

    def test_sub_title_max_length(self):
        blogpost = BlogPost.objects.get(id=1)
        max_length = blogpost._meta.get_field('sub_title').max_length
        self.assertEqual(max_length, 300)

    def test_category_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    def test_language_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field('language').verbose_name
        self.assertEqual(field_label, 'language')

    def test_author_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_date_published_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field('date_published').verbose_name
        self.assertEqual(field_label, 'Published')

    def test_date_modified_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field('date_modified').verbose_name
        self.assertEqual(field_label, 'Last Modified')

    def test_content_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'Content')

    def test_object_name_is_title_and_sub_title(self):
        blogpost = BlogPost.objects.get(id=1)
        expected_object_name = f'Title: {blogpost.title}, Sub-title: {blogpost.sub_title}'
        self.assertEqual(expected_object_name, str(blogpost))

    def test_ordering(self):
        expected_ordering = [
            self.blogpost3.pk,
            self.blogpost2.pk,
            self.blogpost1.pk,
        ]
        qs = BlogPost.objects.all().values_list('pk', flat=True)
        self.assertListEqual(list(qs), expected_ordering)

    def test_category_name(self):
        category1 = Category.objects.get(id=self.category1.id)
        category2 = Category.objects.get(id=self.category2.id)
        self.assertEqual(str(category1), "Category 1")
        self.assertEqual(str(category2), "Category 2")

    def test_language_name(self):
        language1 = Language.objects.get(id=self.language1.id)
        language2 = Language.objects.get(id=self.language2.id)
        self.assertEqual(str(language1), "English")
        self.assertEqual(str(language2), "French")

    def test_blog_post_fields(self):
        blog_post = BlogPost.objects.get(id=self.blogpost1.id)
        self.assertEqual(blog_post.title, "Test Blog Post 1")
        self.assertEqual(blog_post.sub_title, "Test Sub-title 1")
        self.assertEqual(blog_post.author, self.user)
        self.assertEqual(blog_post.content, "Test Content 1")
        self.assertEqual(blog_post.category.count(), 2)
        self.assertIn(self.category1, blog_post.category.all())
        self.assertIn(self.category2, blog_post.category.all())
        self.assertEqual(blog_post.language.count(), 2)
        self.assertIn(self.language1, blog_post.language.all())
        self.assertIn(self.language2, blog_post.language.all())

    def test_blog_post_dates(self):
        blog_post = BlogPost.objects.get(id=self.blogpost1.id)
        self.assertLess(blog_post.date_published, timezone.now())
        self.assertLess(blog_post.date_modified, timezone.now())


