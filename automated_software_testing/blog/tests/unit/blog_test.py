from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('My Day', 'Larry')

        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(b2.__repr__(), 'My Day by Larry (0 posts)')

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b.posts = ['test']
        b2 = Blog('My Day', 'Larry')
        b2.posts = ['test', 'another']

        self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(b2.__repr__(), 'My Day by Larry (2 posts)')

    def test_create_post_in_blog(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].content, 'Test Content')
