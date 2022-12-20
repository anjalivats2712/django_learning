from django.test import TestCase,SimpleTestCase
from .models import Post
from django.urls import reverse


# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_home_status_code_check(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)
    def test_home_status_code_by_name(self):
        resp=self.client.get(reverse("home"))
        self.assertEqual(resp.status_code,200)
    def test_home_correct_template_used(self):
        resp=self.client.get(reverse("home"))
        self.assertTemplateUsed(resp,"Homepage.html")
    def test_contact_status_code_check(self):
        response2=self.client.get('/contact')
        self.assertEqual(response2.status_code,200)
    def test_query_page_status_code(self):
        response=self.client.get('/query')
        self.assertEqual(response.status_code,200)
class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(name="anjali",content="vats")
    def test_post_content(self):
        post=Post.objects.get(id=1)
        expected_name=post.name
        expected_content=post.content
        self.assertEqual(expected_name,'anjali')
        self.assertEqual(expected_content,'vats')

