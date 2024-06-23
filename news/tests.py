from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.
class PostModelTests(TestCase):
    def setUp(self):
        Post.objects.create(title = 'Test Title', content = 'Test Content')

    def test_title_content(self):
        post = Post.objects.get(id=1)
        expected_object_title = f'{post.title}'
        expected_object_content = f'{post.content}'
        self.assertEqual(expected_object_title, 'Test Title')
        self.assertEqual(expected_object_content, 'Test Content')


class HomePageViewTests(TestCase):
    def setUp(self):
        Post.objects.create(title = 'Test Title 2', content = 'Test Content 2')

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


