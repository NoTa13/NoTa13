from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def test_create_post(self):
        post = Post.objects.create(title="Тестовый пост", content="Содержимое поста")
        self.assertEqual(post.title, "Тестовый пост")
        self.assertEqual(post.content, "Содержимое поста")
